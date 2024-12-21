import pgzrun
import random

WIDTH = 600
HEIGHT = 400



circle_width = WIDTH // 2
circle_height = HEIGHT // 2
radius = circle_height // 2
def draw():
    global radius
    screen.clear()


  
    for i in range(10):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        
        screen.draw.circle((circle_width,circle_height),radius,(r,g,b))
        radius += 10
        
pgzrun.go()