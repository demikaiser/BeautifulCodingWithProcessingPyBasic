def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "Program started."
    text(string, 30, 60)
    
    string = "millis() = " + str(millis())
    text(string, 30, 120)
    
    
