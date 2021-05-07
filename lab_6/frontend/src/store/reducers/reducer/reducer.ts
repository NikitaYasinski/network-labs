import {
  ADD_NEW_ITEM,
  DELETE_ITEM,
  SET_SELECTED_ITEM,
  SET_SELECTED_ITEM_STATE,
  UPDATE_ITEM,
} from '@/constants';
import { Store } from '@/store/context/types';
import { SelectItems } from '@/components/pages/Home/common/components/Controls/types';
import { Actions } from './types';

export const reducerInitialState: Store = {
  selectedItemState: SelectItems.Student,
  selectedItem: [],
};

export const reducer: (state: Store, action: Actions) => Store = (state: Store, action: Actions) => {
  switch (action.type) {
    case SET_SELECTED_ITEM:
      return {
        ...state,
        selectedItem: action.payload.selectedItem,
      };
    case SET_SELECTED_ITEM_STATE:
      return {
        ...state,
        selectedItemState: action.payload.selectedItemState,
      };
    case ADD_NEW_ITEM:
      return {
        ...state,
        selectedItem: [...state.selectedItem, action.payload.item],
      };
    case DELETE_ITEM:
      return {
        ...state,
        selectedItem: state.selectedItem.filter(item => item.id !== action.payload.id),
      };
    case UPDATE_ITEM:
      return {
        ...state,
        selectedItem: state.selectedItem.map(item => (item.id === action.payload.item.id ? action.payload.item : item)),
      };
    default:
      return state;
  }
};
