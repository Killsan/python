import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

player_pos = [400, 300]
player_size_x = 50
player_size_y = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			x = player_pos[0]
			y = player_pos[1]
			if event.key == pygame.K_LEFT:
				x -= 10
			elif event.key == pygame.K_RIGHT:
				x += 10
			player_pos = (x, y)


		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((0,0,0))
	pygame.draw.rect(screen, (255,0,0), (player_pos[0], player_pos[1], player_size_x, player_size_y)) # red fucking square


	pygame.display.update()