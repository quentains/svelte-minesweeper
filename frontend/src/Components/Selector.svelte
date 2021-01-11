<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let choice = ["Easy", "Normal", "Hard"];

    export let selected = 1;

</script>


<style>
    span {
        text-align: center;
    }

    .first {
        border-radius: 10px 0px 0px 10px;
        padding-left: 10px;
    }

    .last {
        border-radius: 0px 10px 10px 0px;
        padding-right: 10px;
    }

    button {
        padding-top: 10px;
        background-color : #333;
        color : white;
        text-transform: uppercase;
        border: none;
    }

    .selected {
        background-color : #111;
        border: 1px grey solid;
    }
</style>

<span>
    {#each choice as text, i}
        <button on:click={e => selected = i} type="button" class="{i==0?'first':''} {i==choice.length-1?'last':''} {i==selected?'selected':''}">{text}</button>
    {/each}
</span>