<script>
	import Grid from "./Game/Grid.svelte";
	import api from "./api.js";

	let width = 30;
	let height = 16;
	let game = api.new_game(width, height);

	$ : {
		width,
		height,
		game = api.new_game(width, height);
	}
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

	input {
		width : 75px;
	}
</style>

<main>
	<h1>Minesweeper</h1>
	<input type=number bind:value={width} min=3 max=30>
	<input type=number bind:value={height} min=3 max=30>
	<hr>
	{#await game}
		<p>Downloading the game...</p>
	{:then current_game}
		<Grid game={current_game} />
	{:catch error}
		<p>Error : Unable to get the game :/</p>
	{/await}
</main>
