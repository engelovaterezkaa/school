<script>
	import { shared } from "$lib/shared.svelte";
    let { level } = $props()

    let upgradeClicked = $state(false)

    function upgrade(){
        if (level === 1) {
            shared.multi = 2
        } else if (level === 2) {
            shared.multi = 5
        } else if (level === 3) {
            shared.multi = 10
        } else if (level === 4){
            setInterval(()=>{ 
                shared.score += 1
            }, 1000)
        }
        upgradeClicked = true 
    }


</script>

<div>
    {#if upgradeClicked}
        <p>Upgraded</p>
    {:else}
        <p>Upgrade clicker</p>
    {/if}

    <button onclick={upgrade}>Upgrade</button>
</div>

<style>
    button {
        color: white;
        background-color: var(--color);
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
        margin-right: 50px;
    }

    button:hover {
        background-color: rgb(245, 156, 146);
    }
</style>