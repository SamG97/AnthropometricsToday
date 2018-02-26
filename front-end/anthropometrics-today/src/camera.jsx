import React from 'react';
import Webcam from 'react-webcam';
import { analyseImage } from './requests/requestWrappers';
import { ServerError } from './errors';

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
            analyseFailed: false,
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
            analyseFailed: false,
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
            analyseFailed: false,
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
            analyseFailed: false,
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
            analyseFailed: false,
        });
    }

    analyse = () => {
        this.setState({
            analysing: true,
            analyseFailed: false,
        });

        var data = new FormData();
        data.append(
            'user_photo1', {
                uri: this.state.photo1,
                name: 'user_photo1.jpg',
                type: 'image/jpg'
            },

            'user_photo2', {
                uri: this.state.photo2,
                name: 'user_photo2.jpg',
                type: 'image/jpg'
            }
        );

        analyseImage(this.requestCompleted, data, this.requestFailed);
    }

    requestCompleted = () => {
        this.setState({
            freeze1: false,
            freeze2: false,
            retake1: false,
            retake2: false,
            photo1: null,
            photo2: null,
            analysing: false,
            analyseFailed: true,
        });
    }

    requestFailed = (err) => {
        console.log('Request failed with error:\n' + err);
        this.setState({
            freeze1: false,
            freeze2: false,
            retake1: false,
            retake2: false,
            photo1: null,
            photo2: null,
            analysing: false,
        })
    };

    render() {
        if (this.state.analysing) {
            return (
                <div class="container text-center">
                    <h1>Analysing Photo!</h1>
                </div>
            );
        }

        if (this.state.analyseFailed) {
            return (
                <ServerError />
            );
        }

        if (this.state.freeze1) {
            return (
                <section class="features" id="features">
                    <div class="container">
                        <div class="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                            {this.state.photo1 ? <img src={this.state.photo1} /> : null}
                            <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                            <div class="container text-center">
                                <button onClick={this.clear1} class="btn btn-xl btn-light mr-4">
                                    Retake
                                </button>

                                <button onClick={this.clear2} class="btn btn-xl btn-dark">
                                    Next Step
                                </button>
                            </div>
                        </div>
                    </div>
                </section>
            );
        }

        if (this.state.freeze2) {
            return (
                <section class="features" id="features">
                    <div class="container">
                        <div class="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                            {this.state.photo2 ? <img src={this.state.photo2} /> : null}
                            <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                            <div class="container text-center">
                                <button onClick={this.clear2} class="btn btn-xl btn-light mr-4">
                                    Retake
                            </button>

                                <button onClick={this.analyse} class="btn btn-xl btn-dark">
                                    Get Result
                            </button>
                            </div>
                        </div>
                    </div>
                </section>
            );
        }

        if (this.state.retake1) {
            return (
                <section class="features" id="features">
                    <div class="container">
                        <div class="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                            <Webcam
                                audio={false}
                                ref={node => this.webcam = node}
                            />

                            <div class="container text-center">
                                <button onClick={this.capture1} class="btn btn-xl btn-light mr-4">
                                    Capture
                                </button>
                            </div>
                        </div>
                    </div>
                </section>
            );
        }

        if (this.state.retake2) {
            return (
                <section class="features" id="features">
                    <div class="container">
                        <div class="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                            <Webcam
                                audio={false}
                                ref={node => this.webcam = node}
                            />

                            <div class="container text-center">
                                <button onClick={this.capture2} class="btn btn-xl btn-light mr-4">
                                    Capture
                                </button>
                            </div>
                        </div>
                    </div>
                </section>
            );
        }

        return (
            <section class="features" id="features">
                <div class="container">
                    <div class="section-heading text-center">
                        <h2>Anthropometrics Today</h2>
                        <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae malesuada odio.</p>

                        <Webcam
                            audio={false}
                            ref={node => this.webcam = node}
                        />

                        <div class="col-md-10 col-lg-8 col-xl-7 mx-auto">
                            <form>
                                <div class="form-row">
                                    <div class="col-12 col-md-9 mb-2 mb-md-0">
                                        <input type="email" class="form-control form-control-lg" placeholder="Enter your name here..." />
                                    </div>
                                    <div class="col-12 col-md-3">
                                        <button onClick={this.capture1} class="btn btn-block btn-lg btn-primary">
                                            Capture!
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>

                    </div>
                </div>
            </section>
        );
    }
}