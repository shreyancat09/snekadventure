import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek Adventure")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
score_font = pygame.font.SysFont(None, 32)

player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - 120
player_vel_x = 0
player_vel_y = 0
player_speed = 5
player_color = (80, 220, 120)

obs_width, obs_height = 40, 40
obs_x = random.randint(0, WIDTH - obs_width)
obs_y = -50
obs_vel_y = 4
obs_color = (230, 60, 80)

game_state = 1
score = 0
score_timer = 0

def check_collision():
    return (player_x < obs_x + obs_width and
            player_x + player_width > obs_x and
            player_y < obs_y + obs_height and
            player_y + player_height > obs_y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_state == 1:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    player_vel_x = -player_speed
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player_vel_x = player_speed
                if event.key in (pygame.K_UP, pygame.K_w):
                    player_vel_y = -player_speed
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    player_vel_y = player_speed
            elif game_state == 2:
                if event.key == pygame.K_r:
                    game_state = 1
                    score = 0
                    score_timer = 0
                    player_x = WIDTH // 2
                    player_y = HEIGHT - 120
                    obs_y = -50
                    obs_vel_y = 4
                    obs_x = random.randint(0, WIDTH - obs_width)
                
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                player_vel_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_s):
                player_vel_y = 0

    if game_state == 1:
        player_x += player_vel_x
        player_y += player_vel_y

        obs_y += obs_vel_y
        if obs_y > HEIGHT:
            obs_y = -50
            obs_x = random.randint(0, WIDTH - obs_width)
            score += 10

        score_timer += 1
        if score_timer >= 30:
            score += 1
            score_timer = 0

        obs_vel_y = 4 + (score // 50)

        if check_collision():
            game_state = 2
            player_x, player_y = 1000, 1000
            player_vel_x, player_vel_y = 0, 0
            obs_x, obs_y = 1000, 1000
            obs_vel_y = 0

    screen.fill((15, 15, 25))

    if game_state == 1:
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, obs_color, (obs_x, obs_y, obs_width, obs_height))
        
        score_surface = score_font.render(f"Score: {score}", True, (240, 240, 240))
        screen.blit(score_surface, (20, 20))

    elif game_state == 2:
        game_over_text = font.render("GAME OVER - Press R to Restart", True, (230, 60, 80))
        final_score_text = score_font.render(f"Final Score: {score}", True, (240, 240, 240))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
