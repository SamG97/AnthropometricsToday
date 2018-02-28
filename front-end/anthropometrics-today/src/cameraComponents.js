import React from 'react';

const CameraHeader = () => {
    return (
        <div>
            <h2>Anthropometrics Today</h2>
            <p className="text-muted">Take two pictures respectively of your front and side and get to know your historical twin.</p>
        </div>
    );
};

const FrontPictureHeader = () => {
    return (
        <div>
            <h2>Anthropometrics Today</h2>
            <p className="text-muted">Take a picture from the front.</p>
        </div>
    );
};

const SidePictureHeader = () => {
    return (
        <div>
            <h2>Anthropometrics Today</h2>
            <p className="text-muted">Take a picture from the side.</p>
        </div>
    );
};

export { CameraHeader, FrontPictureHeader, SidePictureHeader }