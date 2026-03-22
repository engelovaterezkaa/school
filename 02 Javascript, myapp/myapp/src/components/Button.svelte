<script>
    import { shared } from "$lib/shared.svelte"
    import elapsedTime from "../components/Timer.svelte"
    let { message } = $props()


    function increment(){
        shared.score = shared.score + shared.multi
    }

    // function timeScore() {
    //     setInterval(()=>{ 
    //         shared.multi += 1
    //     }, 1000)
    // }



</script>


<button onclick={increment}>{message}</button>
<!-- <button onclick={timeScore}>Times running out</button> -->

<style>
    button {
        color: white;
        background-color: salmon;
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
        animation: click 0.5s linear;
        margin-right: 15px;
    }

    button:hover {
        background-color: rgb(245, 156, 146);
    }

    @keyframes click {
        50% {
            scale: 1.5;
        }
        100% {
            scale: 1;
        }
    }
</style>