<script>
    import { shared } from "$lib/shared.svelte"

    function clear(){
        shared.score = 0
    }
</script>

<button class = "button2" onclick={clear}>Clear</button>

<style>
    .button2{
        background-color: rgb(110, 11, 0);
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
        color: white;
    }

    .button2:hover {
        background-color: rgb(110, 50, 43);
    }
</style>