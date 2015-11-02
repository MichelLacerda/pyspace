import pygame, sys, os, time

import engine.utils


from pygame.locals import*

if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600), 0, 16)
    
    group = pygame.sprite.Group()
    
    #fundo 
    back = engine.utils.path("space.png",'sprite')
    back_fundo = pygame.image.load(back)
    
    #botão
    jogar = engine.utils.path("bt_jogar.png",'sprite')
    sair = engine.utils.path("bt_sair.png",'sprite')
    bt_jogar = pygame.image.load(jogar)
    bt_sair = pygame.image.load(sair)
    
    #mouse
    seta = engine.utils.path("cursor.png",'sprite')
    seta_st = pygame.image.load(seta)
        
    #select = pygame.mouse.get_pressed()
    
    pygame.mouse.set_visible(False)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        p_x, p_y = pygame.mouse.get_pos()
            
        screen.fill((1,0,0))
        
        screen.blit(back_fundo,(0,0))
        screen.blit(bt_jogar,(300,300))
        screen.blit(bt_sair,(300, 400))
        
        screen.blit(seta_st,(p_x, p_y))
        
        
        pygame.display.update()
        
        
        

"""
    contador = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        # colisao
		
        for c in Cursor.group:
            collisions = pygame.sprite.spritecollide(c, Botao.group, False)
            if len(collisions) > 0:
                for hit in collisions:
                    contador+=1
                    print('bot', contador)
                
        
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        
        cursor.position((m_x, m_y))
        Botao.group.draw(screen)
        Cursor.group.draw(screen)
        
		
        pygame.display.update()
        
"""