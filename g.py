import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Target properties
target_wight = 50
target_height = 50
target_image = pygame.Surface((target_wight, target_height))
target_image.fill(WHITE)

# Initial target position
target_x = random.randint(0, SCREEN_WIDTH - target_wight)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hit the Target!')

# Score and timer
score = 0
font = pygame.font.Font(None, 36)
start_time = time.time()
game_duration = 30  # seconds

# Sound effect
hit_sound = pygame.mixer.Sound('sound/damage.mp3')

running = True
while running:
    screen.fill(BLACK)
    current_time = time.time()
    elapsed_time = current_time - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_wight and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_wight)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1
                hit_sound.play()
                # Increase difficulty
                if target_wight > 20:
                    target_wight -= 1
                    target_height -= 1
                    target_image = pygame.Surface((target_wight, target_height))
                    target_image.fill(WHITE)

    # Draw target
    screen.blit(target_image, (target_x, target_y))

    # Draw score and timer
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    time_left = max(0, int(game_duration - elapsed_time))
    timer_text = font.render(f"Time: {time_left}", True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH - 120, 10))

    pygame.display.update()

    # Check for game over
    if elapsed_time > game_duration:
        running = False

# Game over screen
screen.fill(BLACK)
game_over_text = font.render("Game Over!", True, WHITE)
final_score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
pygame.display.update()
time.sleep(5)

pygame.quit()
