import React from "react";

export default class ContestantListEntry extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'name': this.props.name,
            'tickets': this.props.tickets
        }

        this.onNameChanged = this.onNameChanged.bind(this)
        this.onTicketsChanged = this.onTicketsChanged.bind(this)
        this.onRemoveClicked = this.onRemoveClicked.bind(this)
    }

    componentDidUpdate() {
        this.props.onContestantUpdate(this.props.contestantId, {
            'name': this.state.name,
            'tickets': this.state.tickets
        });
    }

    onNameChanged(e) {
        this.setState({
            'name': e.target.value
        });
    }

    onTicketsChanged(e) {
        this.setState({
            'tickets': Number(e.target.value)
        });
    }

    onRemoveClicked() {
        this.props.onRemoveClicked(this.props.contestantId)
    }

    render() {
        return <div className="contestant-list-entry">
            <input className="contestant-name" type="text" onChange={this.onNameChanged} value={this.state.name} />
            <input className="contestant-tickets" type="number" onChange={this.onTicketsChanged} value={this.state.tickets} />
            <button className="contestant-delete" onClick={this.onRemoveClicked}>Remove</button>
        </div>
    }
}
