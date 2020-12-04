import pygame

pygame.init()

gameWindow = pygame.display.set_mode((10, 10))
pygame.display.set_caption("Get All Dum Events")

exit_game = False
game_over = False

print("Space", pygame.K_SPACE)
print("C", pygame.K_c)
print("X", pygame.K_x)
print(pygame.QUIT)
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")
            elif event.key == pygame.K_c:
                print("C")
            elif event.key == pygame.K_x:
                print("X")
            else:
                print(event.key)
pygame.quit()
quit()
