import {
  ADD_NEW_ITEM,
  DELETE_ITEM,
  SET_SELECTED_ITEM,
  SET_SELECTED_ITEM_STATE,
  UPDATE_ITEM,
} from '@/constants';
import {
  Faculty, Group, Student, Teacher,
} from '@/models';
import { SelectItems } from '@/components/pages/Home/common/components/Controls/types';
import { ItemType } from '@/shared/types';

export type SelectedItemActionType = { type: typeof SET_SELECTED_ITEM, payload: { selectedItem: Student[] | Teacher[] | Group[] | Faculty[] } };
export type SetSelectedItemType = (students: Student[] | Teacher[] | Group[] | Faculty[]) => SelectedItemActionType;

export type SelectedItemStateActionType = { type: typeof SET_SELECTED_ITEM_STATE, payload: { selectedItemState: SelectItems }};
export type SetSelectedItemStateType = (selectedItemState: SelectItems) => SelectedItemStateActionType;

export type AddNewItemActionType = { type: typeof ADD_NEW_ITEM, payload: { item: ItemType }};
export type AddNewItemType = (item: ItemType) => AddNewItemActionType;

export type DeleteItemActionType = { type: typeof DELETE_ITEM, payload: { id: number }};
export type DeleteItemType = (id: number) => DeleteItemActionType;

export type UpdateItemActionType = { type: typeof UPDATE_ITEM, payload: { item: ItemType }};
export type UpdateItemType = (item: ItemType) => UpdateItemActionType;
