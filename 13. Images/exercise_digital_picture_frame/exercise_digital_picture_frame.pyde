index = 0

def setup():
    size(640, 360)
    global images
    images = []
    images.append(loadImage("dog.jpg"))
    images.append(loadImage("fox.jpg"))
    images.append(loadImage("sheep.jpg"))
    images.append(loadImage("pig.jpg"))
    
def draw():
    global index
    image(images[index%4], 0, 0, 640, 360)
    index += 1
    delay(3000)
    
    
    
