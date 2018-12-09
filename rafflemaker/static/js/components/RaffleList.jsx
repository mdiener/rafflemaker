import React from "react";
import RaffleListEntry from "./RaffleListEntry";

export default class RaffleList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            raffles: []
        };

        this.onRaffleClicked = this.onRaffleClicked.bind(this);
        this.onRemoveClicked = this.onRemoveClicked.bind(this);
    }

    componentDidMount() {
        this.loadRaffles();
    }

    loadRaffles() {
        window.fetch(window.location.origin + '/rest/raffles').then(res => res.json()).then((result) =>
            this.setState({
                raffles: result
            })
        );
    }

    onRaffleClicked(id) {
        window.location = window.location.origin + '/raffle/' + id
    }

    onRemoveClicked(id) {
        self = this;

        window.fetch(window.location.origin + '/rest/raffle/' + id, {
            method: 'DELETE'
        }).then(function(response) {
            if (!response.ok) {
                addMessage('Could not remove the raffle. Please try again.');
            } else {
                self.loadRaffles();
            }
        });
    }

    getRaffles() {
        let raffleElements = [];

        for (var i = 0; i < this.state.raffles.length; i++) {
            var raffle = this.state.raffles[i];
            raffleElements.push(<RaffleListEntry
                key={raffle['raffleid']}
                raffleid={raffle['raffleid']}
                onRaffleClicked={this.onRaffleClicked}
                onRemoveClicked={this.onRemoveClicked}
                name={raffle['name']}
                description={raffle['description']}
                max_winners={raffle['max_winners']}
            />)
        }

        return raffleElements;
    }

    render() {
        return <div className="raffles-list">
            <table>
                <thead>
                    <tr>
                        <th className="name">Name</th>
                        <th className="description">Description</th>
                        <th className="max-winners">Max Winners</th>
                    </tr>
                </thead>
                <tbody>
                    {this.getRaffles()}
                </tbody>
            </table>
        </div>
    }
}
