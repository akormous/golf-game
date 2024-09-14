import math
from constants import SCREEN_WIDTH
import pygame

def sign(num: int):
    return (num > 0) - (num < 0)


def draw_dotted_line(surface, start_pos, end_pos, color, initial_dot_radius=8, spacing=15):
    direction = end_pos - start_pos
    distance = direction.length()

    if distance > 0:
        direction = direction.normalize()
        num_dots = int(distance / spacing)
        for i in range(num_dots):
            dot_pos = start_pos + direction * (i * spacing)
            # The radius of the dots decreases as the distance increases
            dot_radius = max(2, initial_dot_radius * (1 - i / num_dots))
            pygame.draw.circle(surface, color, (int(dot_pos.x), int(dot_pos.y)), int(dot_radius))


