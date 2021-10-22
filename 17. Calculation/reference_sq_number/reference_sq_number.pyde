def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "sq(2) = " + str(sq(2))
    text(string, 30, 60)
    
    string = "sq(10) = " + str(sq(10))
    text(string, 30, 120)
    
    
