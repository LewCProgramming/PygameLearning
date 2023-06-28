import pygame
from sys import exit
import os

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LewGame')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load('./sky.png').convert()
ground_surface = pygame.image.load('./ground.png').convert()

scaled_sky_surface = pygame.transform.scale(sky_surface,(800,300))
scaled_ground_surface = pygame.transform.scale(ground_surface,(800,100))

#score_surface = test_font.render('This is LewGame', False, (64,200,0))
#score_rectangle = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('./Graphics/Enemies/snailWalk1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('./Graphics/Player/p1_walk/PNG/p1_walk01.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,305))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('./Graphics/Player/p1_front.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('LewGame', False, (85, 196, 100))
game_name_rectangle = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run.', False, ('red'))
game_message_rectangle = game_message.get_rect(center = (400, 320))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos):
                player_gravity = -20"""

        if event.type == pygame.KEYDOWN and player_rectangle.bottom >= 305 and game_active == True:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
                print('button')
                game_active = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks()/1000) 
     
    screen.blit(scaled_sky_surface,(0,0))
    screen.blit(scaled_ground_surface,(0,300))
    #pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
    #pygame.draw.rect(screen,'Blue',score_rectangle,2)
    #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(), 10)
    #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
    #screen.blit(score_surface,score_rectangle)
    display_score()
    
    if game_active:
        snail_rectangle.x -= 4
        if snail_rectangle.x <= 0:
            snail_rectangle.left = 800
        elif snail_rectangle.x > 800:
            snail_rectangle.right = 0
        screen.blit(snail_surface,snail_rectangle)

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 305:
            player_rectangle.bottom = 305
        screen.blit(player_surface,player_rectangle)

        # Collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill((50,100,160))
        screen.blit(player_stand, player_stand_rectangle)
        screen.blit(game_name, game_name_rectangle)
        screen.blit(game_message, game_message_rectangle)

    pygame.display.update()
    clock.tick(60)