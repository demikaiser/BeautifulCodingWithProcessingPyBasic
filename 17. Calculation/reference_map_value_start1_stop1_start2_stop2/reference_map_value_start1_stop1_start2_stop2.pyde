def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(32)

    string = "map(1, 0, 10, 0, 1) = " 
    string += str(map(1, 0, 10, 0, 1))
    text(string, 30, 60)
    
    string = "map(-1, 0, 10, 0, 1) = " 
    string += str(map(-1, 0, 10, 0, 1))
    text(string, 30, 120)
    
    
    
