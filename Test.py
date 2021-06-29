import rotatescreen
import time
screen = rotatescreen.get_primary_display()

i=0

while True:
    screen.rotate_to(i*90 % 360)
    i=i+1

