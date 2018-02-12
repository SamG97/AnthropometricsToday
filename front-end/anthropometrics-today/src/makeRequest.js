import 'whatwg-fetch';
import config from './config';

const makeRequest = (callback, body) => {
    let promise;
    if (!body) {
        promise = fetch(config.baseUrl + config.getSuffix);
    } else {
        promise = fetch(config.baseUrl + config.postSuffix, {
            method: 'post',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'multipart/form-data',
            },
            body: body,
        });
    }
    promise.then((response) => {
        if (response.status !== 200) {
            console.log('Error contacting server. Error code: ' + response.status);
            return;
        }

        response.json().then((data) => callback(data));
    }).catch((error) => console.log('Request failed with error: ' + error));
};

export default makeRequest;