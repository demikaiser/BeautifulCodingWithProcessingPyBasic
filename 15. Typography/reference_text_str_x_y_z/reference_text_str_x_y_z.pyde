def setup():
    size(640, 360, P3D)
    myFont = createFont("Roboto Bold", 48)
    textFont(myFont)
    
def draw():
    background(255)
    fill(200, 0, 0, 255)
    text("Roboto Bold Font", 30, 60, 0)
    fill(200, 0, 0, 128)
    text("Roboto Bold Font", 30, 120, -100)
    fill(200, 0, 0, 32)
    text("Roboto Bold Font", 30, 180, -300)
    
    
    
