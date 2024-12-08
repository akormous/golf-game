
# SCREEN SIZE
class Screen:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

# COLORS
class Colors:
    SKY = (133, 202, 237)
    WHITE = (255, 255, 255)
    GRASS = (49, 145, 65)
    BLACK = (0, 0, 0)
    YELLOW = (255, 225, 0)
    RED = (184, 0, 31)
    ALPHA = (0, 255, 0)

# BALL
class BallConstants:
    # RADIUS
    RADIUS = 20
    # DEFAULT SPAWN COORDINATES
    COORD_X = 2*RADIUS
    COORD_Y = RADIUS + 100
    # INITIAL SPEED
    SPEED_X = 20 
    SPEED_Y = 1 

# PHYSICS
class Physics:
    GRAVITY = 0.8
    FRICTION_COEFFICIENT = 0.6
    DAMP = 0.97
    JUMP = 64

# PLATFORM
class Platform:
    HEIGHT = 100
    WIDTH = Screen.SCREEN_WIDTH
    HALF_WIDTH = Screen.SCREEN_WIDTH/2
    POS_Y_DEFAULT = 980
    POS_X_DEFAULT = 0