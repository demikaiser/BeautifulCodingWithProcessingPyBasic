def setup():
    size(640, 360)
    rectMode(CORNERS)
    
def draw():
    background(255)

    basket = [0, 0, 0, 0, 0, 0, 0]
    
    for i in range(700):
        random_number = randomGaussian()
        
        if -3.5 < random_number and random_number < -2.5:
            basket[0] += 1
        elif -2.5 < random_number and random_number < -1.5:
            basket[1] += 1
        elif -1.5 < random_number and random_number < -0.5:
            basket[2] += 1
        elif -0.5 < random_number and random_number < +0.5:
            basket[3] += 1
        elif +0.5 < random_number and random_number < +1.5:
            basket[4] += 1
        elif +1.5 < random_number and random_number < +2.5:
            basket[5] += 1
        elif +2.5 < random_number and random_number < +3.5:
            basket[6] += 1
    
    height_box = 9*height/10
    offset = 300
    
    fill(235, 70, 53, 255)
    rect(40, height_box, 120, offset - basket[0])
    fill(235, 149, 52, 255)
    rect(120, height_box, 200, offset - basket[1])
    fill(235, 219, 52, 255)
    rect(200, height_box, 280, offset - basket[2])
    fill(26, 255, 0, 255)
    rect(280, height_box, 360, offset - basket[3])
    fill(0, 166, 255, 255)
    rect(360, height_box, 440, offset - basket[4])
    fill(21, 0, 255, 255)
    rect(440, height_box, 520, offset - basket[5])
    fill(187, 0, 255, 255)
    rect(520, height_box, 600, offset - basket[6])   
    
    delay(300)
    

    
    
    
