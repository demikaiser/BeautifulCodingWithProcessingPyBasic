def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "round(5.2) = " + str(round(5.2))
    text(string, 30, 60)
    
    string = "round(5.5) = " + str(round(5.5))
    text(string, 30, 120)
    
    
