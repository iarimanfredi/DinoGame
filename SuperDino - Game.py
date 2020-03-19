import pygame
from time import sleep

SCREEN_H = 480
SCREEN_W = 640
SCREEN_SIZE = (SCREEN_W, SCREEN_H)

COLOR_GREEN = (0, 200, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BROWN = (150, 75, 0)
COLOR_LIGHTBLUE = (0, 150, 255)
COLOR_VIOLET = (175, 0, 175)
COLOR_DARKGREEN = (0, 75, 0)

PLAYER_H = 20
PLAYER_W = 10
OBSTACLE_H = 20
OBSTACLE_W = 10
BAT_H = 5
BAT_W = 10

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial ms')
def write(surf, text, size, x, y, color):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)

class Entity():
	def __init__(self, x, y, h, w, color):
		self.x = x
		self.y = y
		self.h = height
		self.w = width
		self.color = color

class Player(Entity):
	def __init__(self, x, y, color, h, w):
		self.x = x
		self.y = y
		self.color = color
		self.h = h
		self.w = w
	
	def is_collision(self, ob, bt):
		invisible = False
		if ((self.x == ob.x) and self.y == ob.y or (self.x + PLAYER_W == ob.x) and self.y == ob.y) or ((self.x == bt.x) and self.y == bt.y or (self.x + PLAYER_W == bt.x) and self.y == bt.y):
			return True

	def draw(self):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
			
	def jump(self):
		self.y -= 20
		self.draw()
		pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(SCREEN_W / 2, self.y + PLAYER_H, PLAYER_W, 20))
		
	def land(self):
		self.y += 20
		self.draw()
		pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(SCREEN_W / 2, self.y - PLAYER_H, PLAYER_W, 20))
				

class Obstacle(Entity):
	def __init__(self, x, y, color, h, w):
		self.x = x
		self.y = y
		self.color = color
		self.h = h
		self.w = w

	def draw(self):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
		
	def slide(self):
		self.x -= ob_speed
		self.draw()
		pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(self.x + OBSTACLE_W, 450 - OBSTACLE_H, ob_speed, OBSTACLE_H))
		if self.x <= 0 - OBSTACLE_W:
			self.x = SCREEN_W


class Bat(Entity):
	def __init__(self, x, y, color, h, w):
		self.x = x
		self.y = y
		self.color = color
		self.h = h
		self.w = w

	def draw(self):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
		
	def fly(self):
		self.x -= bat_speed
		self.draw()
		pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(self.x + BAT_W, 410, bat_speed, BAT_H))
		if self.x <= 0 - BAT_W:
			self.x = SCREEN_W

#VELOCITà AMMESSE: 1, 2, 4, 5, 8, 10, 16, 20

bat_speed = 1	
ob_speed = 2
playing = True
counter = -1
player = Player(SCREEN_W / 2, 450 - PLAYER_H, COLOR_GREEN, PLAYER_H, PLAYER_W)
obstacle = Obstacle(SCREEN_W - OBSTACLE_W, 450 - OBSTACLE_H, COLOR_DARKGREEN, OBSTACLE_H, OBSTACLE_W)
bat = Bat(SCREEN_W - BAT_W, 410, COLOR_VIOLET, BAT_H, BAT_W)

while playing:
	counter += 1
	if counter >= 1200:
		ob_speed = 5
		bat_speed = 2
	if counter >= 1800:
		ob_speed = 8
		bat_speed = 4
	if counter >= 2500:
		ob_speed = 8
		bat_speed = 5
	if counter >= 3600:
		ob_speed = 10
		bat_speed = 8
	if counter >= 4200:
		ob_speed = 10
		bat_speed = 10
	if counter >= 5200:
		ob_speed = 16
		bat_speed = 16
	if counter >= 6200:
		ob_speed = 20
		bat_speed = 20
	screen.fill(COLOR_BLACK)
	pygame.draw.rect(screen, COLOR_LIGHTBLUE, pygame.Rect(0, 0, SCREEN_W, 400))
	pygame.draw.rect(screen, COLOR_BROWN, pygame.Rect(0, 450, SCREEN_W, 30))
	pygame.draw.rect(screen, COLOR_WHITE, pygame.Rect(0, 450, SCREEN_W, 1))
	pygame.draw.rect(screen, COLOR_WHITE, pygame.Rect(0, 400, SCREEN_W, 1))
	write(screen, str(counter), 20, 600, 30, COLOR_WHITE)
	player.draw()
	obstacle.draw()
	obstacle.slide()
	bat.draw()
	bat.fly()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if player.y != 410:
					player.jump()
			if event.key == pygame.K_DOWN:
				if player.y != 430:
					player.land()
	if player.is_collision(obstacle, bat):
		playing = False	

	pygame.display.flip()
	clock.tick(60)

screen.fill(COLOR_BLACK)
write(screen, 'YOU DIED! YOUR SCORE: {}'.format(counter), 20, SCREEN_W / 2, 200, COLOR_WHITE)
pygame.display.flip()
sleep(3)
quit()