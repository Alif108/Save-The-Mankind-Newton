import pygame
import random
import math


class Fruit:

    def __init__(self, fruit_path):
        self.fruitImg = pygame.image.load(fruit_path)
        self.fruitX = random.randint(0, 736)
        self.fruitY = random.randint(-20, 0)
        self.fruitY_change = round(random.uniform(0.5, 1.0), 2)

    def fruit_show(self, screen):
        screen.blit(self.fruitImg, (self.fruitX, self.fruitY))

    def check_position(self):
        if self.fruitY >= 480:
            self.fruitY = -75
            self.fruitX = random.randint(0, 736)

    def change_vertical(self):
        self.fruitY += self.fruitY_change

    def collision(self, player):
        dist = math.sqrt((self.fruitX - player.getX())**2 + (self.fruitY - player.getY())**2)

        if dist < 35:
            return True
        else:
            return False

    def resetFruit(self):
        self.fruitX = random.randint(0, 736)
        self.fruitY = random.randint(-20, 0)

    def getX(self):
        return self.fruitY

    def getY(self):
        return self.fruitY