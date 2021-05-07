import {
  AddNewItemActionType, DeleteItemActionType,
  SelectedItemActionType,
  SelectedItemStateActionType, UpdateItemActionType,
} from '@/store/actions/students/types';

export type Actions =
  SelectedItemActionType | SelectedItemStateActionType
  | AddNewItemActionType | DeleteItemActionType | UpdateItemActionType;
