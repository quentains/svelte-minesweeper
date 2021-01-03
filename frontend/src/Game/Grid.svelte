<script>
    import Case from "./Case.svelte";

    export let game;

    var bomb_song = new Audio('sound/explosion.mp3');
    var win_song = new Audio('sound/celebration.mp3');

    let width = game[0].length;
    let height = game.length;

    // Variables to detect the end of the game
    let nb_flags = 0;
    let nb_clicked = 0;
    let nb_bombs = game.flat(2).reduce((total,x) => (x==-1 ? total+1 : total), 0)
    
    // Populate the needed structure
    // (useless to get it from the backend)
    game = game.map((e,j) => e.map((x, i) => {return {"x": i, "y": j, "value": x, "flagged": false, "clicked": false}}));
   
    // Update the game structure
    function handleUpdate(event) {
        let x = event.detail.x;
        let y = event.detail.y;
        let clicked = event.detail.clicked;
        let flagged = event.detail.flagged;

        // Add a new flag
        if (!game[y][x].flagged && flagged)
            nb_flags++;

        // Remove a flag
        if (game[y][x].flagged && !flagged)
            nb_flags--;

        // New clicked case
        if (!game[y][x].clicked && clicked)
            nb_clicked++;

        game[y][x].clicked = clicked;
        game[y][x].flagged = flagged;

        // If clicked on a bomb -> Loose
        if (event.detail.isBomb && clicked)
            bomb_song.play();
    }
    
    // If case is empty, reveal the adjacent cases
    function handleEmpty(event) {
        let x = event.detail.x;
        let y = event.detail.y;
        
        for (let j = y-1; j <= y+1; j++) {
            for (let i = x-1 ; i <= x+1 ; i++) {
                if ((i >= 0) && (j >= 0) && (i<width) && (j<height)) {
                    // If not already counted (nb_clicked)
                    if (!game[j][i].clicked)
                        nb_clicked++;
                    game[j][i].clicked = true;
                }
            }
        }
    }
    
    // Check if the game is finished
    $ : {
        // If there are as many flags as bombs AND the all the other cases are clicked
        if ( (nb_flags == nb_bombs) && (nb_flags + nb_clicked == width * height) ) {
            win_song.play();
        }
    }
</script>

<!-- https://i.redd.it/5u83w0fyzzf31.jpg -->
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
