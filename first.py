import pygame


def draw(screen):

    screen.fill((0, 0, 0))
    # nn = width / n
    white = (255, 255, 255)
    z = 0
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
    while w > z:
        pygame.draw.circle(screen, colors[z % 3], (w, w), w - z * w)
        z = z + 1
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    inp = [int(a) for a in input().split()]
    w = inp[0]
    n = inp[1]
    height = w * n
    print(height)
    width = height
    size = height, width
    assert str(height).isdigit(), "Неправильный формат ввода"
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
