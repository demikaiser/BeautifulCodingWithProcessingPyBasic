def setup():
    size(640, 360)
    myFont = createFont("Roboto Bold", 48)
    textFont(myFont)
    
def draw():
    background(255)
    lines = "Line1\nLine2\nLine3"
    fill(200, 0, 0, 204)
    
    textLeading(50) 
    text(lines, 30, 60)
    textLeading(90)
    text(lines, 230, 60)
    textLeading(130)
    text(lines, 430, 60)
    
    
