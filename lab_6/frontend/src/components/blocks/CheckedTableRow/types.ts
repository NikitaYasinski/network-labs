import React from 'react';
import { RowType } from '@/components/pages/Home/types';

export interface Props {
  selected: boolean;
  onCheckBoxClick: () => void;
  tableItem: RowType;
}
