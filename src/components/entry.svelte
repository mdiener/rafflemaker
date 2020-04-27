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
  font-size: var(--font-regular);
  outline: none;
  border: 1px solid var(--color-primary);
}

button {
  width: 30px;
  background-color: var(--color-red);
  color: var(--color-white);
  border-color: var(--color-red);
  padding: 10px 5px 10px 5px;
}

input.input-name {
  width: calc(100% - 20% - 30px - 20px);
}
input.input-tickets {
  width: 20%;
}
</style>
