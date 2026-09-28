import math

class Rover: 
    SPEED = 1
    DELTA_T = 0.1
    epsilon = 0.1
    
    def __init__(self, x, y, theta, v, omega):
        self.x = x              # x position
        self.y = y              # y position
        self.theta = theta      # heading
        self.v = v              # velocity
        self.omega = omega      # angular velocity

    def find_target(self, x_target, y_target):
        self.theta = math.atan2(y_target - self.y, x_target - self.x)
        t = 0
        while self.euclidian_distance(x_target-self.x, y_target-self.y) > self.epsilon:
            self.advance(self.SPEED, self.DELTA_T)
            t += self.DELTA_T
            print(t, self.x, self. y)
            if (self.x > 50 or self.y> 50):
                return 0
        return t

    def advance(self, v, delta_t):
        self.x += (v * math.cos(self.theta)) * delta_t
        self.y += (v * math.sin(self.theta)) * delta_t
        # angular rate later when search is introduced

    def euclidian_distance(self, x, y):
        return math.sqrt(x**2 + y**2)

    
