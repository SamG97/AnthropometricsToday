import React from 'react';
import ReportComponent from './reportComponent';
import { map } from 'lodash';
import config from '../utility/config';
import capitalise from '../utility/capitalise';
import { getHistoricData } from '../requests/requestWrappers';
import { uncompress } from '../utility/urlCompress';
import { MalformedMeasurements, ServerError } from '../errors';
import '../../node_modules/bootstrap/dist/css/bootstrap.css';
import './report.css';
import Spinner from '../utility/loading';

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

        console.log(this.userMeasurements);

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

    generateFieldComponent = (field) => {
        return (
            <ReportComponent
                key={field}
                fieldName={capitalise(field)}
                userValue={this.userMeasurements[field]}
                twinValue={this.state.twinMeasurements[field]}
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
                    <Spinner />
                </div>
            );
        }

        if (this.state.loadFailed) {
            return (
                <ServerError />
            );
        }

        if (!this.userMeasurements) {
            return (
                <MalformedMeasurements />
            );
        }

        const reportBody = (<div>{map(config.fieldOrdering, (field) => this.generateFieldComponent(field))}</div>);

        return (
            <div className="container">
                <div className="row">
                    <div className="number-container">
                        <div className="number-label">
                            No.
                        </div>
                        <div className="report-number">
                            {Math.floor(Math.random() * 9000 + 1000)}
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="title col-12">
                        ANTHROPOMETRICS TODAY
                    </div>
                </div>
                {reportBody}
                <div className="row">
                    <div className="footer" />
                </div>
            </div>
        );
    };
}
