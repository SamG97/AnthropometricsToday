import React from 'react';
import makeRequest from './makeRequest';

export default class Report extends React.Component {
    constructor(props) {
        super(props);
        const { user, twin } = props.match.params;
        this.state = {
            isLoading: true,
            response: null,
            twin: twin,
            user: user,
        }
    }

    requestCompleted = (data) => {
        this.setState({
            isLoading: false,
            response: data,
        })
    };

    componentDidMount() {
        makeRequest(this.requestCompleted)
    }

    render() {
        if (this.state.isLoading) {
            return (
                <div>
                    Loading...
                </div>
            );
        }

        return (
            // TODO: Replace with actual report implementation
            <div>
                This is a report for user {this.state.user} who matched {this.state.twin}.
                The request result is {this.state.response.id}.
            </div>
        );
    };
}
