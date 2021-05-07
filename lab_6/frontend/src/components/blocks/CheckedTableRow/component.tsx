import React, {
  MouseEvent, useCallback, useContext, useState,
} from 'react';
import MaterialTableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import {
  Grid, IconButton,
} from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import {
  getInitialInputCellsState,
  InputCellsStateType,
} from '@/components/blocks/CheckedTableRow/utils/getInitialInputCellsState';
import DynamicModal from '@/components/pages/Home/common/components/DynamicModal';
import RequestService from '@/services/RequestService';
import { DispatchContext, StoreContext } from '@/store/context';
import { useToastResponse } from '@/utils/hooks/useToastResponse';
import ResponseStatusService from '@/services/ResponseStatusService';
import { deleteItem, updateItem } from '@/store/actions/students';
import { useStyles } from './styles';
import { Props } from './types';

const CheckedTableRow = ({ tableItem }: Props) => {
  const state = useContext(StoreContext);
  const dispatch = useContext(DispatchContext);
  const classes = useStyles();
  const [rowOpened, setRowOpened] = useState(false);
  const [inputCellsState, setInputCellsState] = useState(getInitialInputCellsState(tableItem.cells));
  const invokeToastResponse = useToastResponse();

  const onDeleteIconClick = async (event: MouseEvent<HTMLButtonElement>) => {
    event.stopPropagation();
    try {
      const statusCode = await RequestService.del(`${state.selectedItemState}/${tableItem.id}`);
      invokeToastResponse({ statusCode });
      if (ResponseStatusService.handleStatusCode(statusCode).type === 'success') {
        dispatch(deleteItem(tableItem.id));
      }
    } catch (error) {
      invokeToastResponse({ customStatusObject: { type: 'error', message: error.message } });
    }
  };

  const onSaveButtonClick = useCallback(async (inputCellState: InputCellsStateType) => {
    try {
      const [statusCode, updatedItem] = await RequestService.put(`${state.selectedItemState}/${tableItem.id}`, inputCellState);
      invokeToastResponse({ statusCode });
      if (ResponseStatusService.handleStatusCode(statusCode).type === 'success') {
        dispatch(updateItem(updatedItem));
      }
    } catch (error) {
      invokeToastResponse({ customStatusObject: { type: 'error', message: error.message } });
    }
  }, [state.selectedItemState, tableItem.id]);

  const onChangeInput = (type: string, value: string) => {
    const updatedState = {
      ...inputCellsState,
      [type]: value,
    };
    setInputCellsState(updatedState);
  };

  // const onCheckBoxPress = (event: MouseEvent) => {
  //   event.stopPropagation();
  //   onCheckBoxClick();
  // };

  const onCloseModal = () => {
    setRowOpened(false);
  };

  const openRowDetails = () => {
    setRowOpened(!rowOpened);
  };

  return (
    <>
      <MaterialTableRow
        className={classes.root}
        onClick={openRowDetails}
        hover
        role="checkbox"
        aria-checked={false}
        tabIndex={-1}
      >
        <TableCell padding="checkbox">
          <Grid
            container
            justify="center"
            alignItems="center"
            className={classes.checkBoxWrap}
          >
            <Grid item xs={6}>
              <IconButton onClick={onDeleteIconClick} aria-label="delete">
                <DeleteIcon />
              </IconButton>
            </Grid>
          </Grid>
        </TableCell>
        {tableItem.cells.map(cell => (
          <TableCell key={cell.type} align="center">{cell.value}</TableCell>
        ))}
      </MaterialTableRow>
      <DynamicModal
        onClose={onCloseModal}
        visibility={rowOpened}
        cells={tableItem.cells}
        onChange={onChangeInput}
        onSaveButtonClick={onSaveButtonClick}
        inputCellState={inputCellsState} />
    </>
  );
};

export default React.memo(CheckedTableRow);
