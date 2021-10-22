def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "log(e) = " + str(log(2.7182))
    text(string, 30, 60)
    
    string = "log(10) = " + str(log(10))
    text(string, 30, 120)
    
    
    
