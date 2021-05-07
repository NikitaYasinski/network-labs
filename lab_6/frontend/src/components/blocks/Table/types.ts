import React from 'react';
import { HeadCell } from '@/components/blocks/TableHeader/types';

export interface Props {
  children: React.ReactNode;
  headCells?: HeadCell[];
  onHeaderCheckBoxClick?: (value: boolean) => void;
}
