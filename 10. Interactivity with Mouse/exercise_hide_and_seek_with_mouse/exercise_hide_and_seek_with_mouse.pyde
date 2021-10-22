def setup():
    size(640, 360)
    
def draw():
    background(0)
    
    if (0 < mouseX and mouseX < 160) and (0 < mouseY and mouseY < 180):
        circle(80, 90, 90)
    if (160 < mouseX and mouseX < 320) and (0 < mouseY and mouseY < 180):
        circle(240, 90, 90)
    if (320 < mouseX and mouseX < 480) and (0 < mouseY and mouseY < 180):
        circle(400, 90, 90)
    if (480 < mouseX and mouseX < 640) and (0 < mouseY and mouseY < 180):
        circle(560, 90, 90)
        
    if (0 < mouseX and mouseX < 160) and (180 < mouseY and mouseY < 360):
        circle(80, 270, 90)
    if (160 < mouseX and mouseX < 320) and (180 < mouseY and mouseY < 360):
        circle(240, 270, 90)
    if (320 < mouseX and mouseX < 480) and (180 < mouseY and mouseY < 360):
        circle(400, 270, 90)
    if (480 < mouseX and mouseX < 640) and (180 < mouseY and mouseY < 360):
        circle(560, 270, 90)

    
    
    
    
    
