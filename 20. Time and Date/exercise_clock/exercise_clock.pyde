def setup():
    size(640, 360)
    global background_img
    background_img = loadImage("background.jpg")
    font_roboto = createFont("Roboto Bold", 48)
    textFont(font_roboto)
    
def draw():
    image(background_img, 0, 0, 640, 360)
    
    fill(255, 255, 255, 185)
    textSize(64)
    textAlign(CENTER, CENTER)
    date = str(year()) + "-" + str(month()) + "-" + str(day())
    date += " "
    date += calculate_am_pm_hour()[0]
    text(date, 320, 60)
    
    noStroke()
    fill(255, 255, 255, 95)
    circle(150, 230, 160)
    circle(320, 230, 160)
    circle(490, 230, 160)

    fill(255, 255, 255, 255)
    textSize(100)
    text(str(calculate_am_pm_hour()[1]), 150, 220)
    text(str(minute()), 320, 220)
    text(str(second()), 490, 220)
    
def calculate_am_pm_hour():
    hour_now = hour()
    if hour_now <= 12:
        return ("AM", hour_now)
    else:
        return ("PM", hour_now - 12)
    
    
    
    
    
    
    
    
    
    
    
    
    
