import {
  ADD_NEW_ITEM, DELETE_ITEM, SET_SELECTED_ITEM, SET_SELECTED_ITEM_STATE, UPDATE_ITEM,
} from '@/constants';
import {
  AddNewItemType, DeleteItemType,
  SetSelectedItemStateType,
  SetSelectedItemType, UpdateItemType,
} from '@/store/actions/students/types';

export const setSelectedItem: SetSelectedItemType = selectedItem => ({
  type: SET_SELECTED_ITEM,
  payload: {
    selectedItem,
  },
});

export const setSelectedItemState: SetSelectedItemStateType = selectedItemState => ({
  type: SET_SELECTED_ITEM_STATE,
  payload: {
    selectedItemState,
  },
});

export const addNewItem: AddNewItemType = item => ({
  type: ADD_NEW_ITEM,
  payload: {
    item,
  },
});

export const deleteItem: DeleteItemType = (id: number) => ({
  type: DELETE_ITEM,
  payload: {
    id,
  },
});

export const updateItem: UpdateItemType = item => ({
  type: UPDATE_ITEM,
  payload: {
    item,
  },
});
