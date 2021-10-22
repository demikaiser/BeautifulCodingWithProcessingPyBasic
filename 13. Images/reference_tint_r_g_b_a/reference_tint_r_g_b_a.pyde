def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    tint(0, 255, 0, 5)
    image(img, 0, 0, 640, 360)
    
    
    
