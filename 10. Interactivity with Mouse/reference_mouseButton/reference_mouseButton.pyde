def setup():
    size(640, 320)
    
def draw():
    background(0)
    textSize(64)
    
def mousePressed(): 
    if mouseButton == LEFT:
        text("Left Button!", 50, 100)
    elif mouseButton == RIGHT:
        text("Right Button!", 50, 100)   
    
    
    
    
