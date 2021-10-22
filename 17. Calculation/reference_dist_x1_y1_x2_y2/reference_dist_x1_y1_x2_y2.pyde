def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "dist(0, 0, 1, 1) = " 
    string += str(dist(0, 0, 1, 1))
    text(string, 30, 60)

    string = "dist(0, 0, 0, 5) = " 
    string += str(dist(0, 0, 0, 5))   
    text(string, 30, 120)
    
    
