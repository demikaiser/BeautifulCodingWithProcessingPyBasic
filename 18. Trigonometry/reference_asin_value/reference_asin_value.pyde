def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "asin(0) = " + str(asin(0))
    text(string, 30, 60)
    
    string = "asin(1) = " + str(asin(1))
    text(string, 30, 120)
    
    
    
