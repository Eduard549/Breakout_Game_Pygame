import pygame
from random import randint

BALL_RADIUS = 15
BALL_COLOR = (255, 255, 255)
BALL_SPEED_X = 4
BALL_SPEED_Y = -4
width, height = (800, 600)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.radius = BALL_RADIUS

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = [BALL_SPEED_X, BALL_SPEED_Y]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 40:
            self.speed[1] = -self.speed[1]

    def bounce(self):
            self.speed[0] = -self.speed[0]
            self.speed[1] = randint(-8, 8)