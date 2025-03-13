import pygame
import pygame.display
from pygame.locals import *
from sys import exit

pygame.init()
    #Setting the window size configuration

lar = 800
altu= 600
tela = pygame.display.set_mode((lar, altu))
fps = pygame.time.Clock()


#   Setting movements variavels

pos_x = 0.0
pos_y = 0.0

pygame.display.set_caption("GAME_PROTORYPE") #Setting the title for the game window


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    fps.tick(60)
    


#Utilizando a analise de sistema cartesiano [e feito o posicionamento
#de elementos na tela porem no pygame essa logica e invertida ou 
#seja ele utiliza a 4 area do plano de referencia.
# 
# Exemplo o retangulo sao 4 pontos no plano sendo x,y
#  (3,5),   (5,5),  (3,8),  (5,8)
#   x_pos   +Lar    y_pos   +Altu 
#
#Alem de poder definir cor desse objeto em RGB


    tela.fill((0,0,0))

#               rect(tela,(Cores), (pos-x, pos-y, alt, larg))    
    pygame.draw.rect(tela,(255,0,0),(pos_x,pos_y,40,50)) 
    
    if pos_y != 200 and pos_x != 300: #logica de movimento 
         pos_y = pos_y + 15
    
    if pos_y >=altu:
        pos_y = -150
        pos_x = pos_x + 20
        if pos_x >= lar:
            pos_x = 0
            pos_y = 0
 
#               circle(tela,(Cores), (pos-x, pos-y)'central',raio)    
    pygame.draw.circle(tela,(55,0,66),(220,380),40)

#               line(tela,(Cores),(pos-init x,y),(pos-end x,y))    
    pygame.draw.line(tela,(0,0,255),(400,0),(400,600),8)

    pygame.draw.rect(tela,(255,255,0),(600,300,40,50))
    pygame.draw.circle(tela,(55,90,66),(620,380),40)



