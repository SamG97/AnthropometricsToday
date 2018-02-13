import React from 'react';
import Webcam from 'react-webcam';
import { analyseImage } from './requests/requestWrappers';

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
            screenshot: image,
        });
    }

    analyse = () => {
        this.setState({
            analysing: true,
        });
        analyseImage(this.requestCompleted, this.state.screenshot);
    }

    requestCompleted = () => {
        this.setState({
            analysing: false,
        });
    }

    render() {
        if (this.state.analysing) {
            return (
                <h1>
                    Analysing Photo.
                </h1>
            );
        }

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
                    <div className='analyse'>
                        <button onClick={this.analyse}>get result</button>
                    </div>
                </div>
            </div>
        );
    }
}