def setup():
    size(640, 360)
    global img
    img = loadImage("dog.jpg")
    
def draw():
    image(img, 0, 0, 320, 180)
    face = get(100, 20, 140, 120)
    set(320, 180, face)
    
    for x in range(600, 640):
        for y in range(320, 360): 
            set(x, y, color(0, 0, 0, 255))
    
    
