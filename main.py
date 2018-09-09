import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Safnarinn")
clock = pygame.time.Clock()

def things_cought(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Cought: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def things_lost(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Lost: " + str(count), True, black)
    gameDisplay.blit(text, (0, 40))

def quit_game():
    pygame.quit()
    quit()

def player(player_x, player_y, player_w, player_h):
    pygame.draw.rect(gameDisplay, red, [player_x, player_y, player_w, player_h])

def things(thing_x, thing_y, thing_width, thing_height):
    pygame.draw.rect(gameDisplay, blue, [thing_x, thing_y, thing_width, thing_height])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)


def game_loop():
    game_over = False
    player_length = 100
    player_height = 20
    player_x = (display_width * 0.45)
    player_y = (display_height * 0.8)
    player_move = 0
    #player = pygame.Rect(player_x, player_y, player_length, 20)
    #screen_rect = gameDisplay.get_rect()

    #player
    #current position
    x_position = (display_width * 0.45)
    y_position = (display_height * 0.8)


    thing_width = 100
    thing_start_x = random.randrange(0, display_width - thing_width)
    thing_start_y = -600
    thing_height = 100
    thing_speed = 6.5

    cought = 0
    lost = 0


    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if lost == 3:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_move = -7
                elif event.key == pygame.K_RIGHT:
                    player_move = 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_move = 0

        player_x += player_move

        #test player
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.move_ip(6, 0)
        if keys[pygame.K_LEFT]:
            player.move_ip(-6, 0)
        player.clamp_ip(screen_rect)#passar að leikmaður fari ekki út fyrir"""

        gameDisplay.fill(white)

        """pygame.draw.rect(gameDisplay, red, player)"""

        player(player_x, player_y, player_length, player_height)
        things(thing_start_x, thing_start_y, thing_width, thing_height)
        thing_start_y += thing_speed




        if player_y < thing_start_y + thing_height:
            print("y crossover")

            if player_x > thing_start_x and player_x < thing_start_x + thing_width or player_x + player_length > thing_start_x and player_x + player_length < thing_start_x + thing_width or player_x < thing_start_x and player_x + player_length > thing_start_x + thing_width:
                print("x crossover")
                thing_start_y = 0 - thing_height
                thing_start_x = random.randrange(0, display_width)
                cought += 1
                player_length += 5

        #checks if object passes player
        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            lost += 1

        #current border check
        if player_x <= 0:
            player_move = 0

        if (player_x + player_length) >= display_width:
            player_move = 0



        """if player_y < thing_start_y + display_height:
            print("y corssover")

            if player_x > thing_start_x and player_x < thing_start_x + thing_width or player_x + player_length > thing_start_x and player_x + player_length < thing_start_x + thing_width:
                print("x crossover")
                thing_start_y = 0 - thing_height
                thing_start_x = random.randrange(0, display_width)
                cought += 1
                player_length = player_length + 5"""


        if player_length >= display_width * 0.75:
            game_over = True
            message_display("You Win!")

        things_cought(cought)
        things_lost(lost)

        pygame.display.update()
        clock.tick(60)
game_loop()
time.sleep(2)
pygame.quit()
quit()