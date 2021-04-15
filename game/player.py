import pygame


class Player:

    def __init__(self):
        self.PlayerImg = pygame.image.load('Images\isaac-newton.png')
        self.PlayerX = 370
        self.PlayerY = 480
        self.PlayerX_change = 0

    def show_player(self, screen):
        screen.blit(self.PlayerImg, (self.PlayerX, self.PlayerY))

    def left_x_change(self):
        self.PlayerX_change = -2

    def right_x_change(self):
        self.PlayerX_change = 2

    def change_horizontal(self):
        self.PlayerX += self.PlayerX_change

    def stop_moving(self):
        self.PlayerX_change = 0

    def check_position(self):
        if self.PlayerX <= 0:
            self.PlayerX = 0
        elif self.PlayerX >= 736:
            self.PlayerX = 736

    def getX(self):
        return self.PlayerX

    def getY(self):
        return self.PlayerY