def setup():
    size(640, 360)
    global lines
    lines = loadStrings("https://www.google.com")
    
def draw():
    background(255)
    textSize(24)
    fill(0, 0, 0, 255)
    leading = 60
    for line in lines:
        text(line, 30, leading)
        leading += 60
    noLoop()
    
    
