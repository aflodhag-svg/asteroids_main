import pygame; from constants import SCREEN_WIDTH, SCREEN_HEIGHT; from logger import log_state

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    TIME = 60
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
              return

        screen.fill(000000)
        pygame.display.flip()
        Clock.tick(TIME)
        dt = Clock.tick(TIME) / 1000



if __name__ == "__main__":
    main()
