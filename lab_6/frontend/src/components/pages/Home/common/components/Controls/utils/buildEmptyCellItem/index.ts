import { SelectItems } from '@/components/pages/Home/common/components/Controls/types';
import { Cell } from '@/components/pages/Home/types';

type buildEmptyCellItemType = (selectedValue: SelectItems) => Cell[];

export const buildEmptyCellItem: buildEmptyCellItemType = (selectedValue: SelectItems) => {
  switch (selectedValue) {
    case SelectItems.Faculty:
      return [{ type: 'name', value: '' }];
    case SelectItems.Student:
      return [
        { type: 'name', value: '' },
        { type: 'email', value: '' },
        { type: 'phone', value: '' },
        { type: 'group', value: '' },
      ];
    case SelectItems.Teacher:
      return [
        { type: 'name', value: '' },
        { type: 'email', value: '' },
        { type: 'phone', value: '' },
        { type: 'group', value: '' },
        { type: 'subject', value: '' },
      ];
    case SelectItems.Group:
      return [{ type: 'number', value: '' }, { type: 'faculty', value: '' }];
    default:
      return [{ type: 'name', value: '' }];
  }
};
