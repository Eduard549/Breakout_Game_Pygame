import pygame
from paddle import Paddle
from ball import Ball
from wall import Brick

pygame.init()

WHITE = (255, 255, 255)
BG_COLOR = (70, 25, 89)
BRICK_COLORS = [
    (200, 0, 0),
    (0, 200, 0),
    (0, 0, 200),
    (200, 200, 0),
    (0, 200, 200)]
score = 0
lives = 3

width, height = (800, 600)

BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICKS_PER_ROW = 10
BRICK_ROWS = 4
horizontal_gap = 10
vertical_gap = 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")

all_sprites_list = pygame.sprite.Group()

ball = Ball()
ball.rect.x = 345
ball.rect.y = 300

paddle = Paddle()
paddle.rect.x = 350
paddle.rect.y = 560

all_bricks = pygame.sprite.Group()
ball_paddle_bricks = [ball, paddle, all_bricks]

for row in range(BRICK_ROWS):
    for col in range(BRICKS_PER_ROW):
        color_index = row % len(BRICK_COLORS)
        brick = Brick(
            col * BRICK_WIDTH + horizontal_gap,
            row * BRICK_HEIGHT + vertical_gap,
            color_index)
        all_bricks.add(brick)


all_sprites_list.add(ball_paddle_bricks)

running = True
clock = pygame.time.Clock()

#  Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break
        elif event.type == pygame.QUIT:
            running = False

    all_sprites_list.update()

    # if ball hits bottom wall - 1 life
    if ball.rect.y > 590:
        ball.rect.x = 345
        ball.rect.y = 300
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.time.wait(3000)
            running = False
    # collision with paddle
    if pygame.sprite.collide_mask(ball, paddle):
        if abs(ball.rect.bottom - paddle.rect.top) < 10 and ball.speed[1] > 0:
            ball.speed[1] = -ball.speed[1]
        else:
            ball.rect.x -= ball.speed[0]
            ball.rect.y -= ball.speed[1]
            ball.bounce()

    # collision with bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {str(score)}", 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render(f"Lives: {str(lives)}", 1, WHITE)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()