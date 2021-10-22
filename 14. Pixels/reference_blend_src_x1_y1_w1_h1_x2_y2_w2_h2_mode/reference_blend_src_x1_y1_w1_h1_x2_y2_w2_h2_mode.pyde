def setup():
    size(640, 360)
    background(loadImage("dog.jpg"))
    global img
    img = loadImage("dog.jpg")
    
def draw():
    blend(img,
          0, 0, 640, 360,
          0, 0, 320, 180,
          MULTIPLY)
    
    
    
