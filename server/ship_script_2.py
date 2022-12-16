#just some test
import math
n = 0
center_x = 1000
center_y = 1000

def cycle():
    global n
    x = center_x + math.cos(n)*500
    y = center_y + math.cos(n)*500
    n += 0.1
    
    return {"x":x, "y":y}
