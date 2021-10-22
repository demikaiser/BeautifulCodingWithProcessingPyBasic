last_key = ''

def setup():
    size(640, 320)
    
def draw():
    background(0)
    textSize(64)
    text(last_key, 50, 100)
    
def keyPressed():
    global last_key
    if (key == CODED) and (keyCode == SHIFT):
        last_key = "SHIFT"
    else:
        last_key = key

    
    
