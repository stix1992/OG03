import pygame
import random
import time

pygame.init()

score = 0
font = pygame.font.Font(None, 36)
start_time = time.time()
game_duration = 30  # seconds

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

hit_sound = pygame.mixer.Sound('sound/damage.mp3')
mis_sound = pygame.mixer.Sound('sound/missing.mp3')
final_sound = pygame.mixer.Sound('sound/final.mp3')

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/target_icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
original_target_image = target_image.copy()
target_width = target_image.get_width()
target_height = target_image.get_height()

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    current_time = time.time()
    elapsed_time = current_time - start_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mis_sound.play()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hit_sound.play()

                score += 1
                if target_width > 20:
                    target_width -= 2
                    target_height -= 2
                    target_image = pygame.transform.smoothscale(original_target_image, (target_width, target_height))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    time_left = max(0, int(game_duration - elapsed_time))
    timer_text = font.render(f"Time: {time_left}", True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH - 120, 10))
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

    if elapsed_time > game_duration:
        running = False

screen.fill(BLACK)
final_sound.play()
game_over_text = font.render("Game Over!", True, WHITE)
final_score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
pygame.display.update()
time.sleep(5)

pygame.quit()
