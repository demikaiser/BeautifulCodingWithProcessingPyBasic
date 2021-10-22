def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    text(str(randomGaussian()), 30, 60)
    text(str(randomGaussian()), 30, 120)
    text(str(randomGaussian()), 30, 180)
    delay(1000)

    
    
    
    
