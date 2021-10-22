
def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    tint(255, 0, 0, 255)
    image(img, 0, 0)
    
