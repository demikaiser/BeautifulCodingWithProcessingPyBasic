def setup():
    size(640, 360)
    noiseSeed(77)
  

def draw(): 
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)
    string = str(degrees(atan2(mouseY, mouseX)))
    text(string, 30, 120)
    
    
    
    
