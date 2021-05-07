import React from 'react';
import { Store } from '@/store/context/types';
import { Actions } from '@/store/reducers/reducer/types';
import { SelectItems } from '@/components/pages/Home/common/components/Controls/types';

export const StoreContext = React.createContext<Store>({
  selectedItemState: SelectItems.Student,
  selectedItem: [],
});

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const DispatchContext = React.createContext<React.Dispatch<Actions>>((action: Actions) => {});
