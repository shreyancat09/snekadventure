import pygame
import os
from settings import *
from entities import Player, Obstacle

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek Adventure Extended")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 32)

def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            try:
                return int(f.read())
            except:
                return 0
    return 0

def save_high_score(score):
    current_high = load_high_score()
    if score > current_high:
        with open("highscore.txt", "w") as f:
            f.write(str(score))

player = Player()
obstacles = [Obstacle() for _ in range(3)] 

game_state = 0 # 0: Menu, 1: Playing, 2: Game Over
score = 0
high_score = load_high_score()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == 0:
                if event.key == pygame.K_SPACE:
                    game_state = 1
                    score = 0
                    player = Player()
                    obstacles = [Obstacle() for _ in range(3)]
            elif game_state == 1:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    player.vel_x = -player.speed
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player.vel_x = player.speed
            elif game_state == 2:
                if event.key == pygame.K_r:
                    game_state = 1
                    score = 0
                    player = Player()
                    obstacles = [Obstacle() for _ in range(3)]

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                player.vel_x = 0

    if game_state == 1:
        player.update()
        score += 1

        speed_mult = 1.0 + (score // 500) 
        player_rect = player.get_rect()
        for obs in obstacles:
            if obs.update(speed_mult):
                score += 10
            if player_rect.colliderect(obs.get_rect()):
                game_state = 2
                save_high_score(score // 10)
                high_score = load_high_score()

    screen.fill(BG_COLOR)

    if game_state == 0:
        title = font.render("SNEK ADVENTURE", True, TEXT_COLOR)
        prompt = small_font.render("Press SPACE to Start", True, PLAYER_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 10))

    elif game_state == 1:
        player.draw(screen)
        for obs in obstacles:
            obs.draw(screen)

        score_surface = small_font.render(f"Score: {score // 10}", True, TEXT_COLOR)
        screen.blit(score_surface, (20, 20))

    elif game_state == 2:
        go_text = font.render("GAME OVER", True, OBSTACLE_COLOR)
        sub_text = small_font.render(f"Final Score: {score // 10}", True, TEXT_COLOR)
        hs_text = small_font.render(f"High Score: {high_score}", True, PLAYER_COLOR)
        restart_text = small_font.render("Press R to Restart", True, TEXT_COLOR)

        screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, HEIGHT // 2 - 80))
        screen.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2 - 20))
        screen.blit(hs_text, (WIDTH // 2 - hs_text.get_width() // 2, HEIGHT // 2 + 20))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 70))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
