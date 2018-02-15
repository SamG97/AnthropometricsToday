import React from 'react';
import './errors.css';

const ErrorTemplate = (props) => {
    return (
        <div className="error-container">
            <div className="error-title">
                Sorry!
            </div>
            <div className="error-body">
                {props.message}
            </div>
        </div>
    );
};

const PageNotFound = (_) => {
    return (
        <ErrorTemplate
            message="We don't know where that page is. Please check that you typed the URL correctly."
        />
    );
};

const ServerError = (_) => {
    return (
        <ErrorTemplate
            message={`We're having problems contacting the server. Please ensure you have a working internet
             connection or try again later.`}
        />
    );
};

const MalformedMeasurements = (_) => {
    return (
        <ErrorTemplate
            message="That URL is not valid. Please ensure that it is correctly formatted and try again."
        />
    );
};

export { MalformedMeasurements, PageNotFound, ServerError };
