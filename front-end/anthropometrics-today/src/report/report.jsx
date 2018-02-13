import React from 'react';
import ReportComponent from './reportComponent';
import { map } from 'lodash';
import config from '../utility/config';
import { getHistoricData } from '../requests/requestWrappers';
import { uncompress } from '../utility/urlCompress';

export default class Report extends React.Component {
    constructor(props) {
        super(props);
        const { user, twin } = props.match.params;
        const details = uncompress(user);
        this.twin = twin;

        if (details && details.measurements.length === config.fieldOrdering.length) {
            const userMeasurements = {};
            for (let i = 0; i < config.fieldOrdering.length; i++) {
                userMeasurements[config.fieldOrdering[i]] = details.measurements[i];
            }
            this.name = details.name;
            this.userMeasurements = userMeasurements;
        } else {
            this.name = null;
            this.userMeasurements = null;
        }

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
                fieldName={field}
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
            <div>
                {reportBody}
            </div>
        );
    };
}
