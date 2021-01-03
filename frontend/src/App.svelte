<script>
	import Grid from "./Game/Grid.svelte";
	import api from "./api.js";

	let game = api.new_game(3, 3);
</script>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<main>
	<h1>Minesweeper</h1>
	{#await game}
		<p>Downloading the game...</p>
	{:then current_game}
		<Grid game={current_game} />
	{:catch error}
		<p>Error : Unable to get the game :/</p>
	{/await}
</main>
