import math
from rover import Rover
from environment import Tag, Environment

def detect_tag(env: Environment, rover: Rover):
    # if tag's global coordinates are within the range and fov of camera, 
    # return true, else false, None, None
    
    # Get tag and camera specs
    tag = env.get_tag_position()
    range, fov = rover.get_camera_specs()
    
    # Calculate distance to tag from the rover and relative angle of tag to rover heading
    distance = rover.distance_to(tag) 
    rel_angle = rover.angle_to(tag) - rover.get_heading()
    print("Rover's angle to tag: ", rover.angle_to(tag))
    print("Rover's heading: ", rover.get_heading())
    print("Relative angle: ", rel_angle)
    
    if distance <= range and abs(rel_angle) <= fov/2:
        return True, distance, rel_angle
    
    return False, None, None