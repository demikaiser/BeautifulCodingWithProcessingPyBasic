def setup():
    size(640, 360)
    global lines
    lines = loadStrings("fruits.txt")
    
def draw():
    background(255)
    textSize(48)

    fill(255, 0, 0, 255)
    text(lines[0], 30, 60)
    fill(255, 204, 0, 255)
    text(lines[1], 30, 120)
    fill(255, 102, 0, 255)
    text(lines[2], 30, 180)
    
    
    
    
    
    
    
    
    
