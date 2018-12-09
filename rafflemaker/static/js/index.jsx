import React from 'react';
import ReactDOM from 'react-dom';
import RaffleList from './components/RaffleList';
import Raffle from './components/Raffle';
import Winners from './components/Winners';

let raffleListEl = document.getElementById('raffle_list')
let raffleEl = document.getElementById('raffle')
let winnerEl =  document.getElementById('winners')

if (raffleListEl != null) {
    ReactDOM.render(<RaffleList />, raffleListEl);
}

if (raffleEl != null) {
    let raffleid = window.location.pathname.match('raffle/([0-9]*)')[1]
    ReactDOM.render(<Raffle raffleid={raffleid} />, raffleEl)
}

if (winnerEl != null) {
    let raffleid = window.location.pathname.match('raffle/([0-9]*)')[1]
    ReactDOM.render(<Winners raffleid={raffleid} />, winnerEl)
}
