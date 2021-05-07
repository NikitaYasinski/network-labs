import React from 'react';
import {
  Container, Grid, IconButton, Modal,
} from '@material-ui/core';
import TextInput from '@/components/controls/TextInput/component';
import CloseIcon from '@material-ui/icons/Close';
import Button from '@/components/controls/Button';
import { Props } from './types';
import { useStyles } from './styles';

const DynamicModal = ({
  visibility,
  cells,
  onChange,
  inputCellState,
  onClose,
  onSaveButtonClick,
}: Props) => {
  const classes = useStyles();

  return (
    <Modal open={visibility} className={classes.modal}>
      <Container className={classes.modalContainer}>
        <Grid container justify="center" alignItems="center">
          <Grid xs={12} item className={classes.closeIcon}>
            <IconButton onClick={onClose}>
              <CloseIcon />
            </IconButton>
          </Grid>
          {cells.map(cell => (
            <Grid
              key={cell.type}
              xs={12}
              item
            >
              <TextInput
                className={classes.item}
                label={cell.type}
                value={inputCellState[cell.type]}
                onChange={event => onChange(cell.type, event.target.value)} />
            </Grid>
          ))}
          <Grid item xs={12}>
            <Button label="Сохранить" onClick={() => onSaveButtonClick(inputCellState)} />
          </Grid>
        </Grid>
      </Container>
    </Modal>
  );
};

export default React.memo(DynamicModal);
