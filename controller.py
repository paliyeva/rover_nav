import math
from rover import Rover

def navigate_to(rover: Rover, target, v, omega, epsilon=0.1):
    new_theta = rover.angle_to(target)
    rover.set_heading(new_theta)
    t = 0
    while (rover.distance_to(target) > epsilon):
        rover.move(v, omega)
        t += 0.1
    return t




    