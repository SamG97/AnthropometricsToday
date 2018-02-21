import React from 'react';
import QRCode from 'qrcode.react';
import { map } from 'lodash';
import capitalise from '../utility/capitalise';
import config from '../utility/config';
import Spinner from '../utility/loading';
import { ComparisonReportComponent, TwinReportComponent } from './reportComponents';
import { MalformedMeasurements, ServerError } from '../errors';
import { getHistoricData } from '../requests/requestWrappers';
import { uncompress } from '../utility/urlCompress';
import '../../node_modules/bootstrap/dist/css/bootstrap.css';
import './report.css';

export default class Report extends React.Component {
    constructor(props) {
        super(props);
        const { user, twin } = props.match.params;
        const details = uncompress(user);
        this.twin = twin;

        if (details && details.length === config.fieldOrdering.length) {
            const userMeasurements = {};
            for (let i = 0; i < config.fieldOrdering.length; i++) {
                userMeasurements[config.fieldOrdering[i]] = details[i];
            }
            this.userMeasurements = userMeasurements;
        } else {
            this.userMeasurements = null;
        }

        this.state = {
            isLoading: true,
            loadFailed: false,
            twinMeasurements: null,
        }
    }

    requestCompleted = (data) => {
        this.setState({
            isLoading: false,
            twinMeasurements: data,
        })
    };

    requestFailed = (err) => {
        console.log('Request failed with error:\n' + err);
        this.setState({
            isLoading: false,
            loadFailed: true,
        })
    };

    generateTwinComponents = (field) => {
        if (field === 'dob') {
            const dob = this.state.twinMeasurements['dobd'] + '/' + this.state.twinMeasurements['dobm'] + '/' +
                this.state.twinMeasurements['doby'];
            return (
                <TwinReportComponent
                    key={field}
                    fieldName={'Date of Birth'}
                    userValue={this.userMeasurements[field]}
                    twinValue={dob}
                />
            );
        }

        const fieldName = (field === 'hair' || field === 'eye') ? (field + ' colour') : field;

        return (
            <TwinReportComponent
                key={field}
                fieldName={capitalise(fieldName)}
                userValue={this.userMeasurements[field]}
                twinValue={this.state.twinMeasurements[field]}
            />
        );
    };

    generateComparisonComponent = (field) => {
        const isMeasurement = field !== 'name';
        const fieldName = isMeasurement ? (field + ' width') : field;

        return (
            <ComparisonReportComponent
                key={field}
                fieldName={capitalise(fieldName)}
                userValue={this.userMeasurements[field] + (isMeasurement ? ' cm' : '')}
                twinValue={this.state.twinMeasurements[field] + (isMeasurement ? ' cm' : '')}
            />
        );
    };

    componentDidMount() {
        getHistoricData(this.twin, this.requestCompleted, this.requestFailed)
    }

    render() {
        if (this.state.isLoading) {
            return (
                <div className="loading-container">
                    <Spinner/>
                </div>
            );
        }

        if (this.state.loadFailed) {
            return (
                <ServerError/>
            );
        }

        if (!this.userMeasurements) {
            return (
                <MalformedMeasurements/>
            );
        }

        const linkAddress = config.webBaseUrl + '/report/' + this.props.match.params.twin + '/' +
            this.props.match.params.user;

        const twinBody = (<div>{map(config.twinOrdering, (field) => this.generateTwinComponents(field))}</div>);

        const reportBody = (<div>{map(config.fieldOrdering, (field) => this.generateComparisonComponent(field))}</div>);

        return (
            <div className="outer-container">
                <div className="container">
                    <div className="row">
                        <div className="col-6">
                            <div className="number-container">
                                <div className="number-label">
                                    No.
                                </div>
                                <div className="report-number">
                                    {Math.floor(Math.random() * 9000 + 1000)}
                                </div>
                            </div>
                        </div>
                        <div className="col-6">
                            <QRCode className="qr-code" value={linkAddress} bgColor="#CAC3BB"/>
                        </div>
                    </div>
                    <div className="row">
                        <div className="intro col-12">
                            Your historical twin is {this.twin['name']}! <br/>
                            Find out more about them and how you compare in your report below!
                        </div>
                    </div>
                    <div className="row">
                        <div className="title col-12">
                            ANTHROPOMETRICS TODAY
                        </div>
                    </div>
                    {twinBody}
                    <div className="row">
                        <div className="divider"/>
                    </div>
                    {reportBody}
                    <div className="row">
                        <div className="divider"/>
                    </div>
                </div>
            </div>
        );
    };
}
