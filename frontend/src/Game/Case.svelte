<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    // Value of the case ([1-6]), -1 if bomb !
    export let x;
    export let y;
    export let value = 0;
    export let flagged = false;
    export let clicked = false;

    export let finished = false;

    let isBomb = value == -1 ? true : false;
    let isDisarmed = value == -2 ? true : false;
    let isExplode = value == -3 ? true : false;
    
    let image = 'img/case.png';

    function handleClick(event) {
        // If game is finished, do nothing
        if (finished)
            return;

        // Show the case
        if (event.button == 0){
            if (!flagged)
                clicked = true;
        }

        // Toggle the flag
        else if (event.button == 2) {
            if (!clicked)
                flagged = !flagged;
        }

        dispatch('update', {
            x:x,
            y:y,
            flagged:flagged,
            clicked:clicked,
            isBomb: isBomb
        });
    }

    // Update the image path based on the current state
    $: {
        isDisarmed = value == -2 ? true : false;
        isExplode = value == -3 ? true : false;

        if (isDisarmed){
            image = '/img/bomb_sad.svg';
        }
        else if (isExplode) {
            image = '/img/bomb_happy.svg';
        }
        else {
            if (flagged)
                image = 'img/flag.svg';
            else if (clicked) {
                // If bomb
                if (isBomb)
                    image = 'img/bomb_happy.svg';
                else {
                    image = "img/" + value + ".png";
                    if (value == 0){
                        dispatch('empty', {x:x, y:y});
                    }
                }
            }
            else
                image = 'img/case.png';
        }
    }

</script>

<style>
    img {
        width: 100%;
    }
</style>


<img src={image} alt="case" class="case" on:click={handleClick} on:contextmenu={handleClick} oncontextmenu="return false;" ondragstart="return false;"/>

