import pygame
import sys
import math

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
COLORS = [BG_COLOR, BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY]

# Variables
drawing = False
last_pos = None
radius = 10
color = BLACK
bg_color = BG_COLOR

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint")
screen.fill(BG_COLOR)

# Draw shapes functions
def draw_square(pos, side_length):
    pygame.draw.rect(screen, color, (pos[0], pos[1], side_length, side_length))

def draw_right_triangle(pos, base_length, height):
    points = [(pos[0], pos[1]), (pos[0] + base_length, pos[1]), (pos[0] + base_length, pos[1] + height)]
    pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(pos, side_length):
    height = side_length * math.sqrt(3) / 2
    points = [(pos[0] + side_length / 2, pos[1]), (pos[0], pos[1] + height), (pos[0] + side_length, pos[1] + height)]
    pygame.draw.polygon(screen, color, points)

def draw_rhombus(pos, side_length, angle):
    angle_rad = math.radians(angle)
    half_diag_length = side_length / math.sqrt(2)
    points = [
        (pos[0] + side_length / 2, pos[1] - half_diag_length),
        (pos[0] + side_length, pos[1]),
        (pos[0] + side_length / 2, pos[1] + half_diag_length),
        (pos[0], pos[1])
    ]
    rotated_points = []
    for point in points:
        dx = point[0] - (pos[0] + side_length / 2)
        dy = point[1] - (pos[1])
        rotated_x = dx * math.cos(angle_rad) - dy * math.sin(angle_rad) + (pos[0] + side_length / 2)
        rotated_y = dx * math.sin(angle_rad) + dy * math.cos(angle_rad) + (pos[1])
        rotated_points.append((rotated_x, rotated_y))
    pygame.draw.polygon(screen, color, rotated_points)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
                    rect_width = 2 * radius
                    pygame.draw.rect(screen, bg_color, (event.pos[0] - radius, event.pos[1] - radius, rect_width, rect_width))
                else:
                    pygame.draw.circle(screen, color, event.pos, radius)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                radius = 10
            elif event.key == pygame.K_c:
                color = COLORS[(COLORS.index(color) + 1) % len(COLORS)]
            elif event.key == pygame.K_e:
                color = bg_color
            elif event.key == pygame.K_ESCAPE:
                screen.fill(BG_COLOR)
            elif event.key == pygame.K_s:  # Draw square
                draw_square(pygame.mouse.get_pos(), 50)
            elif event.key == pygame.K_t:  # Draw right triangle
                draw_right_triangle(pygame.mouse.get_pos(), 50, 50)
            elif event.key == pygame.K_u:  # Draw equilateral triangle
                draw_equilateral_triangle(pygame.mouse.get_pos(), 50)
            elif event.key == pygame.K_i:  # Draw rhombus
                draw_rhombus(pygame.mouse.get_pos(), 50, 45)

    # Update the display
    pygame.display.flip()
