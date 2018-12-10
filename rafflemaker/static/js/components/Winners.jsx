import React from "react";
import anime from 'animejs';
import WinnerEntry from "./WinnerEntry";

export default class Winners extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            contestants: [],
            winners: []
        };

        this._restURL = window.location.origin + '/rafflemaker/rest/raffle/';
        this._baseURL = window.location.origin + '/rafflemaker/raffle/';

        this.onDrawWinnersClicked = this.onDrawWinnersClicked.bind(this);
        this.onRedrawClicked = this.onRedrawClicked.bind(this);
    }

    componentDidMount() {
        window.fetch(this._restURL + this.props.raffleid + '/contestants').then(res => res.json()).then((result) =>
            this.setState({
                contestants: result
            })
        );
    }

    componentDidUpdate() {
        if (this.state.winners.length > 0) {
            this._drawWinners(this.state.winners);
        }
    }

    getAllContestants() {
        let contestantList = [];

        this.state.contestants.map((contestant) => contestantList.push(<WinnerEntry key={contestant['contestantid']} id={contestant['contestantid']} name={contestant['name']} />));

        return contestantList;
    }

    onDrawWinnersClicked() {
        if (this.state.winners.length > 0) {
            document.location.reload();
            return;
        }

        document.querySelector('#draw_winner_btn').textContent = 'New Drawing';
        document.querySelector('#redraw_btn').style.display = 'none';

        window.fetch(this._restURL + this.props.raffleid + '/winners').then(res => res.json()).then((result) =>
            this.setState({
                winners: result
            })
        );
    }

    _drawWinners(winners) {
        this.state.contestants.map((contestant) => {
            let isWinner = false;

            winners.map((winner) => {
                if (winner.id == contestant.contestantid) {
                    isWinner = true;
                }
            });

            if (!isWinner) {
                let el = document.querySelector('.winner-entry[data-id="' + contestant.contestantid + '"]');
                let animation = anime({
                    targets: el,
                    scale: .1,
                    duration: 500,
                    easing: 'easeOutQuad',
                    delay: 500 + Math.floor(Math.random() * 1000)
                });
                animation.complete = () => el.style.display = 'none';
            }
        });
    }

    onRedrawClicked() {
        if (this.state.winners.length > 0) {
            document.location.reload();
            return;
        }

        document.querySelector('#draw_winner_btn').textContent = 'New Drawing';
        document.querySelector('#redraw_btn').style.display = 'none';

        window.fetch(this._restURL + this.props.raffleid + '/last-winners').then(res => res.json()).then((result) =>
            this.setState({
                winners: result
            })
        )
    }

    render() {
        return <div className="winners-block">
            <div id="winner_controls">
                <button onClick={this.onDrawWinnersClicked} id="draw_winner_btn">Draw Winners</button>
                <button onClick={this.onRedrawClicked} id="redraw_btn">Replay Last Drawing</button>
            </div>
            <div id="drawing_container">
                    {this.getAllContestants()}
            </div>
        </div>
    }
}
