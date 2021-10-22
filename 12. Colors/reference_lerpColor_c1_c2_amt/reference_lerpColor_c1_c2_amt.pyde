def setup():
    size(640, 360)
    
def draw():
    color1 = color(255, 125, 0, 255)
    color2 = color(0, 125, 255, 255)

    fill(color1)
    circle(120, 180, 90)
    
    fill(lerpColor(color1, color2, 0.25))
    circle(220, 180, 90)
    
    fill(lerpColor(color1, color2, 0.50))
    circle(320, 180, 90)
    
    fill(lerpColor(color1, color2, 0.75))
    circle(420, 180, 90)
    
    fill(color2)
    circle(520, 180, 90)
    
    
    
    
