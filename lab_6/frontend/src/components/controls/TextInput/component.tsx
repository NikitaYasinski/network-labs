import React from 'react';
import { TextField } from '@material-ui/core';
import { Props } from './types';

const TextInput = ({
  label, value, onChange, required = false, className,
}: Props) => (
  <TextField
    label={label}
    className={className}
    value={value}
    onChange={onChange}
    variant="outlined"
    required={required} />
);

export default React.memo(TextInput);
