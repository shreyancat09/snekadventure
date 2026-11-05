import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek Adventure")

clock = pygame.time.Clock()

player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_vel_x = 0
player_vel_y = 0
player_speed = 4

# TODO: load actual png assets later instead of plain rect
player_color = (80, 220, 120)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_vel_x = -player_speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_vel_x = player_speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_vel_y = -player_speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_vel_y = player_speed
                
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                player_vel_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_s):
                player_vel_y = 0

    player_x += player_vel_x
    player_y += player_vel_y

    screen.fill((15, 15, 25))
    kjdcn
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
