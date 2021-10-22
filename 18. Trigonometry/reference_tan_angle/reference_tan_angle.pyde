def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "tan(0) = " + str(tan(0))
    text(string, 30, 60)
    
    string = "tan(PI/4) = " + str(tan(PI/4))
    text(string, 30, 120)
    
    
    
