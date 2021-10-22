def setup():
    size(640, 360)
    
def draw():
    background(255)
    
    color_switch = True
    
    x = 0
    y = 0
    
    while (x < 640) and (y < 360):
        if color_switch:
            fill(255)
        else:
            fill(0)
        color_switch = not color_switch
        
        rect(x, y, 20, 20)
        
        x += 20
        if x == 640:
            x = 0
            y += 20
            color_switch = not color_switch
    
    
   
    
