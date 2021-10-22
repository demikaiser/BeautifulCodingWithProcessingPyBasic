def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "lerp(0, 10, 0.33) = " 
    string += str(lerp(0, 10, 0.33))
    text(string, 30, 60)
    
    string = "lerp(0, 10, 0.66) = " 
    string += str(lerp(0, 10, 0.66))    
    text(string, 30, 120)
    
    
    
