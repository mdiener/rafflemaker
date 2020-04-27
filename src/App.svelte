<script>
  import Raffle from './components/raffle.svelte'
  import Footer from './components/footer.svelte'
</script>

<main>
  <h1>Rafflemaker</h1>
  <Raffle />
</main>
<Footer />

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

  :global(*) {
    box-sizing: border-box;
  }

  :global(:root) {
    --color-primary: #bcaaa4;
    --color-primary-light: #efdcd5;
    --color-rimary-dark: #8c7b75;
    --color-secondary: #ffd740;
    --color-secondary-light: #ffff74;
    --color-secondary-dark:#c8a600;

    --color-grey-light: #ebebeb;
    --color-grey: #bfbfbf;
    --color-grey-dark: #5c5c5c;
    --color-black: #000;
    --color-white: #fff;
    --color-red: #f00;

    --font-regular: 1rem;
    --font-large: 1.5rem;
    --font-small: 0.8rem;
  }

  :global(html), :global(body) {
    padding: 0px;
    margin: 0px;
    height: 100%;
    width: 100%;
    font-size: 18px;
    overflow: hidden;
    font-family: 'Roboto', sans-serif;
  }

  :global(button) {
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    background-color: var(--color-primary);
    color: var(--color-secondary);
    border-radius: 5px;
    border: 1px solid var(--color-secondary);
    box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.1);
    font-weight: bold;
    cursor: pointer;
  }
  :global(button:active),
  :global(button:hover),
  :global(button) {
    outline: none;
  }

  :global(input) {
    background: var(--color-primary-light);
    border: 1px solid var(--color-primary-dark);
    padding: 10px;
    border-radius: 5px;
  }

  main {
    margin-top: 10px;
    width: 100%;
    max-width: 700px;
    display: block;
    overflow-y: auto;
    overflow-x: auto;
    margin-left: auto;
    margin-right: auto;
    height: calc(100% - 45px);
    background-color: var(--color-primary-light);
    border-radius: 20px;
    padding: 20px;
  }

  h1 {
    color: var(--color-primary);
    text-transform: uppercase;
    font-size: var(--font-large);
    text-align: center;
    font-weight: bold;
  }

  @media only screen and (max-width: 700px) {
    :global(html), :global(body) {
      overflow: auto;
    }

    main {
      margin-top: 0px;
      height: 100%;
      overflow: visible;
      border-radius: 0px;
    }
  }
</style>
