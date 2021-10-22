def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "max(1, 2) = " + str(max(1, 2))
    text(string, 30, 60)
    
    string = "max(5, 3) = " + str(max(5, 3))
    text(string, 30, 120)
    
    
    
    
