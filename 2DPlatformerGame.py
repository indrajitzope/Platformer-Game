import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Player properties
player_width, player_height = 50, 50
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150
player_speed = 5
player_velocity_y = 0
gravity = 0.8
jump_strength = -15

# Ground and platforms
ground = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
platforms = [
    pygame.Rect(200, 400, 200, 20),
    pygame.Rect(500, 300, 200, 20)
]

# Game loop variables
running = True
on_ground = False

# Main game loop
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = jump_strength
        on_ground = False
    
    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y
    
    # Check collisions with ground
    if player_y + player_height >= SCREEN_HEIGHT - 50:
        player_y = SCREEN_HEIGHT - 50 - player_height
        player_velocity_y = 0
        on_ground = True

    # Check collisions with platforms
    for platform in platforms:
        if (
            player_x + player_width > platform.x and
            player_x < platform.x + platform.width and
            player_y + player_height > platform.y and
            player_y + player_height - player_velocity_y <= platform.y
        ):
            player_y = platform.y - player_height
            player_velocity_y = 0
            on_ground = True
    
    # Draw ground and platforms
    pygame.draw.rect(screen, GREEN, ground)
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)

    # Draw player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, BLACK, player_rect)
    
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
