import React from "react";

export default function addMessage(message) {
    let parentEl;
    let messagesEl = document.getElementById('flashed_messages');
    if (messagesEl.children.length < 1) {
        parentEl = document.createElement('ul');
        messagesEl.appendChild(parentEl);
    } else {
        parentEl = messagesEl.children[0];
    }

    let liEl = document.createElement('li');
    liEl.textContent = message;
    parentEl.appendChild(liEl);
}
