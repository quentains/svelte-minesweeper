<script>
	import Grid from "./Game/Grid.svelte";
	import Selector from "./Components/Selector.svelte";
	import api from "./api.js";

	let width = 30;
	let height = 16;
	let difficulty = 1;
	let game = api.new_game(width, height);
	let time = 0;

	$ : {

		if (difficulty == 0) {
			width = 20;
			height = 8;
		}
		else if (difficulty == 1) {
			width = 30;
			height = 16;
		}
		else {
			width = 50;
			height = 25;
		}

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
		height: 142px;
	}

	#banner img {
		width: 75px;
		display: inline-block;
		position: relative;
		top: 6px;
	}

	p {
		color: #E5D9F2;
		font-weight: bold;
		font-size: 30px;
		margin-top: 10px;
		margin-bottom: 30px;
	}

	#restart {
		width: 50px;
		position: relative;
		top: 12px;
		left: 10px;
	}


</style>

<main>
	<div class="container" id="banner">
		<h1>Minesweeper</h1>
		<img alt="Bomb icon" src="img/bomb_white.png"/>
	</div>
	<Selector bind:selected={difficulty}/>
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
