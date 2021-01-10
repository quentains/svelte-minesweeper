<script>
	import { onMount, onDestroy } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    import Case from "./Case.svelte";

    export let game;
    export let time;

    let starting_point = game.starting_point;
    game = game.board;

    var bomb_song = new Audio('sound/explosion.mp3');
    var win_song = new Audio('sound/celebration.mp3');

    let width = game[0].length;
    let height = game.length;

    // Variables to detect the end of the game
    let nb_flags = 0;
    let nb_clicked = 1;
    let nb_bombs = game.flat(2).reduce((total,x) => (x==-1 ? total+1 : total), 0)

    let started = false;
    let finished = false;

    // Populate the needed structure
    // (useless to get it from the backend)
    game = game.map((e,j) => e.map((x, i) => {return {"x": i, "y": j, "value": x, "flagged": false, "clicked": false}}));
    
    // Reveal the starting point
    game[starting_point.y][starting_point.x].clicked = true;

    // Create the timing and stop it on destroy
    const interval = setInterval(update_time, 1000);
    onDestroy(async () => {
        clearInterval(interval);
    });

    // Increase the timer once a click is done
    function update_time() {
        if (started) {
            time++;
        }
    }
    
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
        if (event.detail.isBomb && clicked && !finished) {
            bomb_song.play();
            // Show all the disarmed bombs
            // the rest of the bombs
            bombs_animation();
            finished = true;
        }
        started = true;
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

    function bombs_animation() {
        // This function reveal all bombs
        // by calling bomb_reveal()

        let bombs = [];
            for (let j=0 ; j < height ; j++) {
                for (let i=0 ; i < width ; i++) {
                    if (game[j][i].value == -1) {
                        bombs.push({'x': i, 'y': j});
                    }
                }
            }

            // Shuffle the array in order to reveal
            // the bombs in a random order
            shuffleArray(bombs);
            bomb_reveal(bombs);
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    function bomb_reveal(bombs) {
        // Recursive function, reveal all bombs in 1 sec.
        if (bombs.length == 0){
            return;
        }
        let coord = bombs.shift();
        let x = coord.x;
        let y = coord.y;

        // If already detected -> disarmed
        if (game[y][x].flagged) {
            game[y][x].value = -2;
        }
        // Else -> explosion
        else {
            game[y][x].value = -3;
        }

        // Little time before revealing the next one
        setTimeout(bomb_reveal, 1000/nb_bombs, bombs);

    }
    
    // Check if the game is finished
    $ : {
        // If there are as many flags as bombs AND the all the other cases are clicked
        if ( (nb_flags == nb_bombs) && (nb_flags + nb_clicked == width * height) ) {
            win_song.play();
            // Show all the disarmed bombs
            bombs_animation();
            finished = true;
        }

        if (finished) {
            clearInterval(interval);
        }
    }
</script>

<style>
	.container {
		display: flex;
        justify-content: center;
		flex-direction: column;
        height: 100%;
        min-height: 100%;
	}

    .row {
        display: flex;
        flex-direction: row;
        justify-content: center;
    }

    .case {
        width: 100%;
    }

</style>

<!-- https://i.redd.it/5u83w0fyzzf31.jpg -->
<div class="container">
    {#each game as row}
        <div class="row">
            {#each row as data}
                <div class="case">
                    <Case {...data} finished={finished} on:empty={handleEmpty} on:update={handleUpdate}/>
                </div>
            {/each}
        </div>
    {/each}
</div>
