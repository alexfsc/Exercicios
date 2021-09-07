import pygame

pygame.init()

AMARELO = (255,255,0)
PRETO = (0,0,0)
RAIO = 30
centro_x = 1
centro_y = 1
vel_x = 0.1
vel_y = 0.1



tela = pygame.display.set_mode((640,300),0)



while True:
    tela.fill(PRETO)
    #Desenhando a cabeça do pacman
    pygame.draw.circle(tela, AMARELO, (int(centro_x), int(centro_y)), RAIO, 0)

    #Desenhando a boca do pacman
    pontos = [(centro_x,centro_y),(centro_x + RAIO, centro_y),(centro_x+RAIO,centro_y-RAIO)]
    pygame.draw.polygon(tela,(PRETO),pontos,0)

    #Desenhando o olho do pacman
    pygame.draw.circle(tela, (PRETO), (int(centro_x + RAIO/5), int(centro_y - RAIO/2)), RAIO/10, 0)



    pygame.display.update()


    if centro_x + RAIO > 640:
        vel_x = -0.1
    if centro_x - RAIO < 0:
        vel_x = 0.1

    if centro_y + RAIO > 300:
        vel_y = -0.1
    if centro_y - RAIO < 0:
        vel_y = 0.1

    centro_x = centro_x + vel_x
    centro_y = centro_y + vel_y


    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
