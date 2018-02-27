import React from 'react';
import Webcam from 'react-webcam';
import { history, analyseImage } from './requests/requestWrappers';
import { compress } from './utility/urlCompress';

export default class Camera extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            nameError: false,
            freeze1: false,
            freeze2: false,
            retake1: false,
            retake2: false,
            photo1: null,
            photo2: null,
            analysing: false,
            analyseFailed: false,
        };

        this.handleChange = this.handleChange.bind(this);
    }

    setRef = (webcam) => {
        this.webcam = webcam;
    }

    handleChange(event) {
        this.setState({
            username: event.target.value,
        });
    }

    capture1 = () => {
        const image = this.webcam.getScreenshot();

        console.log('Username submitted: ' + this.state.username);
        if (this.state.username.length > 50) {
            this.setState({
                username: '',
                nameError: true,
            });
        }

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
            });

        data.append('user_photo2', {
            uri: this.state.photo2,
            name: 'user_photo2.jpg',
            type: 'image/jpg'
        }
        );

        analyseImage(this.requestCompleted, data);
    }

    requestCompleted = (response) => {
        history.push('/report/' + response.id + "/" + compress(this.state.username, [response.Face_breadth, response.Face_iobreadth, response.Head_length]));
    }

    render() {
        if (this.state.analysing) {
            return (
                <div className="container text-center">
                    <h1>Analysing Photo!</h1>
                </div>
            );
        }

        if (this.state.freeze1) {
            return (
                <section className="features" id="features">
                    <div className="container">
                        <div className="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p className="text-muted">Take a picture from the front.</p>

                            {this.state.photo1 ? <img src={this.state.photo1} alt="from the front" /> : null}
                            <p className="text-muted">This is your picture from the front.</p>

                            <div className="container text-center">
                                <button onClick={this.clear1} className="btn btn-xl btn-light mr-4">
                                    Retake
                                </button>

                                <button onClick={this.clear2} className="btn btn-xl btn-dark">
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
                <section className="features" id="features">
                    <div className="container">
                        <div className="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p className="text-muted">Take a picture from the side.</p>

                            {this.state.photo2 ? <img alt="from the front" src={this.state.photo2} /> : null}
                            <p className="text-muted">This is your picture from the side.</p>

                            <div className="container text-center">
                                <button onClick={this.clear2} className="btn btn-xl btn-light mr-4">
                                    Retake
                            </button>

                                <button onClick={this.analyse} className="btn btn-xl btn-dark">
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
                <section className="features" id="features">
                    <div className="container">
                        <div className="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p className="text-muted">Take a picture from the front.</p>

                            <Webcam
                                audio={false}
                                ref={node => this.webcam = node}
                                screenshotFormat="image/jpeg"
                            />

                            <div className="container text-center">
                                <button onClick={this.capture1} className="btn btn-xl btn-light mr-4">
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
                <section className="features" id="features">
                    <div className="container">
                        <div className="section-heading text-center">
                            <h2>Anthropometrics Today</h2>
                            <p className="text-muted">Take a picture from the side.</p>

                            <Webcam
                                audio={false}
                                ref={node => this.webcam = node}
                                screenshotFormat="image/jpeg"
                            />

                            <div className="container text-center">
                                <button onClick={this.capture2} className="btn btn-xl btn-light mr-4">
                                    Capture
                                </button>
                            </div>
                        </div>
                    </div>
                </section>
            );
        }

        return (
            <section className="features" id="features">
                <div className="container">
                    <div className="section-heading text-center">
                        <h2>Anthropometrics Today</h2>
                        <p className="text-muted">Take two pictures respectively of your front and side and get to know your historical twin.</p>

                        <Webcam
                            audio={false}
                            ref={node => this.webcam = node}
                            screenshotFormat="image/jpeg"
                        />

                        <div className="col-md-10 col-lg-8 col-xl-7 mx-auto">
                            <form noValidate className={this.state.nameError ? 'nameError' : ''}>
                                <div className="form-row">
                                    <div className="col-12 col-md-9 mb-2 mb-md-0">
                                        <input className="form-control form-control-lg" placeholder="Enter your name here..." type="text" name="usernmae" id="username" value={this.state.username} onChange={this.handleChange} required />
                                    </div>
                                    <div className="col-12 col-md-3">
                                        <button onClick={this.capture1} className="btn btn-block btn-lg btn-primary">
                                            Start!
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