def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    image(img, 0, 0, 320, 180)
    face = get(100, 20, 140, 120)
    image(face, 320, 180)
    
    
    
    
    
