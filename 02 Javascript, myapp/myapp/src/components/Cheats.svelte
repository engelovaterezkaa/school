<script>
    import { shared } from "$lib/shared.svelte"
    import flower from "$lib/assets/flower.png"

    let text = $state("Cheaty")
    let color = $state("black")
    let visible = $state(false)

    function cheatCode() {
        if (text === "money") {
            color = "green"
            shared.score += 100
        }
    }

    function show(){
        visible = true
    }

</script>

<img class="icon" onclick={show} src={flower} alt="">

<div class="chet" style="visibility: {visible? 'visible':'hidden'};"> 
    <p class="par" style="color: {color}">{text}</p>
    <input class="in" bind:value={text} type="text" oninput={cheatCode}>
    <!-- <button onclick={cheatCode}>Submit</button> -->
</div>

<style>
    .chet{
        display: flex;
        align-items: center;
        justify-content: center;
        visibility: hidden;
    }

    .in{
        border-radius: 20px;
        padding: 5px;
    }

    .icon{
        height: 30px;
        position: absolute;
        right: 2%;
        top: 2%;
    }
</style>