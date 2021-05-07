import React, { useReducer } from 'react';
import Router from '@/Router';
import { Container, makeStyles } from '@material-ui/core';
import { StoreContext, DispatchContext } from '@/store/context';
import { reducer, reducerInitialState } from '@/store/reducers/reducer/reducer';
import {
  DefaultToastContainer,
  ToastProvider,
} from 'react-toast-notifications';

const useStyles = makeStyles({
  root: {
    height: '98vh',
  },
  toastContainer: {
    zIndex: 9999,
  },
});

const MyCustomToastContainer = (props: any) => (
  <DefaultToastContainer {...props} />
);

function App() {
  const [state, dispatch] = useReducer(reducer, reducerInitialState);
  const classes = useStyles();

  return (
    <DispatchContext.Provider value={dispatch}>
      <StoreContext.Provider value={state}>
        <ToastProvider
          autoDismissTimeout={2000}
          autoDismiss placement="bottom-right"
          components={{ ToastContainer: (props: any) => <MyCustomToastContainer {...props} style={{ zIndex: 9999 }} /> }}
        >
          <Container className={classes.root} fixed>
            <Router />
          </Container>
        </ToastProvider>
      </StoreContext.Provider>
    </DispatchContext.Provider>
  );
}

export default App;
