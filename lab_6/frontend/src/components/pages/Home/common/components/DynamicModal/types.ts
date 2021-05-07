import { InputCellsStateType } from '@/components/blocks/CheckedTableRow/utils/getInitialInputCellsState';
import { Cell } from '@/components/pages/Home/types';

export interface Props {
  visibility: boolean;
  cells: Cell[];
  onChange: (type: string, text: string) => void;
  inputCellState: InputCellsStateType;
  onClose: () => void;
  onSaveButtonClick: (inputCellState: InputCellsStateType) => void;
}
