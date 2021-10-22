def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "pow(2, 2) = " + str(pow(2, 2))
    text(string, 30, 60)
    
    string = "pow(2, 10) = " + str(pow(2, 10))
    text(string, 30, 120)
    
    
