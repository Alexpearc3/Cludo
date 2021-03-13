import pygame
import random
import numpy as np
class dice:
    def __init__(self):
        self.rolldice(self)


    def rolldice(self):
        dis = pygame.Overlay.display.set_mode((300, 300))
       # dice functionality
        dis = pygame.Overlay.display.set_mode((300, 300))
        pygame.Overlay.display.set_caption("dice")
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        d = random.randint(1, 6)
                    if d==1:
                        pygame.draw.rect(dis,(255, 0, 0), [120, 120, 70, 70])
                        pygame.draw.rect(dis, (0,0,0), [150, 150, 15, 15])
                    elif d==2:
                        pygame.draw.rect(dis, (255, 0, 0), [120, 120, 70, 70])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 170, 15, 15])
                    elif d==3:
                        pygame.draw.rect(dis, (255, 0, 0), [120, 120, 70, 70])
                        pygame.draw.rect(dis, (0, 0, 0), [150, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 170, 15, 15])
                    elif d==4:
                        pygame.draw.rect(dis, (255, 0, 0), [120, 120, 70, 70])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 130, 15, 15])
                    elif d==5:
                        pygame.draw.rect(dis, (255, 0, 0), [120, 120, 70, 70])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [150, 150, 15, 15])
                    elif d==6:
                        pygame.draw.rect(dis, (255, 0, 0), [120, 120, 70, 70])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 170, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 130, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [130, 150, 15, 15])
                        pygame.draw.rect(dis, (0, 0, 0), [170, 150, 15, 15])

        pygame.Overlay.display.update()
    pygame.quit()
    quit()