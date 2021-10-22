light = 0
x = 0

def setup():
    size(640, 360)
    myFont = createFont("Roboto Bold", 48)
    textFont(myFont)
    
def draw():
    global light
    global x
    background(0)
    textSize(128)
    
    fill(0, 255, 0, light)
    text("NEON!", x, 210)
    
    light += 10
    if light > 255:
        light = 0
    
    x += 10
    if x > 640:
        x = -360
    
    
    
