import React from "react";

export default class RaffleListEntry extends React.Component {
    constructor(props) {
        super(props);

        this.onRaffleClicked = this.onRaffleClicked.bind(this);
        this.onRemoveClicked = this.onRemoveClicked.bind(this);
    }

    onRaffleClicked() {
        this.props.onRaffleClicked(this.props.raffleid);
    }

    onRemoveClicked() {
        this.props.onRemoveClicked(this.props.raffleid);
    }

    render() {
        return <tr>
            <td className="name" onClick={this.onRaffleClicked}>{this.props.name}</td>
            <td className="description" onClick={this.onRaffleClicked}>{this.props.description}</td>
            <td className="max-winners" onClick={this.onRaffleClicked}>{this.props.max_winners}</td>
            <td className="delete"><button onClick={this.onRemoveClicked}>Remove</button></td>
        </tr>
    }
}
