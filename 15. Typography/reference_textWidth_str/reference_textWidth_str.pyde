def setup():
    size(640, 360)
    myFont = createFont("Roboto Bold", 48)
    textFont(myFont)
    
def draw():
    background(255)
    string = "Roboto Bold"
    w = textWidth("Roboto Bold")
    
    fill(205, 0, 0, 255)
    text(str(w), 30, 60)
    text(string, 30, 120)
    text(string, 30 + w, 180)
    
    
    
    
    
    
