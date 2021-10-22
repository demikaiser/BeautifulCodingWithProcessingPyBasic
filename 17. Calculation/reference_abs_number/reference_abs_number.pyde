def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "abs(13) = " + str(abs(13))
    text(string, 30, 60)
    
    string = "abs(-13) = " + str(abs(-13))
    text(string, 30, 120)
    
    
    
    
