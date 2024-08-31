from ball import Ball
from constants import COORD_X, COORD_Y, DAMP, RADIUS, SCREEN_LENGTH, WHITE, SCREEN_WIDTH
from physics import Physics


class Game:
    def __init__(self, terrain):
        self.ball = Ball(COORD_X, COORD_Y, RADIUS, WHITE)
        self.physics = Physics()
        self.terrain = terrain

    def simulate_physics(self):
        if self.is_out_of_bounds_x():
            print("STAY IN THE PLAY AREA!")

        if self.is_colliding(self.terrain):
            self.invert_speed_y()
            self.physics.simulate_friction_x(self.ball)
        else:
            self.physics.simulate_gravity_y(self.ball)


    # checks if ball is colliding with terrain
    def is_colliding(self, terrain) -> bool:
        if self.ball.y + self.ball.radius >= terrain.top:
            self.ball.y = terrain.top - self.ball.radius
            return True
        return False
 
    def invert_speed_y(self):
        if abs(self.ball.get_speed_y()) < DAMP:
            self.ball.set_speed_y(0)
        else:
            self.ball.set_speed_y( self.physics.damp(self.ball.get_speed_y(), DAMP) )
            self.ball.set_speed_y( -self.ball.get_speed_y() )

    def invert_speed_x(self):
        if abs(self.ball.get_speed_x()) < DAMP:
            self.ball.set_speed_x( 0 )
        else:
            self.ball.set_speed_x( self.physics.damp(self.ball.get_speed_x(), DAMP) )
            self.ball.set_speed_x(  -self.ball.get_speed_x() )


    def is_out_of_bounds_y(self):
        if self.ball.y - self.ball.radius < 0 or self.ball.y + self.ball.radius > SCREEN_LENGTH:
            return True
        return False
    
    def is_out_of_bounds_x(self):
        if self.ball.x - self.ball.radius < 0:
            self.ball.x = self.ball.radius
            self.invert_speed_x()
            return True
        elif self.ball.x + self.ball.radius > SCREEN_WIDTH:
            self.ball.x = SCREEN_WIDTH - self.ball.radius
            self.invert_speed_x()
            return True
        return False




