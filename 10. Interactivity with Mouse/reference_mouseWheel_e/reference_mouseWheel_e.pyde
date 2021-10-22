wheel_position = 0

def setup():
    size(640, 320)
    
def draw():
    background(0)
    textSize(60)
    text("Wheel Position: " + str(wheel_position), 
         50, 100)
    
def mouseWheel(event): 
    global wheel_position
    wheel_position += event.getCount()
    
    
    
    
    
    
    
