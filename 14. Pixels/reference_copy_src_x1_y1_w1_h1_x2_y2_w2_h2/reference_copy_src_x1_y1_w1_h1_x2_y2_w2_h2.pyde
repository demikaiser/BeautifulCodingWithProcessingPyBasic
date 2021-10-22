def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    copy(img, 
         200, 40, 280, 240, 
         320, 180, 140, 120)
    image(img, 0, 0, 320, 180)
    copy(100, 20, 140, 120, 
         480, 180, 140, 120)

    
