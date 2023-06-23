import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks()
    current_time = round(current_time/1000)
    score_surface = test_font.render(f'{current_time}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LewGame')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

sky_surface = pygame.image.load('Desktop/Code Folder/PygameLearning/sky.png').convert()
ground_surface = pygame.image.load('Desktop/Code Folder/PygameLearning/ground.png').convert()

scaled_sky_surface = pygame.transform.scale(sky_surface,(800,300))
scaled_ground_surface = pygame.transform.scale(ground_surface,(800,100))

#score_surface = test_font.render('This is LewGame', False, (64,200,0))
#score_rectangle = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('Desktop/Code Folder/PygameLearning/Graphics/Enemies/snailWalk1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('Desktop/Code Folder/PygameLearning/Graphics/Player/p1_walk/PNG/p1_walk01.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,305))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos):
                player_gravity = -20"""

        if event.type == pygame.KEYDOWN and player_rectangle.bottom >= 305:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                snail_rectangle.left = 800
    
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
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)