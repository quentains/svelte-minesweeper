<script>
	import Grid from "./Game/Grid.svelte";
	import api from "./api.js";

	let width = 30;
	let height = 16;
	let game = api.new_game(width, height);
	let time = 0;

	$ : {
		width,
		height,
		game = api.new_game(width, height);
		time = 0;
	}
</script>

<style>
	main {
		background-color: #222;
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
		font-family: "Comic Sans MS", "Comic Sans", cursive;
		min-height: 100%;
	}

	h1 {
		color: #1ce;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	p {
		color: #1ce;
		font-weight: bold;
		font-size: 30px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	input {
		background-color: #222;
		color: white;
		width : 75px;
		border-radius: 10px;
	}
</style>

<main>
	<h1>Minesweeper</h1>
	<input type=number bind:value={width} min=3 max=30>
	<input type=number bind:value={height} min=3 max=30>
	<hr>
	<p>TIME : {time}</p>
	{#await game}
		<p>Downloading the game...</p>
	{:then current_game}
		<Grid game={current_game} bind:time={time}/>
	{:catch error}
		<p>Error : Unable to get the game :/</p>
	{/await}
</main>
