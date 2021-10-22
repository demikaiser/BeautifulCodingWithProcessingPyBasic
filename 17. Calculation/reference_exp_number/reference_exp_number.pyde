def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "exp(1) = " + str(exp(1))
    text(string, 30, 60)
    
    string = "exp(2) = " + str(exp(2))
    text(string, 30, 120)
    
