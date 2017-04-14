import pygame
from pygame.locals import *
from sys import exit

def loadSprite(fileName):
    return pygame.image.load(fileName).convert_alpha()

pygame.init()

clock = pygame.time.Clock()

print("Starting Game...")
print("Loading...")

backgroundImg = pygame.image.load('img/background2.png')
background_size = backgroundImg.get_size()
background_rect = backgroundImg.get_rect()

width, height = 980, 700

running = True


screen = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('Insper Game')

running = True



# set up sound

#popSound = pygame.mixer.Sound('sound/pop.wav')
splashSound = pygame.mixer.Sound('sound/splash.wav')
#natureSound = pygame.mixer.Sound('sound/nature.mp3')

pygame.mixer.music.load('sound/soundTrack.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# set up sprites - images

grassCenterImg = loadSprite('img/Tiles/grassCenter.png')
grassMidImg = loadSprite('img/Tiles/grassMid.png')
signRightImg = loadSprite('img/Tiles/signRight.png')
avatarStandImg = loadSprite('img/Player/p3_stand.png')




while running:
    screen.blit(backgroundImg, background_rect)
    
    screen.blit(signRightImg, (0,700-70-70-70))
    screen.blit(grassMidImg, (0,700-70-70))
    screen.blit(grassCenterImg, (0,700-70))
    
    screen.blit(avatarStandImg, (70,700-70-70-70))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #pygame.display.flip()
    pygame.display.update()
    clock.tick(10)