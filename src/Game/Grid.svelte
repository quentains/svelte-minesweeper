<script>
    import Case from "./Case.svelte";

    export let width = 16;
    export let height = 16;
</script>

<div class="container">
    {#each Array(height) as _, i}
        <div class="row">
            {#each Array(width) as _, j}
                <div class="col p-0">
                    <Case/>
                </div>
            {/each}
        </div>
    {/each}
</div>
