x = 20
y = 32
last_key = ""

def setup():
    size(640, 360)
    background(0)
        
def draw():
    textSize(32)
    text(last_key, x, y)
    
def keyPressed():
    global x
    global y
    global last_key
    
    last_key = key
    x += 20
    
    if x > 630:
        x = 20
        y += 32
    
    
    
    
    
    
