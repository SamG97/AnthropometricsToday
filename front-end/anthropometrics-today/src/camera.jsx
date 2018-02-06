import React from 'react';
import Webcam from 'react-webcam';

export default class Camera extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            // Initialise state here; if no state is needed convert to functional component like Report
        };
    }

    render() {
        // TODO: Replace with actual camera implementation
        return (
            <div>
                This is a camera
                <p><Webcam/></p>;
            </div>
        );
    }
}