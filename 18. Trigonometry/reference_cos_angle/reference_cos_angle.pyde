def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "cos(0) = " + str(cos(0))
    text(string, 30, 60)
    
    string = "cos(PI/2) = " 
    string += str(round(cos(PI/2)))
    text(string, 30, 120)
    
    
