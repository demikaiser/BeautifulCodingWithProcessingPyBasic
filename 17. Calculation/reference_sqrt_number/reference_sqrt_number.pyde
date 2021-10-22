def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "sqrt(4) = " + str(sqrt(4))
    text(string, 30, 60)
    
    string = "sqrt(25) = " + str(sqrt(25))
    text(string, 30, 120)
