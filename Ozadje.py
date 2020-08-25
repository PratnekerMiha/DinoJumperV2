import pygame
import random

class Ozadje(pygame.sprite.Sprite):
	def __init__(self, WIDTH=640, HEIGHT=500):
		pygame.sprite.Sprite.__init__(self)
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.speed = 5
		self.imgs = ['./pics/bg/bg1.png', './pics/bg/bg2.png', './pics/bg/bg3.png']
		self.reset()
	def move(self):
		self.x = self.x - self.speed
	def draw(self, screen):
		if self.bg1_rect.right < 0:
			self.x = 0
			self.bg1 = self.bg2
			self.bg1_rect = self.bg2_rect
			self.bg2 = self.bg3
			self.bg2_rect = self.bg3_rect
			self.bg3 = pygame.image.load(self.imgs[random.randint(0, 2)]).convert_alpha()
			self.bg3_rect = self.bg3.get_rect()
		self.bg1_rect.left, self.bg1_rect.top = self.x, int(self.HEIGHT/2.3)
		self.bg2_rect.left, self.bg2_rect.top = self.bg1_rect.right, int(self.HEIGHT/2.3)
		self.bg3_rect.left, self.bg3_rect.top = self.bg2_rect.right, int(self.HEIGHT/2.3)
		screen.blit(self.bg1, self.bg1_rect)
		screen.blit(self.bg2, self.bg2_rect)
		screen.blit(self.bg3, self.bg3_rect)
	def reset(self):
		self.x = 0
		self.bg1 = pygame.image.load(self.imgs[0]).convert_alpha()
		self.bg2 = pygame.image.load(self.imgs[1]).convert_alpha()
		self.bg3 = pygame.image.load(self.imgs[2]).convert_alpha()
		self.bg1_rect = self.bg1.get_rect()
		self.bg2_rect = self.bg2.get_rect()
		self.bg3_rect = self.bg3.get_rect()
		self.bg1_rect.left, self.bg1_rect.top = self.x, int(self.HEIGHT / 2.3)
		self.bg2_rect.left, self.bg2_rect.top = self.bg1_rect.right, int(self.HEIGHT / 2.3)
		self.bg3_rect.left, self.bg3_rect.top = self.bg2_rect.right, int(self.HEIGHT / 2.3)