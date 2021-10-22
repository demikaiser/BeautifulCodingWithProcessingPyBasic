def setup():
    size(640, 360)
    
def draw():
    background(255)
    fill(0, 0, 0, 255)
    textSize(48)

    string = "Today is 2021/08/05"
    text(string, 30, 60)
    
    string = "day() = " + str(day())
    text(string, 30, 120)
    
    
    
