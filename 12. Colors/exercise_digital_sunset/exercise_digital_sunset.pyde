def setup():
    size(640, 360)
    
def draw():
    color1 = color(253, 231, 103, 255)
    color2 = color(158, 37, 143, 255)
    
    amt = 0
    x = 0
    y = 0
    
    for i in range (0, 12):
        fill(lerpColor(color1, color2, amt))
        noStroke()
        rect(x, y, 640, 30)
        y += 30
        amt += 0.0833
    
    
