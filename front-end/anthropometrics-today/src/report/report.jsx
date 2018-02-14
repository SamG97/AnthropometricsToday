import React from 'react';
import ReportComponent from './reportComponent';
import { map } from 'lodash';
import config from '../utility/config';
import capitalise from '../utility/capitalise';
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

        console.log(this.userMeasurements);

        this.state = {
            isLoading: true,
            twinMeasurements: null,
        }
    }

    requestCompleted = (data) => {
        this.setState({
            isLoading: false,
            twinMeasurements: data,
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
        getHistoricData(this.twin, this.requestCompleted)
    }

    render() {
        if (this.state.isLoading) {
            return (
                <div>
                    Loading...
                </div>
            );
        }

        const reportBody = this.userMeasurements ? (
            <div>{map(config.fieldOrdering, (field) => this.generateFieldComponent(field))}</div>
        ) : null; // TODO: Replace with proper message for wrong URL

        return (
            // TODO: Replace with actual report implementation
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
