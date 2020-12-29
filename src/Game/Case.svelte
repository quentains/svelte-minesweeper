<script>
    export let bomb = false;
    export let value = 0;
    let flagged = false;
    let clicked = false;
    let image = 'img/case.png';

    function handleClick(event) {
        if (event.button == 0) {
            clicked = true;       
        }
        if (event.button == 2) {
            if (!clicked) {
                flagged = !flagged; 
            }       
        }
    }

    $: {
        if (flagged) {
            image = 'img/flag.png';
        }
        else if (clicked) {
            if (bomb) {
                image = 'img/bomb.png';
            }
            else {
                image = "img/" + value + ".png";
            }
        }
        else {
            image = 'img/case.png';
        }

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
