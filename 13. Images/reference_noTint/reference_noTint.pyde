def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    tint(0, 255, 0, 5)
    image(img, 0, 0, 320, 180)
    noTint()
    image(img, 320, 180, 320, 180)
    
    
    
    
