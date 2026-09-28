from rover import Rover
import math

def main():
    my_rover = Rover(0, 0, math.pi/2, 3, 0)
    time = my_rover.find_target(8, 5)
    print(time)


if __name__ == "__main__":
    main()
