import React from 'react';
import { MenuItem } from '@material-ui/core';
import MaterialSelect from '@material-ui/core/Select';
import { Props } from './types';

const Select = ({ value, onChange, items }: Props) => (
  <MaterialSelect
    value={value}
    onChange={onChange}
  >
    {items.map(item => (
      <MenuItem key={item.value} value={item.value}>{item.label}</MenuItem>
    ))}
  </MaterialSelect>
);

export default React.memo(Select);
