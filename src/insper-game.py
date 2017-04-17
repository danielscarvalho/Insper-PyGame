#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Insper - Engenharia - Design de Software - Python - PyGame
# Jogo 2D de plataforma
# Prof: Romero Tori
# Prof: Daniel Carvalho @danielscarvalho

# Estrutura básica do jogo - exemplo

#TODO: Refazer (refactor) o programa utilizando classes (OO - Orientação a Objetos)
#TODO: Criar novas fases do jogo utilizando os diversos sprites (imagens) disponíveis
#TODO: Possibilitar trocar de avatar: rosa, verde e azul
#TODO: Criar tela inicial (splash screen)
#TODO: Criar menu e tela de configuração
#TODO: Criar recursos para salvar o jogo
#TODO: Montar testes de SW
#TODO: BIG-FIX

import pygame
from pygame.locals import *

class Position:
    def __init__(self): #método construtor da classe
        tileSize = 70 #tamanho básico dos sprites (imagens)
        alpha = ["A","B","C","D","E","F","G","H","I","J"] # 700/70 posições discretas eixo y - vertical
        self.abscissa = range(-tileSize, 2940, tileSize) # eixo x - horizontal
        self.ordinate = dict(zip(alpha, range(0, 700 , tileSize))) # eixo y - vertical
        
    def getAbscissa(self, x):
        return self.abscissa[x]
    
    def getOrdinate(self, y):
        return self.ordinate[y] # retorna valor para intervalo de A à J

    def getPosition(self, pos):
        yLetter = pos[0].upper()
        xNumber = int(pos[1:len(pos)])
        print(yLetter, xNumber)
        return Position.getAbscissa(self, xNumber), Position.getOrdinate(self, yLetter)
    
    def __str__(self):
    	return str(list(self.abscissa)) + "\n" + str(self.ordinate)

def avatarJump():
    pass
    
def avatarFire():
    pass
    
def bossEmergencyScreen():
    pass
	
def loadSprite(fileName):
    return pygame.image.load(fileName).convert_alpha()
  
def drawPlatform(x, y):
    screen.blit(platformLeftImg,  (x, y))
    screen.blit(platformMidImg,   (x + tileSize, y))
    screen.blit(platformRightImg, (x + tileSize * 2, y))

# main

pygame.init()

grid = Position()

clock = pygame.time.Clock()

print("Starting Game...")
print("Loading...")

backgroundImg = pygame.image.load('img/background2.png')
background_size = backgroundImg.get_size()
background_rect = backgroundImg.get_rect()

#Globas - refactor
width, height = 980, 700 #Sprites de 70px
tileSize = 70 #pixels
avatarStep = 10 #pixels
avatarX = tileSize #initial position
avatarY = 470
goRigth = True #to know avatar direction
duckOffset = 21
running = True

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)

pygame.display.set_caption('Insper - Jogo 2D de plataforma')

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
avatarCurrentImg = avatarStandImg #avatar atual

#loop infinito do jogo!!
while running:
    #fundo completo (3 x tela - viewport)
    screen.blit(backgroundImg, background_rect)
    
    #Seta
    screen.blit(signRightImg, (0, height - tileSize * 3))
    
    #Chão
    for grid in range(0, 1000, tileSize):	
    	screen.blit(grassMidImg, (grid, height - tileSize * 2))
    	screen.blit(grassCenterImg, (grid, height - tileSize))
    
    #Item
    screen.blit(boxedItemImg, (400, 400 - tileSize))
    
    #Plataforma
    #x, y = grid.getPosition("D10")
    drawPlatform(400, 400)

    #Avatar
    screen.blit(avatarCurrentImg, (avatarX, avatarY))
    
    pygame.display.update()
    
    #eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if avatarX > 0: #Limite Esquerdo da fase
                    if goRigth:
                        avatarCurrentImg = pygame.transform.flip(avatarCurrentImg, True, False)
                    print("key left")
                    avatarX -= avatarStep
                    goRigth = False
            if event.key == pygame.K_RIGHT:        
                if not goRigth:
                    avatarCurrentImg = pygame.transform.flip(avatarCurrentImg, True, False)
                print("key right")
                avatarX += avatarStep
                goRigth = True
            if event.key == pygame.K_UP:
                print("key up")
                avatarJump()
                jumpSound.play()
            if event.key == pygame.K_DOWN:
                avatarCurrentImg = avatarDownImg
                if goRigth:
                    avatarCurrentImg = pygame.transform.flip(avatarCurrentImg, True, False)
                avatarY += duckOffset
                print("key down")
                splashSound.play()
            if event.key == pygame.K_SPACE:
                avatarFire()
                print("key space")
                laserSound.play()    
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_b:
                bossEmergencyScreen()
            if event.key == pygame.K_s:
                print("key s")
                if musicPlaying:
                    musicPlaying=False
                    pygame.mixer.music.stop()
                else:
                    musicPlaying=True
                    pygame.mixer.music.play(-1, 0.0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                avatarCurrentImg = avatarStandImg
                if not goRigth:
                    avatarCurrentImg = pygame.transform.flip(avatarCurrentImg, True, False)
                avatarY -= duckOffset
                print("key down up")
                
    pygame.display.update()
    clock.tick(10)