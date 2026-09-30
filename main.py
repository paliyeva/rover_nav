from rover import Rover
from controller import navigate_to
import math

def main():
    my_rover = Rover(0, 0, math.pi/2)
    my_target = [10, 8]
    navigate_to(my_rover, my_target, 0.1, 0) 


if __name__ == "__main__":
    main()
