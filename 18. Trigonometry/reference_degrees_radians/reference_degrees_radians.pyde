def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "degrees(PI/2) = " + str(degrees(PI/2))
    text(string, 30, 60)
    
    string = "degrees(PI) = " + str(degrees(PI))
    text(string, 30, 120)
    
    
    
