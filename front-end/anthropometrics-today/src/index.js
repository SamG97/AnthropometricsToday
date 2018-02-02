import React from 'react';
import ReactDOM from 'react-dom';
import { createBrowserHistory } from 'history';
import { Route, Router, Switch } from 'react-router';
import Camera from './camera';
import Error from './error';
import Report from './report';

let history = createBrowserHistory();

ReactDOM.render((
        <Router history={history}>
            <Switch>
                <Route exact path='/' component={Camera}/>
                <Route path='/report/:user/:twin' component={Report}/>
                <Route path='/' component={Error}/>
            </Switch>
        </Router>
    ), document.getElementById('root')
);
