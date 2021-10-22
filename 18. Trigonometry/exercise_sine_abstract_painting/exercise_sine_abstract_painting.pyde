def setup():
    size(640, 360)
    background(255)
    
def draw():
    draw_sine_wave(random(100, 700), random(0, 150))

def draw_sine_wave(frequency, wave_height):
    stroke(random(135, 255), random(135, 255), 
           random(135, 255), random(135, 255))
    angle = 0.0
    angle_increment = TWO_PI/frequency
    prev_x = 0
    prev_y = height/2
    for i in range(-width, width):
        x = i
        y = height/2 + sin(angle) * wave_height
        line(prev_x, prev_y, x, y)
        prev_x = x
        prev_y = y
        angle += angle_increment
        
    
    

    
    
