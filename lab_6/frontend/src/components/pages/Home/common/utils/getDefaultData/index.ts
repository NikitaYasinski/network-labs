import { SelectItems } from '@/components/pages/Home/common/components/Controls/types';
import {
  MOCKED_FACULTIES, MOCKED_GROUPS, MOCKED_STUDENTS, MOCKED_TEACHERS,
} from '@/constants';

export const getDefaultData = (selectedState: SelectItems) => {
  switch (selectedState) {
    case SelectItems.Faculty:
      return MOCKED_FACULTIES;
    case SelectItems.Student:
      return MOCKED_STUDENTS;
    case SelectItems.Teacher:
      return MOCKED_TEACHERS;
    case SelectItems.Group:
      return MOCKED_GROUPS;
    default:
      return MOCKED_STUDENTS;
  }
};
