import pygame
pygame.init()
while True:
    event_list = pygame.event.get()
    for i in event_list:
        print(i.type)
