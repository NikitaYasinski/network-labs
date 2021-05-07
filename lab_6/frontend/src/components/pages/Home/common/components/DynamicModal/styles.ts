import { makeStyles } from '@material-ui/core';

export const useStyles = makeStyles({
  modalContainer: {
    maxWidth: 700,
    backgroundColor: 'white',
    padding: 30,
    alignSelf: 'center',
    marginLeft: 20,
    marginRight: 20,
  },
  modal: {
    display: 'flex',
    justifyContent: 'center',
  },
  item: {
    width: '100%',
    marginTop: 20,
    marginBottom: 20,
  },
  closeIcon: {
    display: 'flex',
    justifyContent: 'flex-end',
    alignItems: 'flex-end',
  },
});
