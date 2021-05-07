export interface Props {
  headCells: HeadCell[];
  onCheckBoxClick?: (value: boolean) => void;
}

export interface HeadCell {
  label: string;
}
