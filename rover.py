import math

class Rover: 
    
    def __init__(self, x, y, theta):
        self.x = x              # x position
        self.y = y              # y position
        self.theta = theta      # heading

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
    
    # def euclidian_dist(x, y):
    #     return math.sqrt(x**2 + y**2)
    
    def get_position(self):
        return self.x, self.y
    
    def get_heading(self):
        return self.theta
    
    def set_heading(self, theta):
        self.theta = theta

    
