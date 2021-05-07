import React from 'react';
import Paper from '@material-ui/core/Paper';
import Table from '@/components/blocks/Table';
import TableContainer from '@material-ui/core/TableContainer';
import { useStyles } from '@/components/pages/Home/styles';
import { Box } from '@material-ui/core';
import Controls from '@/components/pages/Home/common/components/Controls';
import CheckedTableRow from '@/components/blocks/CheckedTableRow/component';
import { Props } from './types';

const Home = ({
  onHeaderCheckBoxClick, onCheckBoxClick, tableData, headerCells,
}: Props) => {
  const classes = useStyles();

  return (
    <Box className={classes.container}>
      <Box className={classes.controls}>
        <Controls />
      </Box>
      <Paper>
        <TableContainer>
          <Table
            headCells={headerCells}
            onHeaderCheckBoxClick={onHeaderCheckBoxClick}
          >
            {tableData.map(tableItem => (
              <CheckedTableRow
                key={tableItem.id}
                selected={tableItem.selected}
                onCheckBoxClick={() => onCheckBoxClick(tableItem)}
                tableItem={tableItem} />
            ))}
          </Table>
        </TableContainer>
      </Paper>
    </Box>
  );
};

export default React.memo(Home);
