def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    for x in range(1, 31):
        circle(x * 20 + 5, 
               noise(x) * 50 + 180, 
               10)
    
    
    
    
