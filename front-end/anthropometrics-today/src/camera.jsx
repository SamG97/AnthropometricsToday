import React from 'react';
import Webcam from 'react-webcam';
import { analyseImage } from './requests/requestWrappers';

export default class Camera extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            freeze1: false,
            freeze2: false,
            retake1: false,
            retake2: false,
            photo1: null,
            photo2: null,
            analysing: false,
        };
    }

    setRef = (webcam) => {
        this.webcam = webcam;
    }

    capture1 = () => {
        const image = this.webcam.getScreenshot();
        this.setState({
            freeze1: true,
            freeze2: false,
            retake1: false,
            retake2: false,
            photo1: image,
            analysing: false,
        });
    }

    capture2 = () => {
        const image = this.webcam.getScreenshot();
        this.setState({
            freeze1: false,
            freeze2: true,
            retake1: false,
            retake2: false,
            photo2: image,
            analysing: false,
        });
    }

    clear1 = () => {
        this.setState({
            freeze1: false,
            freeze2: false,
            retake1: true,
            retake2: false,
            photo1: null,
            analysing: false,
        });
    }

    clear2 = () => {
        this.setState({
            freeze1: false,
            freeze2: false,
            retake1: false,
            retake2: true,
            photo2: null,
            analysing: false,
        });
    }

    analyse = () => {
        this.setState({
            analysing: true,
        });

        analyseImage(this.requestCompleted, this.state.photo1);
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

        if (this.state.freeze1) {
            return (
                <div>{this.state.photo1 ? <img src={this.state.photo1} /> : null}
                    <div className='screenshot'>
                        <div class="container text-center">
                            <button onClick={this.clear1} class="btn btn-xl btn-light mr-4">
                                Retake
                            </button>
                            <button onClick={this.clear2} class="btn btn-xl btn-dark">Next Step</button>
                        </div>
                    </div>
                </div>

            );
        }

        if (this.state.freeze2) {
            return (
                <div>{this.state.photo2 ? <img src={this.state.photo2} /> : null}
                    <div className='screenshot'>
                        <div class="container text-center">
                            <button onClick={this.clear2} class="btn btn-xl btn-light mr-4">
                                Retake
                            </button>
                            <button onClick={this.analyse} class="btn btn-xl btn-dark">Get Result</button>
                        </div>
                    </div>
                </div>

            );
        }

        if (this.state.retake1) {
            return (
                <div className="masthead d-flex">
                    <div className="container text-center my-auto">
                        <Webcam
                            audio={false}
                            ref={node => this.webcam = node}
                        />
                    </div>

                    <div className='screenshot'>
                        <div class="container text-center">
                            <button onClick={this.capture1} class="btn btn-xl btn-light mr-4">
                                Capture
                            </button>
                        </div>
                    </div>
                </div>
            );
        }

        if (this.state.retake2) {
            return (
                <div className="masthead d-flex">
                    <div className="container text-center my-auto">
                        <Webcam
                            audio={false}
                            ref={node => this.webcam = node}
                        />
                    </div>

                    <div className='screenshot'>
                        <div class="container text-center">
                            <button onClick={this.capture2} class="btn btn-xl btn-light mr-4">
                                Capture
                            </button>
                        </div>
                    </div>
                </div>
            );
        }

        return (
            <div className="masthead d-flex">
                <div className="container text-center my-auto">
                    <Webcam
                        audio={false}
                        ref={node => this.webcam = node}
                    />

                    <div className='screenshot'>
                        <div class="container text-center">
                            <button onClick={this.capture1} class="btn btn-xl btn-light mr-4">
                                Capture
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}