import { createBrowserHistory } from 'history';
import makeRequest from './makeRequest';
import config from '../utility/config';

const history = createBrowserHistory();

const defaultHandler = (error) => {
    console.log('Request failed with error:\n' + error);
    history.push('/error');
};

const getHistoricData = (id, callback, fail) =>
        makeRequest(config.baseUrl + config.historicSuffix + '/' + id, callback, fail ? fail : defaultHandler);

const analyseImage = (callback, body, fail) =>
    makeRequest(config.baseUrl + config.analysisSuffix, callback, fail ? fail : defaultHandler, body);

export { history, getHistoricData, analyseImage };
