import React from 'react';
import Webcam from 'react-webcam';
import { analyseImage } from './requests/requestWrappers';

export default class Camera extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            freeze: false,
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
            freeze: true,
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

        if (this.state.freeze) {
            return (
                <div>{this.state.screenshot ? <img src={this.state.screenshot} /> : null}
                    <div className='screenshot'>
                        <div class="container text-center">
                            <button onClick={this.capture} className='capture' class="btn btn-xl btn-light mr-4">Capture</button>
                            <button onClick={this.analyse} class="btn btn-xl btn-dark">Get Result</button>
                        </div>
                    </div>
                </div>

            );
        }

        return (
            <div>
                <Webcam
                    audio={false}
                    ref={node => this.webcam = node}
                />

                <div className='screenshot'>
                    <div class="container text-center">
                        <button onClick={this.capture} className='capture' class="btn btn-xl btn-light mr-4">Capture</button>
                        <button onClick={this.analyse} class="btn btn-xl btn-dark">Get Result</button>
                    </div>
                </div>
            </div>
        );
    }
}