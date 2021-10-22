def setup():
    size(640, 360)
    myFont = createFont("Roboto Bold", 48)
    textFont(myFont)
    global data
    data = loadStrings("data.txt")
    
def draw():
    global data
    background(255)
    textSize(32)

    x = 15
    y = 15
    y_increment = 45
    
    for element in data:
        name_number = split(element, " ")
        draw_graph(x, y, y_increment, 
                   name_number[0], int(name_number[1]))
        y += y_increment
    noLoop()
    
def draw_graph(x, y, y_increment, name, number):
    fill(random(125, 255), random(125, 255), random(125, 255), 255)
    rect(x, y, number * 50, y_increment)
    textAlign(LEFT, TOP)
    text(name, number * 50 + 25, y)
    
    
    
    
    
    
    
