import { Cell } from '@/components/pages/Home/types';

export type InputCellsStateType = { [key: string]: string };

export const getInitialInputCellsState = (cells: Cell[]) => {
  const initialState: InputCellsStateType = cells.reduce((accum: InputCellsStateType, cell) => {
    // eslint-disable-next-line no-param-reassign
    accum[cell.type] = cell.value;

    return accum;
  }, {});

  return initialState;
};
