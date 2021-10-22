def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "radians(90) = " + str(radians(90))
    text(string, 30, 60)
    
    string = "radians(180) = " + str(radians(180))
    text(string, 30, 120)
    
    
    
