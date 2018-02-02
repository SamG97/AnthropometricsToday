import React from 'react';

const Report = (props) => {
    let { user, twin } = props.match.params;

    return (
        // TODO: Replace with actual report implementation
        <div>
            This is a report for user {user} who matched {twin}.
        </div>
    );
};

export default Report;