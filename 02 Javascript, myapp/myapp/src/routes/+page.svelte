<script>
    import Button from "../components/Button.svelte"
    import ResetButton from "../components/ResetButton.svelte"
    import Timer from "../components/Timer.svelte"
    import { shared } from "$lib/shared.svelte"
	import Upgrade from "../components/Upgrade.svelte"
    import Cheats from "../components/Cheats.svelte"
    import flower from "$lib/assets/flower.png"
    
    // import Autoclicker from "../components/Autoclicker.svelte"


    let animScore = $state()

    $effect(() => {
        if (shared.score > 0) {
            animScore = "anim-score"
            setTimeout(() => animScore = "", 100)
        }
    })
    

</script>

<div class="h1-wrap">
    <h1>The Score</h1>
</div>

<div class="wrap">
    <p class={animScore}>{shared.score}</p>
</div>

<div class="Timer-wrap">
<Button message={"Click me!"}/>
<Timer />
<ResetButton />
</div>

<div class="Upgrade-wrap">
    <Upgrade level={1} --color="rgb(255, 169, 216)"/>
    <Upgrade level={2} --color="DarkSalmon"/>
    <Upgrade level={3} --color="pink"/>
    <Upgrade level={4} --color="violet"/>
    <!-- <Autoclicker/> -->
</div>

<div class="Cheats-wrap">
    <Cheats/>
</div>

<!-- <flower/> -->

<style>
.h1-wrap{
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgb(143, 69, 69);
    text-decoration: underline;
    font-weight: bolder;
}

.Timer-wrap{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 40px;
}

.Upgrade-wrap{
    display: flex;
    justify-content: center;
    align-items: center;
	display: flex;
    color: rgb(104, 23, 23);
    font-weight: bolder;
    margin: 10px;
}

.Cheats-wrap{
    display: flex;
    justify-content: center;
    align-items: center;
}

.wrap {
    display: flex;
    justify-content: center;
    align-items: center;
}

.anim-score {
    animation: popout 0.1s linear;
}

.icon{
    height: 30px;
    position: absolute;
    right: 2%;
    top: 2%;
}

@keyframes popout {
    50% {
        scale: 2;
    }
    100% {
        scale: 1;
    }
}
</style>