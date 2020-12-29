<script>
	import Case from "./Game/Case.svelte";
	import Grid from "./Game/Grid.svelte";

	let size = { width: 16, height: 16 };
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
	<Grid {...size} />
</main>
