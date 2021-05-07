import { ChangeEvent } from 'react';

export interface Props {
  label: string;
  onChange: (event: ChangeEvent<HTMLTextAreaElement | HTMLInputElement>) => void;
  required?: boolean;
  value: string;
  className?: string;
}
