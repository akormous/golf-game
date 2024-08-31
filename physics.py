from ball import Ball
from constants import FRICTION_COEFFICIENT, GRAVITY
from utils import sign


class Physics:
    def __init__(self):
        pass

    # reduces the speed by a factor
    def damp(self, speed, factor):
        return sign(speed) * (abs(speed) - factor)

    # simulate friction on ball
    def simulate_friction_x(self, ball: Ball):
        ball.set_speed_x( ball.get_speed_x() * FRICTION_COEFFICIENT )

    # simulate gravity on ball
    def simulate_gravity_y(self, ball: Ball):
        ball.set_speed_y( ball.get_speed_y() + GRAVITY )

   
