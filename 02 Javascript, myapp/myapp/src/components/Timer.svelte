<script>
    
    let elapsedTime = $state(0)

    // spustí
    // setTimeout(funkce, 1000)

    // opakuje stále
    //setInterval(funkce, 1000)

    setInterval(()=>{ //=> je stejné jako function, akorát se píše za ()
        elapsedTime += 1
    }, 1000)

</script>

<p style="margin-right: 20px;">Time: {elapsedTime}</p>