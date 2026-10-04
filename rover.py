import math

class Camera:
    def __init__(self, range, fov):
        self.range = range  # range of vision (in distance units)
        self.fov = fov      # field of vision (in angles)
    
    def get_range(self):
        return self.range
    
    def get_fov(self):
        return self.fov

class Rover: 
    
    def __init__(self, x, y, theta, camera: Camera):
        self.x = x                                                  # x position
        self.y = y                                                  # y position
        self.theta = (theta + math.pi) % (2 * math.pi) - math.pi    # heading [-180, 180]
        self.camera = camera                                        # camera 

    def move(self, v, omega, dt = 0.1):
        self.x += (v * math.cos(self.theta)) * dt
        self.y += (v * math.sin(self.theta)) * dt
        self.theta += omega * dt
        
    def distance_to(self, target):
        x_target, y_target = target
        return math.hypot(self.x - x_target, self.y - y_target)
    
    def angle_to(self, target):
        x_target, y_target = target
        return math.atan2(y_target-self.y, x_target - self.x)    
    
    def get_position(self):
        return self.x, self.y
    
    def get_heading(self):
        return self.theta
    
    def get_camera_specs(self):
        camera = self.camera
        return camera.get_range(), camera.get_fov()
    
    def set_heading(self, theta):
        self.theta = theta
    
    

    
