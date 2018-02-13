import React from 'react';
import Webcam from 'react-webcam';

export default class Camera extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            screenshot: null
        };
    }

    setRef = (webcam) => {
        this.webcam = webcam;
    }

    capture = () => {
        const screenshot = this.webcam.getScreenshot();
        this.setState({ screenshot });
    };

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
                <div className='screenshots'>
                    <div className='controls'>
                        <button onClick={this.capture}>capture</button>
                    </div>
                    {this.state.screenshot ? <img src={this.state.screenshot} /> : null}
                </div>
            </div>
        );
    }
}