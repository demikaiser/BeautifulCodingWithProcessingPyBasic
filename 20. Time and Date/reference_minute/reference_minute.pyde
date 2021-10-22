def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "Now is 20:55:21"
    text(string, 30, 60)
    
    string = "minute() = " + str(minute())
    text(string, 30, 120)
    
