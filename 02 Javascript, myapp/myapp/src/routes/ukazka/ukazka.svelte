<!-- spuštění = npv run dev -->
 <!-- + page.svelte ukazuje jako index -->
<script>
    import Button from "../components/Button.svelte"

    let message = "Hello!"
    let src = "https://tse1.explicit.bing.net/th/id/OIP.Gic96FsQ57JDwJ1g1RVKkwHaIZ?rs=1&pid=ImgDetMain&o=7&rm=3"
    let score = $state(0)

    function increment() {
        score += 1
    }
</script>


<h1>Vše funguje</h1>
<ul>
    <li>Vše</li>
    <li>funguje</li>
    <li>bez</li>
    <li>problémů</li>
</ul>

<h2>{message.toUpperCase()} random person</h2>
<img {src} class="image" alt=""> 
<!-- source je automaticky -->

<p>{score >= 5 ? "Good!" : "Neutral"}</p>
<!-- : je else -->
<p>Points: {score}</p>
<button onclick={increment}>Click me!</button>
<Button />

<style>
    .image {
        height: 200px;
    }
</style>
