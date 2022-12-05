import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    font = 100
    n = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((5, 50, 250))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    pygame.display.flip()
pygame.quit()
