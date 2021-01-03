<script>
    
    // Value of the case ([1-6]), -1 if bomb !
    export let value = 0;

    let flagged = false;
    let clicked = false;
    
    let image = 'img/case.png';

    function handleClick(event) {
        
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
    }

    // Update the image path based on the current state
    $: {
        if (flagged)
            image = 'img/flag.png';
        else if (clicked) {
            // If bomb
            if (value == -1)
                image = 'img/bomb.png';
            else
                image = "img/" + value + ".png";
        }
        else
            image = 'img/case.png';
    }

</script>

<style>
    .case {
        width: 100%;
        height: 100%;
        display: inline-block;
    }

    img {
        width: 100%;
    }
</style>

<span class="case" on:click={handleClick} on:contextmenu={handleClick} oncontextmenu="return false;">
    <img src={image} alt="case" />
</span>
