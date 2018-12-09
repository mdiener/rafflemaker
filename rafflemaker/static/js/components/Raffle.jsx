import React from "react";
import ContestantList from "./ContestantList"
import addMessage from "./MessageWindow"

export default class Raffle extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            name: '',
            description: '',
            max_winners: 1,
        };

        this.onNameChanged = this.onNameChanged.bind(this);
        this.onDescriptionChanged = this.onDescriptionChanged.bind(this);
        this.onMaxWinnersChanged = this.onMaxWinnersChanged.bind(this);
        this.onWinnerClicked = this.onWinnerClicked.bind(this);
    }

    componentDidUpdate() {
        window.fetch(window.location.origin + '/rest/raffle/' + this.props.raffleid, {
            method: 'POST',
            body: JSON.stringify({
                'name': this.state.name,
                'description': this.state.description,
                'max_winners': this.state.max_winners
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function(response) {
            if (!response.ok) {
                addMessage('Could not update the raffle. Please try again later.')
            }
        });
    }

    componentDidMount() {
        window.fetch(window.location.origin + '/rest/raffle/' + this.props.raffleid).then(res => res.json()).then((result) =>
            this.setState({
                name: result['name'],
                description: result['description'],
                max_winners: result['max_winners']
            })
        )
    }

    onNameChanged(e) {
        this.setState({
            name: e.target.value
        });
    }

    onDescriptionChanged(e) {
        this.setState({
            description: e.target.value
        });
    }

    onMaxWinnersChanged(e) {
        this.setState({
            max_winners: Number(e.target.value)
        });
    }

    onWinnerClicked() {
        document.location = document.location.origin + '/raffle/' + this.props.raffleid + '/winners';
    }

    render() {
        let winner_url = document.location.origin + '/raffle/' + this.props.raffleid + '/winners';

        return <div className="raffle">
            <div className="header">
                <input className="raffle-name-input" onChange={this.onNameChanged} value={this.state.name} />
                <textarea className="raffle-description-input" onChange={this.onDescriptionChanged} value={this.state.description} />
                <div>Winners per drawing: <input type="number" className="raffle-max_winners-input" onChange={this.onMaxWinnersChanged} value={this.state.max_winners} min="1" /></div>
            </div>
            <div className="controls">
                <a className="button winner-btn" href={winner_url}>Draw Winner(s)</a>
            </div>
            <ContestantList raffleid={this.props.raffleid} />
        </div>
    }
}
