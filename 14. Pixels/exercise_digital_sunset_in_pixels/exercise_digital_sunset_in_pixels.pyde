def setup():
    size(640, 360)
    global colors
    global number_pixels_array
    color1 = color(253, 231, 103, 255)
    color2 = color(158, 37, 143, 255)
    colors = []
    for i in range(10):
        colors.append(lerpColor(color1, color2, float(i)/10))
    number_pixels_array = []
    for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        number_pixels_array.append(width * height * i)
    
def draw():
    loadPixels()
    index_colors = 0
    for i in range(width * height): 
        pixels[i] = colors[index_colors]
        if i in number_pixels_array:
            index_colors += 1
    updatePixels()
    filter(BLUR, 10)
    delay(1000)
    
    
    
