<script>
  import { createEventDispatcher } from 'svelte'
  import { fade } from 'svelte/transition';

  export let name = ''
  export let tickets = ''
  export let index = -1

  const dispatch = createEventDispatcher()

  function onRemoveClicked() {
    dispatch('remove', {
      index
    })
  }
</script>

<li in:fade out:fade class="entry">
  <input class="input-name" bind:value={name} type="text" placeholder="Name" />
  <input class="input-tickets" bind:value={tickets} type="number" placeholder="Tickets" min=0 />
  <button on:click={onRemoveClicked}>x</button>
</li>

<style>
li {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

input, button {
  display: inline-block;
}

input {
  font-size: 1rem;
  outline: none;
  border: 1px solid var(--color-secondary);
}

button {
  width: 15%;
  background-color: var(--color-red);
  color: var(--color-white);
}

input.input-name {
  width: 50%;
}
input.input-tickets {
  width: 30%;
}
</style>
