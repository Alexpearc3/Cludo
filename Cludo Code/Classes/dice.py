import pygame
import random
import numpy as np

#dice functionality
dis = pygame.display.set_mode((300,300))
pygame.display.set_caption("dice")
end = False
while end==False:
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

    pygame.display.update()
pygame.quit()
quit()