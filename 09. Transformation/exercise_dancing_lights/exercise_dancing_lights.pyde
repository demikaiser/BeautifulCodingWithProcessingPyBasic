angle = PI

def setup():
    size(640, 360)
    frameRate(12)

def draw():
    global angle
    background(255)
    translate(320, 180)
    
    rotate(angle)
    angle += 0.015
    
    for i in range(0, 18):
        fill(random(128, 255), 
             random(128, 255),
             random(128, 255),
             255)
        rotate(2 * PI * 1/18)
        circle(120, 0, 30)

    
    
   
    
    
    
    
