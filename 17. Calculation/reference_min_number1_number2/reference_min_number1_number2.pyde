def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "min(1, 2) = " + str(min(1, 2))
    text(string, 30, 60)
    
    string = "min(5, 3) = " + str(min(5, 3))
    text(string, 30, 120)
    
    
    
