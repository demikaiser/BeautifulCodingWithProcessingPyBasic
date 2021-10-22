def setup():
    size(640, 360)
    myFont = createFont("Roboto Bold", 48)
    textFont(myFont)
    
def draw():
    background(255)
    fill(200, 0, 0, 204)
    
    textAlign(LEFT, TOP)    
    text("Roboto Bold", 0, 0)
    
    textAlign(CENTER, CENTER)   
    text("Roboto Bold", 320, 180)
    
    textAlign(RIGHT, BOTTOM)
    text("Roboto Bold", 640, 360)
    
    
    
