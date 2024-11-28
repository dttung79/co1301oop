import pygame

class Game:
    def __init__(self, title, width, height, bg_color):
        pygame.init()
        pygame.display.set_caption(title)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                # handle other events (sub class will override this method)
                self.handle_event(event)    
            
            self.screen.fill(self.bg_color)
            # draw the game objects (sub class will override this method)
            self.draw()       
            # tick the clock
            pygame.time.Clock().tick(60)
            # flip the display
            pygame.display.flip()

    def handle_event(self, event):
        pass

    def draw(self):
        pass

if __name__ == '__main__':
    white = (255, 255, 255)
    game = Game('Demo Pygame 01', 800, 600, white)
    game.run()
    pygame.quit()