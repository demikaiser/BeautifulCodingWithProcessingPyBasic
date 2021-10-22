radius = 150
direction = "UP"  # "UP" | "DOWN"

def setup():
    size(640, 360)
    
def draw():
    global radius
    global direction
    background(255)
    draw_target(radius)
    if direction == "UP":
        radius += 1
    elif direction == "DOWN":
        radius -= 1
    if radius == 300:
        direction = "DOWN"
    elif radius == 150:
        direction = "UP"
    
def draw_target(largest_radius):
    strokeWeight(1.5)
    fill(0, 0, 255, 255)
    circle(width/2, height/2, lerp(0, largest_radius, 1.00))
    fill(0, 255, 0, 255)
    circle(width/2, height/2, lerp(0, largest_radius, 0.80))
    fill(255, 255, 0, 255)
    circle(width/2, height/2, lerp(0, largest_radius, 0.60))
    fill(255, 127, 0, 255)
    circle(width/2, height/2, lerp(0, largest_radius, 0.40))
    fill(255, 0 , 0, 255)
    circle(width/2, height/2, lerp(0, largest_radius, 0.20))
    
    
    
    
    
    
    
    
    

    
    
    
