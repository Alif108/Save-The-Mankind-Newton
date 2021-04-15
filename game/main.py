import pygame
from pygame import mixer
from player import Player
from fruit import Fruit
import random

pygame.init()

#setting up screen
screen = pygame.display.set_mode((800, 600))

#Icon and Title
pygame.display.set_caption('Save the Mankind Newton')
icon = pygame.image.load('Images\Icon.png')
pygame.display.set_icon(icon)

# Background Image
background_img = pygame.image.load('Images\Background (2).jpg')

#Sounds
bonk = mixer.Sound("Sound\Bonk.mp3")
ouch = mixer.Sound("Sound\ouch.mp3")
ouch_mofo = mixer.Sound("Sound\ouch_motherfucker.mp3")
hell_yeah = mixer.Sound("Sound\hell-yeah.mp3")
whistle = mixer.Sound("Sound\whistle.mp3")

#Score Text Position
textX = 10
textY = 10

#Font of Score
font = pygame.font.Font('freesansbold.ttf', 32)
score_value = 0

#Font of Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 50)

#Invented Text
invention = pygame.font.SysFont('Verdana', 30)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_coconut():
    over = over_font.render("NEWTON DIED", True, (0, 0, 0))
    screen.blit(over, (200, 250))
    over2 = over_font.render("SCORE: " + str(score_value), True, (0, 255, 0))
    screen.blit(over2, (235, 300))

def game_over_woman():
    over = over_font.render("YOU SPOILED NEWTON", True, (51, 51, 204))
    screen.blit(over, (100, 250))
    over2 = over_font.render("SCORE: " + str(score_value), True, (204, 0, 0))
    screen.blit(over2, (235, 300))

# def invented_text():
#     x = random.randint(0, 100) % 3
#     if x == 0:
#         text = "LAWS OF MOTION"
#     elif x == 1:
#         text = "CALCULUS"
#     else:
#         text = "REFLECTING TELESCOPE"
#
#     return invention.render(text, True, (255, 255, 0))



apple_no = 3
coconut_no = 2
woman_no = 2

woman_path = 'Images\Woman.png'
woman2_path = 'Images\Woman_2.png'
apple_path = 'Images\Apple.png'
coconut_path = 'Images\coconut.png'


newton = Player()
apples = []
coconuts = []
women = []

for i in range(apple_no):
    apple_obj = Fruit(apple_path)
    apples.append(apple_obj)

for i in range(coconut_no):
    coconut_obj = Fruit(coconut_path)
    coconuts.append(coconut_obj)

woman_obj = Fruit(woman_path)
women.append(woman_obj)
woman_obj2 = Fruit(woman2_path)
women.append(woman_obj2)

running = True
collide_woman = False
collide_coconut = False
# msg_time = 0

while running:

    # msg_time += 1
    screen.blit(background_img, (0, 0))

    if collide_coconut or collide_woman:                        # if collision with any of woman or coconut
        if collide_coconut:
            game_over_coconut()
        else:
            game_over_woman()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    collide_coconut = False
                    collide_woman = False
                    score_value = 0

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    newton.left_x_change()
                if event.key == pygame.K_RIGHT:
                    newton.right_x_change()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    newton.stop_moving()

        newton.change_horizontal()

        newton.check_position()

        # if msg_time < 100:
        #     text = invented_text()
        #     screen.blit(text, (370, 250))

        for apple in apples:
            if apple.collision(newton):
                bonk.play()
                hell_yeah.play()
                apple.resetFruit()
                score_value += 1
                msg_time = 0

            apple.check_position()
            apple.fruit_show(screen)
            apple.change_vertical()

        for coconut in coconuts:
            if coconut.collision(newton):
                bonk.play()
                ouch_mofo.play()

                for woman in women:
                    woman.resetFruit()                              # resetting all woman position

                for coconut in coconuts:
                    coconut.resetFruit()                            # resetting all coconut position
                    collide_coconut = True

                game_over_coconut()
                break

            coconut.check_position()
            coconut.fruit_show(screen)
            coconut.change_vertical()

        for woman in women:
            if woman.collision(newton):
                bonk.play()
                whistle.play()

                for coconut in coconuts:
                    coconut.resetFruit()

                for woman in women:
                    woman.resetFruit()
                    collide_woman = True

                game_over_woman()
                break

            woman.check_position()
            woman.fruit_show(screen)
            woman.change_vertical()

    show_score(textX, textY)
    newton.show_player(screen)
    pygame.display.update()