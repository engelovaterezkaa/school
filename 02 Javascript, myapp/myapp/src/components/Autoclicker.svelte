<script>
    import { shared } from "$lib/shared.svelte"

    function autoClicker() {
        if (!running) { 
            running = true
            setInterval(function() {
                shared.score += 1
            }, 1000)
        }
    }
</script>

<button onclick={autoClicker}>Autoclicker</button>