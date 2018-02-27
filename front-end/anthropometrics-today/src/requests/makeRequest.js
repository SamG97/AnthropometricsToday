import 'whatwg-fetch';

const makeRequest = (url, callback, errCallback, body) => {
    let promise;
    if (!body) {
        promise = fetch(url);
    } else {
        promise = fetch(url, {
            method: 'post',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'multipart/form-data',
                'Access-Control-Allow-Origin': '*',
            },
            body: body,
        });
    }
    promise.then((response) => {
        if (response.status !== 200) {
            errCallback('Error Code: ' + response.status);
            return;
        }

        response.json().then((data) => callback(data));
    }).catch((error) => errCallback(error));
};

export default makeRequest;
