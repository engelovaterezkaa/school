function setup(){
    createCanvas(windowWidth, windowHeight)
    colorMode(HSB, 360, 100, 100, 100)
    background(0)
}

function draw(){
    fill(0, 0, 0, 10)
    rect(0, 0, width, height)

    noStroke() //neni border
    fill(255, 255, 0)
    let h = frameCount % 360 //hue
    let size = random(5, 20)
    fill(h, 80, 100, 80) //hue, saturation, brightness, alpha
    ellipse(mouseX, mouseY, size)
}