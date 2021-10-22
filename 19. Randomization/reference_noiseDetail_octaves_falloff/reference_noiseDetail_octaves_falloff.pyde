def setup():
    size(640, 360)
    noiseSeed(77)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    noiseDetail(4, 0.50)  # Default.
    for x in range(1, 31):
        circle(x * 20 + 5, 
               noise(x) * 50 + 180, 10)
    
    fill(255, 0, 0, 255)
    noiseDetail(40, 0.75)
    for x in range(1, 31):
        circle(x * 20 + 5, 
               noise(x) * 50 + 180, 10)
    
        
        
        
        
