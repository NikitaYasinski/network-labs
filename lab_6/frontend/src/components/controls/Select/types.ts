import { ChangeEvent } from 'react';

export interface Props {
  value: string;
  onChange: (event: ChangeEvent<{ value: any }>) => void;
  items: { label: string; value: string }[];
}
