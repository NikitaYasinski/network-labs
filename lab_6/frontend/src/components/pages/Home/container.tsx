import React, {
  useCallback, useContext, useEffect, useState,
} from 'react';
import { RowType } from '@/components/pages/Home/types';
import { adaptRowData } from '@/components/pages/Home/common/utils/adaptRowData';
import { StoreContext } from '@/store/context';
// import { getDefaultData } from '@/components/pages/Home/common/utils/getDefaultData';
import RequestService from '@/services/RequestService';
import Home from './component';

const HomeContainer = () => {
  const state = useContext(StoreContext);
  const [tableData, setTableData] = useState<RowType[]>(adaptRowData(state.selectedItem));

  useEffect(() => {
    const getInitialData = async () => {
      await RequestService.get(state.selectedItemState);
    };

    getInitialData();
  }, []);

  useEffect(() => {
    setTableData(adaptRowData(state.selectedItem));
  }, [state.selectedItem]);

  const onHeaderCheckBoxClick = useCallback((checked: boolean) => {
    const updatedTableData = tableData.map(student => ({
      ...student,
      selected: checked,
    }));

    setTableData(updatedTableData as RowType[]);
  }, [tableData]);

  const onCheckBoxClick = useCallback((item: RowType) => {
    const selectedItem = tableData.find(element => element.id === item.id);

    if (!selectedItem) {
      return;
    }

    const updatedTableData = tableData.map(tableItem => {
      if (tableItem.id === item.id) {
        const updatedTableItem = {
          ...tableItem,
          selected: !tableItem.selected,
        };
        return updatedTableItem;
      }
      return tableItem;
    });

    setTableData(updatedTableData as RowType[]);
  }, [tableData]);

  return (
    <Home
      onHeaderCheckBoxClick={onHeaderCheckBoxClick}
      onCheckBoxClick={onCheckBoxClick}
      headerCells={[]}
      tableData={tableData} />
  );
};

export default HomeContainer;
