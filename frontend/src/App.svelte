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

	function restart() {
		game = api.new_game(width, height);
		time = 0;
	}

</script>

<style>
	main {
		background-color: #222;
		text-align: center;
		padding: 1em;
		max-width: 100%;
		margin: 0 auto;
		font-family: "Audio Wide", sans-serif;
		min-height: 100%;
	}

	h1 {
		color: #E5D9F2;
		text-transform: uppercase;
		font-size: 4em;
		display: inline-block;
		margin-right: 5px;
	}

	#banner {
		margin-top: 10px;
	}

	#banner img {
		width: 75px;
		display: inline-block;
		position: relative;
		top: -25px;
	}

	p {
		color: #E5D9F2;
		font-weight: bold;
		font-size: 30px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	#restart {
		width: 50px;
		position: relative;
		top: -4px;
		left: 10px;
	}
</style>

<main>
	<div class="container" id="banner">
		<h1>Minesweeper</h1>
		<img alt="Bomb icon" src="img/bomb_white.png"/>
	</div>
	<p>
		TIME : {time}
		<img on:click={restart} id="restart" alt="restart" src="img/restart.svg" />
	</p>
	{#await game}
		<p>Downloading the game...</p>
	{:then current_game}
		<Grid game={current_game} bind:time={time}/>
	{:catch error}
		<p>Error : Unable to get the game :/</p>
	{/await}
</main>
