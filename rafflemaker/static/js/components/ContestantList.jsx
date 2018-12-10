import React from "react";
import ContestantListEntry from "./ContestantListEntry"
import addMessage from "./MessageWindow"

export default class ContestantList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            contestants: []
        }

        this._restURL = window.location.origin + '/rafflemaker/rest/raffle/';
        this._baseURL = window.location.origin + '/rafflemaker/raffle/';

        this.onContestantUpdate = this.onContestantUpdate.bind(this);
        this.onRemoveClicked = this.onRemoveClicked.bind(this);
        this.onAddClicked = this.onAddClicked.bind(this);

        this.name = React.createRef()
        this.tickets = React.createRef()
    }

    componentDidMount() {
        this.loadContestants();
    }

    componentDidUpdate() {
        this.name.current.value = ''
        this.tickets.current.value = ''
    }

    onContestantUpdate(contestantid, values) {
        window.fetch(this._restURL + this.props.raffleid + '/contestant/' + contestantid, {
            method: 'POST',
            body: JSON.stringify({
                'name': values['name'],
                'tickets': values['tickets']
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(red => res.json()).then(response => this.loadContestants());
    }

    onRemoveClicked(contestantid) {
        let self = this;

        window.fetch(this._restURL + this.props.raffleid + '/contestant/' + contestantid, {
            method: 'DELETE'
        }).then(function(response) {
            if (!response.ok) {
                addMessage('Could not remove the contestant. Please try again.')
            } else {
                self.loadContestants()
            }
        });
    }

    getContestants() {
        let contestantElements = [];

        for (var i = 0; i < this.state.contestants.length; i++) {
            var contestant = this.state.contestants[i];
            contestantElements.push(<ContestantListEntry
                key={contestant['contestantid']}
                contestantId={contestant['contestantid']}
                name={contestant['name']}
                tickets={contestant['tickets']}
                onContestantUpdate={this.onContestantUpdate}
                onRemoveClicked={this.onRemoveClicked}
            />)
        }

        return contestantElements;
    }

    loadContestants() {
        window.fetch(this._restURL + this.props.raffleid + '/contestants').then(res => res.json()).then((result) =>
            this.setState({
                contestants: result
            })
        )
    }

    onAddClicked() {
        let self = this;
        let name = document.getElementById('contestant_name_input').value;
        let tickets = Number(document.getElementById('contestant_tickets_input').value);

        let promise = window.fetch(this._restURL + this.props.raffleid + '/contestant', {
            method: 'POST',
            body: JSON.stringify({
                'name': name,
                'tickets': tickets
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        promise.then(function (response) {
            if (!response.ok) {
                addMessage('Could not add the contestant. Please make sure name and tickets are set.');
            } else {
                self.loadContestants();
            }
        });
    }

    render() {
        return <div className="contestants">
            <div className="contestants-list">
                <div className="new-contestant">
                    <input type="text" name="name" id="contestant_name_input" ref={this.name} class="contestant-name" />
                    <input type="number" name="tickets" id="contestant_tickets_input" ref={this.tickets} class="contestant-tickets"/>
                    <button onClick={this.onAddClicked} type="submit" id="contestant_add_button">Add</button>
                </div>
                {this.getContestants()}
            </div>
        </div>
    }
}
