import React from 'react';
import './reportComponent.css';

const ReportComponent = (props) => {
    return (
        <div className='container'>
            <div className='field-name'>
                {props.fieldName}
            </div>
            <div className='value'>
                {props.userValue}
            </div>
            <div className='value'>
                {props.twinValue}
            </div>
        </div>
    );
};

export default ReportComponent;