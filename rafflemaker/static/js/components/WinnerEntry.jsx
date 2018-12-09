import React from "react";

export default class WinnerEntry extends React.Component {
    render() {
        return <div className="winner-entry" data-id={this.props.id}><span>{this.props.name}</span></div>
    }
}
