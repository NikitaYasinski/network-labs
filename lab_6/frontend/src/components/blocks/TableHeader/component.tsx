import React, { useEffect, useState } from 'react';
import { TableCell, TableHead, Typography } from '@material-ui/core';
import TableRow from '@material-ui/core/TableRow';
import Checkbox from '@material-ui/core/Checkbox';
import { Props } from './types';

const TableHeader = ({ headCells, onCheckBoxClick }: Props) => {
  const [checked, setChecked] = useState(false);
  const onCheckBoxPress = () => {
    setChecked(!checked);
  };

  useEffect(() => {
    if (onCheckBoxClick) {
      onCheckBoxClick(checked);
    }
  }, [checked]);

  return (
    <TableHead>
      <TableRow>
        <TableCell padding="checkbox">
          <Checkbox onClick={onCheckBoxPress} checked={checked} />
        </TableCell>
        {headCells.map(headCell => (
          <TableCell key={headCell.label} align="center" padding="none">
            <Typography variant="subtitle2">{headCell.label}</Typography>
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
};

export default React.memo(TableHeader);
