def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "norm(3, 0, 10) = " 
    string += str(norm(3, 0, 10))
    text(string, 30, 60)
    
    string = "norm(3, 0, 100) = " 
    string += str(norm(3, 0, 100))
    text(string, 30, 120)
    
    
