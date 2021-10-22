last_key = ''

def setup():
    size(640, 320)
    
def draw():
    background(0)
    textSize(64)
    text(last_key, 50, 100)
    
def keyPressed():
    global last_key
    last_key = key 
    
    
    
    
