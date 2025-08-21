import pygame
import sys

pygame.init()

# --- Настройки окна ---
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид v2")

# --- Цвета ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

# --- Шрифт ---
font = pygame.font.SysFont("Arial", 20)

# --- Платформа ---
paddle = pygame.Rect(WIDTH//2 - 50, HEIGHT - 20, 100, 10)
paddle_speed = 7

# --- Мяч ---
ball = pygame.Rect(WIDTH//2 - 7, HEIGHT//2 - 7, 14, 14)
ball_speed = [4, -4]

# --- Блоки ---
blocks = []
block_width, block_height = 60, 20
for row in range(5):
    for col in range(8):
        block = pygame.Rect(10 + col * (block_width + 10), 40 + row * (block_height + 5), block_width, block_height)
        blocks.append(block)

# --- Счет и жизни ---
score = 0
lives = 3

clock = pygame.time.Clock()

# --- Игровой цикл ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(paddle_speed, 0)

    # Движение мяча
    ball.move_ip(ball_speed)

    # Столкновения со стенами
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Столкновение с платформой
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Столкновение с блоками
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        del blocks[hit_index]
        ball_speed[1] = -ball_speed[1]
        score += 10

    # Проверка проигрыша
    if ball.bottom >= HEIGHT:
        lives -= 1
        if lives == 0:
            print("GAME OVER")
            pygame.quit()
            sys.exit()
        else:
            ball.x, ball.y = WIDTH//2, HEIGHT//2
            ball_speed = [4, -4]

    # Отрисовка
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # Текст
    score_text = font.render(f"Score: {score}", True, GREEN)
    lives_text = font.render(f"Lives: {lives}", True, GREEN)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(60)
