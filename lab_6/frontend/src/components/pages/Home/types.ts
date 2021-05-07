import { HeadCell } from '@/components/blocks/TableHeader/types';

export interface RowData {
  id: number;
  selected: false;
  cells: Cell[];
}

export interface Cell {
  type: string;
  value: string;
}

export interface Props {
  onHeaderCheckBoxClick: (checked: boolean) => void;
  onCheckBoxClick: (item: RowType) => void;
  tableData: RowType[];
  headerCells: HeadCell[];
}

export type RowType = RowData;
