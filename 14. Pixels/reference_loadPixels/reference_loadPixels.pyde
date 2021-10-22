def setup():
    size(640, 360)
    global pink
    pink = color(255, 102, 204)
    
def draw():
    #loadPixels()
    for i in range(width*height/2): 
        pixels[i] = pink
    updatePixels()
    
    
    
