def setup():
    size(640, 360)
    
def draw():
    red_color = color(255, 0, 0, 255)
    blue_color = color(0, 0, 255, 255)
    blended_color = blendColor(red_color, 
                               blue_color, 
                               ADD)
    fill(blended_color)
    circle(320, 180, 180)
    
    
    
    
    
