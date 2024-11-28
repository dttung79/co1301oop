import pygame
from game_base import Game
import random as rd

class DemoGame(Game):
    def __init__(self, title, width, height, bg_color):
        super().__init__(title, width, height, bg_color)
        self.circle_radius = rd.randint(50, 100)
        self.circle_x = rd.randint(self.circle_radius, self.width - self.circle_radius)
        self.circle_y = rd.randint(self.circle_radius, self.height - self.circle_radius)
        self.circle_color = self.random_color()

        self.rect_width = rd.randint(50, 100)
        self.rect_height = rd.randint(50, 100)
        self.rect_x = rd.randint(0, self.width - self.rect_width)   # x coordinate of the top left
        self.rect_y = rd.randint(0, self.height - self.rect_height) # y coordinate of the top left
        self.rect_color = self.random_color()

    def draw(self):
        self.draw_circle(self.circle_x, self.circle_y, self.circle_radius, self.circle_color)
        self.draw_rect(self.rect_x, self.rect_y, self.rect_width, self.rect_height, self.rect_color)
        self.draw_line()
    
    def random_color(self):
        red = rd.randint(0, 255)
        green = rd.randint(0, 255)
        blue = rd.randint(0, 255)
        return (red, green, blue)

    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def draw_rect(self, x, y, w, h, color):
        pygame.draw.rect(self.screen, color, (x, y, w, h))

    def draw_line(self):
        x1 = rd.randint(0, self.width)
        y1 = rd.randint(0, self.height)
        x2 = rd.randint(0, self.width)
        y2 = rd.randint(0, self.height)
        color = self.random_color()
        pygame.draw.line(self.screen, color, (x1, y1), (x2, y2), 5)

if __name__ == '__main__':
    white = (255, 255, 255)
    game = DemoGame('Demo Pygame 02', 800, 600, white)
    game.run()
    pygame.quit()