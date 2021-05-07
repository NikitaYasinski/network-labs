import React from 'react';
import MaterialButton from '@material-ui/core/Button';
import { Props } from './types';

const Button = ({ onClick, label }: Props) => (
  <MaterialButton onClick={onClick} variant="contained" color="primary">
    {label}
  </MaterialButton>
);

export default React.memo(Button);
