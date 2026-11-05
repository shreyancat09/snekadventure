import pygame
import random
from settings import WIDTH, HEIGHT, PLAYER_COLOR, OBSTACLE_COLOR, POWERUP_COLOR

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = WIDTH // 2
        self.y = HEIGHT - 120
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.color = PLAYER_COLOR

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x < 0: self.x = 0
        if self.x > WIDTH - self.width: self.x = WIDTH - self.width

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Obstacle:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -50
        self.speed = 4
        self.color = OBSTACLE_COLOR

    def update(self, speed_multiplier):
        self.y += self.speed * speed_multiplier
        if self.y > HEIGHT:
            self.y = -50
            self.x = random.randint(0, WIDTH - self.width)
            return True 
        return False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
