import pygame
BRICK_COLORS = [
    (200, 0, 0),
    (0, 200, 0),
    (0, 0, 200),
    (200, 200, 0),
    (0, 200, 200)]


class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y, color_index):
        super().__init__()

        self.width = 60
        self.height = 20
        self.color = BRICK_COLORS[color_index]

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
