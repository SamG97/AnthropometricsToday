import React from 'react';

const ReportComponent = (props) => {
    return (
        <div className="row">
            <div className="field-name col-6">
                <div className="field-text">
                    {props.fieldName}
                </div>
                <div className="filler" />
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

export default ReportComponent;
