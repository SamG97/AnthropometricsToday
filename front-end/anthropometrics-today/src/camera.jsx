import React from 'react';
import Webcam from 'react-webcam';
import { history, analyseImage } from './requests/requestWrappers';

export default class Camera extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            analysing: false,
            screenshot: null
        };
    }

    setRef = (webcam) => {
        this.webcam = webcam;
    }

    capture = () => {
        const image = this.webcam.getScreenshot();
        this.setState({
            analysing: true,
            screenshot: image 
        });

        analyseImage(this.requestCompleted, this.state.screenshot);
    }

    requestCompleted = () => {
        this.setState({
            isLoading: false,
        });
    }

    render() {
        return (
            <div>
                <h1>CAMERA</h1>
                <Webcam
                    audio={false}
                    width = '320'
                    height = '240'
                    ref={node => this.webcam = node}
                />
                <h2>YOUR SCREENSHOT</h2>
                <div className='screenshot'>
                    <div className='capture'>
                        <button onClick={this.capture}>capture</button>
                    </div>
                    {this.state.screenshot ? <img src={this.state.screenshot} /> : null}
                </div>
            </div>
        );
    }
}