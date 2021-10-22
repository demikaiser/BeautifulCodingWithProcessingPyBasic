def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "acos(1) = " + str(acos(1))
    text(string, 30, 60)
    
    string = "acos(0) = " + str(acos(0))
    text(string, 30, 120)
    
    
    
