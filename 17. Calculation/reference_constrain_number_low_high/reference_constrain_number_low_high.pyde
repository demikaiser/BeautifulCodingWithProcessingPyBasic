def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "constrain(15, 0, 10) = " 
    string += str(constrain(15, 0, 10))
    text(string, 30, 60)
    
    string = "constrain(-5, 0, 10) = " 
    string += str(constrain(-5, 0, 10))
    text(string, 30, 120)
    
    
    
    
    
