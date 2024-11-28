import pygame

pygame.init()   # Initialize all imported pygame modules
pygame.display.set_caption('Demo Pygame 01')  # Set the current window caption

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)  # Set the width and height of the screen

white = (255, 255, 255)  # Define some colors
blue = (0, 0, 255)

# Loop until the user clicks the close button.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(white)  # Fill the screen with white color

    center_x = size[0] // 2
    center_y = size[1] // 2
    radius = 50
    # Draw a circle on the screen
    pygame.draw.circle(screen, blue, (center_x, center_y), radius)

    # Flip the display
    pygame.display.flip()