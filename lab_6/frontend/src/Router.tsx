import React from 'react';
import { Router as ReactRouter, Switch, Route } from 'react-router-dom';
import { createBrowserHistory } from 'history';
import { HOME_PAGE } from '@/constants';
import Home from '@/components/pages/Home';

export const history = createBrowserHistory();

const Router = () => (
  <ReactRouter history={history}>
    <Switch>
      <Route exact path={HOME_PAGE} component={Home} />
    </Switch>
  </ReactRouter>
);

export default Router;
