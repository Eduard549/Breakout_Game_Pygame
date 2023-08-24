import pygame
from random import randint

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_COLOR = (255, 255, 255)
PADDLE_SPEED = 10
width, height = (800, 600)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(PADDLE_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = (width - self.width) // 2
        self.rect.y = height - self.height - 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PADDLE_SPEED
        self.rect.x = max(min(self.rect.x, width - self.width), 0)
