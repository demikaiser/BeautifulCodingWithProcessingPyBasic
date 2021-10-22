def setup():
    size(640, 360)
    textSize(48)
    global bigImage
    bigImage = requestImage("dog.jpg")
    
def draw():
    background(0)
    if bigImage.width == 0:
        text("Loading the image...", 50, 100)
    elif bigImage.width == -1:
        text("Error occurred!", 50, 100)
    else:
        image(bigImage, 0, 0)
        
        
