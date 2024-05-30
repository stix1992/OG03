import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_wight, target_height = 80, 80

target_x = random.randint(0, SCREEN_WIDTH - target_wight)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

running = True
while running:
    pass

pygame.quit()
