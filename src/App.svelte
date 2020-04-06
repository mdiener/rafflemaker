<script>
  import Raffle from './Raffle.svelte'
</script>

<main>
  <h1>Rafflemaker</h1>
  <Raffle />
</main>

<footer>
  <p>&copy; 2020 <a href="https://www.twitter.com/_WebD">@_WebD</a> under <a href="https://github.com/mdiener/rafflemaker/blob/master/LICENSE">MIT License</a></p>
</footer>

<style>
  main {
    margin-top: 10px;
    width: 100%;
    max-width: 700px;
    display: block;
    overflow-y: auto;
    overflow-x: auto;
    height: calc(100% - 30px);
  }

  h1 {
    color: var(--color-primary);
    text-transform: uppercase;
    font-size: 2em;
    text-align: center;
    font-weight: bold;
  }

  footer {
    margin-top: 10px;
    width: 100%;
    text-align: center;
    font-size: 0.7rem;
  }

  footer p {
    padding: 0px;
    margin: 0px;
  }
</style>
