def setup():
    size(640, 320)
    
def draw():
    background(0)
    textSize(64)
    text("pmouseX: " + str(pmouseX), 50, 100)
    delay(1000)  # Delay 1 second.
    text("mouseX: " + str(mouseX), 50, 200)
    
    
