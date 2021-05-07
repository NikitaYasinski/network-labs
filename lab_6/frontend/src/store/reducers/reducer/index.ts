import { useReducer } from 'react';
import { reducer, reducerInitialState } from '@/store/reducers/reducer/reducer';

export const useStudentsReducer = () => {
  const [state, dispatch] = useReducer(reducer, reducerInitialState);

  return [state, dispatch];
};
