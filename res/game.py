import pygame

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("MWGC")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
