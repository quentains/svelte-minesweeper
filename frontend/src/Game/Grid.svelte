<script>
    import Case from "./Case.svelte";

    export let game;

    console.log(game);
</script>

<div class="container">
    {#each game as row}
        <div class="row">
            {#each row as col}
                <div class="col p-0">
                    <Case value={col}/>
                </div>
            {/each}
        </div>
    {/each}
</div>
