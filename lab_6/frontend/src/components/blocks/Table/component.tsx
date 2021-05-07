import React from 'react';
import MaterialTable from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
// import TableHeader from '@/components/blocks/TableHeader';
import { Props } from './types';

const Table = ({ children }: Props) => (
  <MaterialTable
    aria-labelledby="tableTitle"
    size="medium"
    aria-label="enhanced table"
  >
    {/* {headCells && ( */}
    {/*  <TableHeader */}
    {/*    onCheckBoxClick={onHeaderCheckBoxClick} */}
    {/*    headCells={headCells} /> */}
    {/* )} */}
    <TableBody>{children}</TableBody>
  </MaterialTable>
);

export default React.memo(Table);
