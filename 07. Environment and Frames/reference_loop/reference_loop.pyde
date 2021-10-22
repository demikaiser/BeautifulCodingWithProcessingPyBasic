def setup():
    size(640, 360)
    
def draw():
    print("Start of the program.")
    noLoop()
    if frameCount == 2:
        print("This will not excute!")
    if frameCount > 3:
        print("Program is running...")
    
def mouseClicked(): 
    loop()
