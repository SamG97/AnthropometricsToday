import React from 'react';
import ReactDOM from 'react-dom';
import { Route, Router, Switch } from 'react-router';
import Camera from './camera';
import { PageNotFound, ServerError } from './errors';
import Report from './report';
import { history } from './requests/requestWrappers';

ReactDOM.render((
        <Router history={history}>
            <Switch>
                <Route exact path='/' component={Camera}/>
                <Route path='/report/:twin/:user' component={Report}/>
                <Route path='/error' component={ServerError}/>
                <Route path='/' component={PageNotFound}/>
            </Switch>
        </Router>
    ), document.getElementById('root')
);
