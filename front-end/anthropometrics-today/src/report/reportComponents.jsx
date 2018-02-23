import React from 'react';

const ComparisonReportComponent = (props) => {
    return (
        <div className="row">
            <div className="field-name col-6">
                <div className="field-text">
                    {props.fieldName}
                </div>
                <div className="filler"/>
            </div>
            <div className="value col-3">
                {props.userValue}
            </div>
            <div className="value col-3">
                {props.twinValue}
            </div>
        </div>
    );
};

const TwinReportComponent = (props) => {
    return (
        <div className="row">
            <div className="field-name col-8">
                <div className="field-text">
                    {props.fieldName}
                </div>
                <div className="filler"/>
            </div>
            <div className="value col-4">
                {props.twinValue}
            </div>
        </div>
    );
};

export { ComparisonReportComponent, TwinReportComponent };
