def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    image(img, 0, 0, 640, 360)
    
    
