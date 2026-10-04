import math
from rover import Rover, Camera
from environment import Tag, Environment

from controller import navigate_to
from perception import detect_tag

def main():
    tag = Tag(0, 0)
    env = Environment(tag)
    camera = Camera(3, math.pi/2)
    rover = Rover (3, 3, 3*math.pi/2, camera)
    print(detect_tag(env, rover))
if __name__ == "__main__":
    main()
