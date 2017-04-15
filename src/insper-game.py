import pygame
from pygame.locals import *
from sys import exit

def loadSprite(fileName):
    return pygame.image.load(fileName).convert_alpha()
    
    
def drawPlatform(x, y):
   screen.blit(platformLeftImg, (x, y))
   screen.blit(platformMidImg, (x+tileSize,y))
   screen.blit(platformRightImg, (x+tileSize*2,y))
   
	
	
pygame.init()

clock = pygame.time.Clock()

print("Starting Game...")
print("Loading...")


backgroundImg = pygame.image.load('img/background2.png')
background_size = backgroundImg.get_size()
background_rect = backgroundImg.get_rect()

width, height = 980, 700
tileSize = 70 #pixels
avatarStep = 10 #pixels
avatarX = tileSize #initial position
avatarY = 470

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)

pygame.display.set_caption('Insper Game')

running = True



# set up sound

#popSound = pygame.mixer.Sound('sound/pop.wav')
splashSound = pygame.mixer.Sound('sound/splash.wav')
laserSound = pygame.mixer.Sound('sound/laser.wav')
jumpSound = pygame.mixer.Sound('sound/jump2.wav')
#natureSound = pygame.mixer.Sound('sound/nature.mp3')

pygame.mixer.music.load('sound/soundTrack.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# set up sprites - images

grassCenterImg = loadSprite('img/Tiles/grassCenter.png')
grassMidImg = loadSprite('img/Tiles/grassMid.png')
signRightImg = loadSprite('img/Tiles/signRight.png')

platformLeftImg = loadSprite('img/Tiles/grassHalfLeft.png')
platformMidImg = loadSprite('img/Tiles/grassHalfMid.png')
platformRightImg = loadSprite('img/Tiles/grassHalfRight.png')
boxedItemImg = loadSprite('img/Tiles/boxitem.png')

avatarStandImg = loadSprite('img/Player/p3_stand.png')
avatarJumpImg = loadSprite('img/Player/p3_jump.png')
avatarDownImg = loadSprite('img/Player/p3_duck.png')

while running:
    #fundo completo (3 x tela)
    screen.blit(backgroundImg, background_rect)
    
    #Seta
    screen.blit(signRightImg, (0,height-tileSize*3))
    
    #Chao
    for grid in range(0,1000,70):	
    	screen.blit(grassMidImg, (grid,height-tileSize*2))
    	screen.blit(grassCenterImg, (grid,height-tileSize))
    
    screen.blit(avatarStandImg, (avatarX, avatarY))
    
    screen.blit(boxedItemImg, (400, 400-tileSize))
    drawPlatform(400, 400)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("key left")
                avatarX -= avatarStep
            if event.key == pygame.K_RIGHT:
                print("key right")
                avatarX += avatarStep
            if event.key == pygame.K_UP:
                print("key up")
                jumpSound.play()
            if event.key == pygame.K_DOWN:
                print("key down")
                splashSound.play()    
            if event.key == pygame.K_SPACE:
                print("key space")
                laserSound.play()    
            if event.key == pygame.K_1:
                print("key 1")
                if musicPlaying:
                    musicPlaying=False
                    pygame.mixer.music.stop()
                else:
                    musicPlaying=True
                    pygame.mixer.music.play(-1, 0.0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                print("key down up")
                
                
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(10)