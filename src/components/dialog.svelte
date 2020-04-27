<script>
  import { tweened } from 'svelte/motion'
  import { fade } from 'svelte/transition';

  export let visible = true
  export let fullwidth = false

  function closeDialog() {
    visible = false
  }

  function getClass() {
    if (fullwidth) return 'dialog fullwidth'
    return 'dialog'
  }
</script>

{#if visible}
<div in:fade out:fade class={getClass()}>
  <div on:click={closeDialog} class="background"></div>
  <div class="wrapper">
    <div class="header">
      <slot name="header"></slot>
    </div>
    <div class="body">
      <slot name="body"></slot>
    </div>
  </div>
</div>
{/if}

<style>
.dialog {
  position: absolute;
  top: 0px;
  left: 0px;
  height: 100%;
  width: 100%;
  z-index: 1000;
  display: flex;
  justify-content: center;
}

.background {
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: 1001;
  background-color: rgba(0, 0, 0, 0.1);
}

.wrapper {
  align-self: center;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  padding: 10px;
  border: 1px solid var(--color-secondary);
  border-radius: 5px;
  background-color: var(--color-primary-light);
  z-index: 1002;
}

.header {
  font-weight: bold;
  font-size: 1.3rem;
}

.body {
  margin-top: 5px;
}

.dialog.fullwidth .wrapper {
  width: 90%;
}
</style>
