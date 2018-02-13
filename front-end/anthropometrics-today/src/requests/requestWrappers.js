import { createBrowserHistory } from 'history';
import makeRequest from './makeRequest';
import config from '../utility/config';

const history = createBrowserHistory();

const handleError = (error) => {
    console.log('Request failed with error:\n' + error);
    history.push('/error');
};

const getHistoricData =
    (id, callback) => makeRequest(config.baseUrl + config.historicSuffix + '/' + id, callback, handleError);

const analyseImage =
    (callback, body) => makeRequest(config.baseUrl + config.analysisSuffix, callback, handleError, body);

export { history, getHistoricData, analyseImage };