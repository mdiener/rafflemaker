<script>
  import Entry from '../components/entry.svelte'
  import { entries } from '../stores/entries.js'

  function removeEntry(event) {
    let myEntries = $entries
    myEntries.splice(event.detail.index, 1)

    entries.set(myEntries)
  }
</script>

<div class="entries">
  <ul>
    {#each $entries as entry, idx}
      <Entry on:remove={removeEntry} bind:name={entry.name} bind:tickets={entry.tickets} index={idx} />
    {/each}
  </ul>
</div>

<style>
ul {
  list-style-type: none;
  padding: 0px;
  margin: 0px;
}
</style>
