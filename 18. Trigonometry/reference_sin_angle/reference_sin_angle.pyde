def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "sin(0) = " + str(sin(0))
    text(string, 30, 60)
    
    string = "sin(PI/2) = " + str(sin(PI/2))
    text(string, 30, 120)
    
    
    
    
