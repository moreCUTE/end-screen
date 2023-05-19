end = False
import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("EEL")  # sets the window title
screen = pygame.display.set_mode((1280, 720))  # creates game screen
screen.fill((0,0,0))
Win = pygame.image.load("insert picture.png/jpg")
win1 = pygame.image.load('insert picture.png/jpg')
clock = pygame.time.Clock() #set up clock



while not end:
    
    screen.blit(Win, (0,0))
    font = pygame.font.Font(None, 65)
    text = font.render(str("YOU WIN"), 1, (255,255,255))
    screen.blit(text, (480, 435))
    screen.blit(win1, (-50, 450))

    pygame.display.flip()
pygame.quit()
