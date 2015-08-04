import pygame
from pygame.locals import *
from random import randint

WIDTH = 640
HEIGHT = 480

freezing = 1
apple_count = 0
score = 0
is_apple = 0

pygame.init()
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eat the apples !")
bg = pygame.image.load("background.jpg").convert()
fenetre.blit(bg, (0,0))

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.x = 100
position_perso.y = 100
fenetre.blit(perso, position_perso)

pygame.key.set_repeat(1, 20)

class Apple(object):
    def __init__(self):
        self.apple = pygame.image.load("apple.png").convert_alpha()
        self.apple_rect = self.apple.get_rect()
        self.apple_rect.x = randint(0, WIDTH - 100)
        self.apple_rect.y = randint(0, HEIGHT - 100)

while freezing == 1:
    if is_apple == 0:
        apple = Apple()
        is_apple = 1
    fps = pygame.time.Clock().tick(30) #30 fps
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render("FPS: %s" % fps, True, (255, 255, 255))
    textrect = text.get_rect()
    
    score_font = pygame.font.SysFont(None, 20)
    score_text = basicfont.render("Score: %s" % score, True, (255, 255, 255))
    score_text_rect = score_text.get_rect()
    score_text_rect.x = 0
    score_text_rect.y = 450               
    
    for event in pygame.event.get():
        if event.type == QUIT:
            freezing = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                freezing = 0
            if event.key == K_DOWN:
                if position_perso.y < (HEIGHT - 90):
                    position_perso = position_perso.move(0, 10)
            if event.key == K_UP:
                if position_perso.y > 0:
                    position_perso = position_perso.move(0, -10)
            if event.key == K_RIGHT:
                if position_perso.x < (WIDTH - 85):
                    position_perso = position_perso.move(10, 0)
            if event.key == K_LEFT:
                if (position_perso.x + 9) > 0:
                    position_perso = position_perso.move(-10, 0)
                
    if is_apple == 1:
        if apple.apple_rect.colliderect(position_perso):
            score = score + 1
            fenetre.blit(score_text, score_text_rect) # Update score
            apple = None
            is_apple = 0
    
    fenetre.blit(bg, (0,0))
    if is_apple == 1:
        fenetre.blit(apple.apple, (apple.apple_rect.x, apple.apple_rect.y))
    fenetre.blit(perso, position_perso)
    fenetre.blit(text, textrect) # Display FPS
    fenetre.blit(score_text, score_text_rect) # Display score
    if score == 5:
        scorefont = pygame.font.SysFont(None, 48)
        scoretext = scorefont.render("ET DE 5 !", True, (255, 255, 255))
        scorerect = scoretext.get_rect()
        scorerect.x = WIDTH/2
        scorerect.y = HEIGHT/2
        fenetre.blit(scoretext, scorerect)
    pygame.display.flip()
    
    