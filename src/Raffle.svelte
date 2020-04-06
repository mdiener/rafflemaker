<script>
  import { onMount } from 'svelte';
  import { tweened } from 'svelte/motion'
  import { cubicOut } from 'svelte/easing'
  import { fade } from 'svelte/transition'
  import Dialog from './Dialog.svelte'
  import Entries from './Entries.svelte'
  import { entries, drawingStarted, drawingEnded } from './store.js'

  let winner = ''

  const drawing = tweened(0, {
    duration: 3000,
    easing: cubicOut
  })

  function onNewEntryClicked() {
    entries.set([...$entries, {}])
  }

  function draw() {
    drawingStarted.set(true)
    drawingEnded.set(false)

    drawing.set(0, {
      duration: 0
    })

    let tickets = []
    $entries.forEach((entry) => {
      const entriesPerName = new Array(entry.tickets).fill(entry.name)
      tickets.push(...entriesPerName)
    });

    for (let i = tickets.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [tickets[i], tickets[j]] = [tickets[i], tickets[j]]
    }

    winner = tickets[Math.floor(Math.random() * tickets.length)]
    drawing.set(100).then(() => {
      drawingEnded.set(true)
      drawingStarted.set(false)
    })
  }
</script>

<div class="raffle">
  <div class="controls">
    <button on:click={draw} disabled={$entries.length < 1}>Draw Winner</button>
    <button on:click={onNewEntryClicked}>New Entry</button>
  </div>

  <Entries />

  <Dialog fullwidth={true} bind:visible={$drawingStarted}>
    <span slot="header">Drawing ...</span>
    <span slot="body">
      <progress value={$drawing} max=100></progress>
    </span>
  </Dialog>

  <Dialog bind:visible={$drawingEnded}>
    <span slot="header">And the Winner is</span>
    <span slot="body"><span class="winner">{winner}</span></span>
  </Dialog>
</div>

<style>
  progress {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border: none;

    background-color: var(--color-primary);
    width: 100%;
    display: block;
    border-radius: 5px;
    color: var(--color-secondary);
  }

  progress::-moz-progress-bar {
    background-color: var(--color-secondary);
    border-radius: 5px;
  }

  progress::-webkit-progress-bar {
    background-color: var(--color-primary);
    border-radius: 5px;
  }
  progress::-webkit-progress-value {
    background-color: var(--color-secondary);
    border-radius: 5px;
  }

  .controls {
    display: flex;
    width: 100%;
    justify-content: space-between;
    margin-bottom: 10px;
  }

  .winner {
    font-weight: bold;
    font-size: 2rem;
    color: var(--color-primary);
  }
</style>
