import React, {
  ChangeEvent, useCallback, useContext, useEffect, useState,
} from 'react';
import { Grid } from '@material-ui/core';
import Select from '@/components/controls/Select';
import Button from '@/components/controls/Button';
import DynamicModal from '@/components/pages/Home/common/components/DynamicModal';
import {
  getInitialInputCellsState,
  InputCellsStateType,
} from '@/components/blocks/CheckedTableRow/utils/getInitialInputCellsState';
import { buildEmptyCellItem } from '@/components/pages/Home/common/components/Controls/utils/buildEmptyCellItem';
import RequestService from '@/services/RequestService';
import { DispatchContext, StoreContext } from '@/store/context';
import { addNewItem, setSelectedItem, setSelectedItemState } from '@/store/actions/students';
import { useToastResponse } from '@/utils/hooks/useToastResponse';
import ResponseStatusService from '@/services/ResponseStatusService';
import { SelectItems } from './types';

const Controls = () => {
  const dispatch = useContext(DispatchContext);
  const state = useContext(StoreContext);
  const [selectedValue, setSelectedValue] = useState<SelectItems>(SelectItems.Student);
  const [inputCellsState, setInputCellsState] = useState(getInitialInputCellsState(buildEmptyCellItem(selectedValue)));
  const [modalVisibility, setModalVisibility] = useState(false);
  const [cells, setCells] = useState(buildEmptyCellItem(selectedValue));
  const invokeToastResponse = useToastResponse();

  useEffect(() => {
    setInputCellsState(getInitialInputCellsState(buildEmptyCellItem(selectedValue)));
    setCells(buildEmptyCellItem(selectedValue));
  }, [selectedValue]);

  const onSaveButtonClick = useCallback(async (inputCellState: InputCellsStateType) => {
    try {
      const [statusCode, item] = await RequestService.post(state.selectedItemState, inputCellState);
      invokeToastResponse({ statusCode });
      if (ResponseStatusService.handleStatusCode(statusCode).type === 'success') {
        dispatch(addNewItem(item));
      }
    } catch (error) {
      invokeToastResponse({ customStatusObject: { type: 'error', message: error.message } });
    }
  }, [state.selectedItemState]);

  const onButtonClick = () => {
    setModalVisibility(true);
  };

  const onChangeInput = (type: string, text: string) => {
    const updatedState = {
      ...inputCellsState,
      [type]: text,
    };
    setInputCellsState(updatedState);
  };

  const onCloseModal = () => {
    setModalVisibility(false);
  };

  const onChange = useCallback(async (event: ChangeEvent<{ value: SelectItems }>) => {
    setSelectedValue(event.target.value as SelectItems);

    const data = await RequestService.get(event.target.value);
    dispatch(setSelectedItem(data));
    dispatch(setSelectedItemState(event.target.value));
  }, []);

  const selectableItems = [{
    label: 'Группы',
    value: SelectItems.Group,
  },
  {
    label: 'Студенты',
    value: SelectItems.Student,
  },
  {
    label: 'Факультет',
    value: SelectItems.Faculty,
  },
  {
    label: 'Преподаватели',
    value: SelectItems.Teacher,
  },
  ];
  return (
    <>
      <Grid container justify="space-between" alignItems="center">
        <Grid item>
          <Select
            value={selectedValue}
            items={selectableItems}
            onChange={onChange} />
        </Grid>
        <Grid item>
          <Button onClick={onButtonClick} label="Добавить" />
        </Grid>
      </Grid>
      <DynamicModal
        visibility={modalVisibility}
        cells={cells}
        onChange={onChangeInput}
        inputCellState={inputCellsState}
        onClose={onCloseModal}
        onSaveButtonClick={onSaveButtonClick} />
    </>
  );
};

export default React.memo(Controls);
