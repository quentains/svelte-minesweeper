<script>
    import Case from "./Case.svelte";

    export let game;

    let width = game[0].length;
    let height = game.length;
    game = game.map((e,j) => e.map((x, i) => {return {"x": i, "y": j, "value": x, "flagged": false, "clicked": false}}));
   
    // Update the game structure
    function handleUpdate(event) {
        let x = event.detail.x;
        let y = event.detail.y;
        let clicked = event.detail.clicked;
        let flagged = event.detail.flagged;
        game[y][x]["clicked"] = clicked;
        game[y][x]["flagged"] = flagged;
    }
    
    // If case is empty, reveal the adjacent cases
    function handleEmpty(event) {
        let x = event.detail.x;
        let y = event.detail.y;
        
        for (let j = y-1; j <= y+1; ++j) {
            for (let i = x-1 ; i <= x+1 ; ++i) {
                if ((i >= 0) && (j >= 0) && (i<width) && (j<height)) {
                    game[j][i]['clicked'] = true;
                }
            }
        }
    }
    
    // Check if the game is finished
    $ : {
        const result = game.map(line => line.every(c => c.flagged || c.clicked));
        if (!result.includes(false)) {
            alert("Finished !");
        }
    }
</script>

<div class="container">
    {#each game as row}
        <div class="row">
            {#each row as data}
                <div class="col p-0">
                    <Case {...data} on:empty={handleEmpty} on:update={handleUpdate}/>
                </div>
            {/each}
        </div>
    {/each}
</div>
