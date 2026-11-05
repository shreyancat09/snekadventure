import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek Adventure")

clock = pygame.time.Clock()

# TODO: organize into proper game states later
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
