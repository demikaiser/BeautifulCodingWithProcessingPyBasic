def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "atan(0) = " + str(atan(0))
    text(string, 30, 60)
    
    string = "atan(1) = " + str(atan(1))
    text(string, 30, 120)
    
    
    
