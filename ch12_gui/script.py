import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Example")
clock = pygame.time.Clock()

x, y, dx, dy, r = 300, 200, 4, 3, 24
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((20, 24, 40))
    pygame.draw.circle(screen, (233, 30, 99), (x, y), r)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()