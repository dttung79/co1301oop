# draw a circle moving on x-axis
import pygame
from game_base import Game

class MovingCircle(Game):
    def __init__(self, title, width, height, bg_color):
        super().__init__(title, width, height, bg_color)
        self.circle_radius = 50
        self.circle_x = width // 2
        self.circle_y = height // 2
        self.circle_color = (0, 0, 255)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.circle_x -= 10
            elif event.key == pygame.K_RIGHT:
                self.circle_x += 10
            elif event.key == pygame.K_UP:
                self.circle_y -= 10
            elif event.key == pygame.K_DOWN:
                self.circle_y += 10
                
    def draw(self):
        self.draw_circle(self.circle_x, self.circle_y, self.circle_radius, self.circle_color)

    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.screen, color, (x, y), radius)

if __name__ == '__main__':
    white = (255, 255, 255)
    game = MovingCircle('Moving Circle', 800, 600, white)
    game.run()
    pygame.quit()