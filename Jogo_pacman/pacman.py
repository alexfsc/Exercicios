import pygame

pygame.init()

AMARELO = (255,255,0)
PRETO = (0,0,0)
RAIO = 20
centro_x = 1 + RAIO
centro_y = 1 + RAIO
vel_x = 0
vel_y = 0



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


    centro_x = centro_x + vel_x
    centro_y = centro_y + vel_y

    evento = pygame.event.get()
    for e in evento:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    vel_x = 0.1

                elif e.key == pygame.K_LEFT:
                    vel_x = -0.1

                elif e.key == pygame.K_UP:
                    vel_y = -0.1

                elif e.key == pygame.K_DOWN:
                    vel_y = 0.1
            elif e.type == pygame.KEYUP:
                vel_y = 0
                vel_x = 0



