import pygame
from macros import width, height

def loop():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    fps = pygame.time.Clock()
    running = True
    radar_raduis = int(810/2)
    arm_raduis = int(135/2)
    scale:tuple = (int(width/2) + arm_raduis , 943)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        pygame.draw.circle(screen, (255, 255, 255), (int(width/2), int(height/2)),radar_raduis , 4)
        pygame.draw.circle(screen, (0, 0, 255), (int(width/2), int(height/2)), arm_raduis, 2)
        pygame.draw.circle(screen, (255, 255, 255), (int(width/2), int(height/2)), 134, 2)
        pygame.draw.circle(screen, (255, 255, 255), (int(width/2), int(height/2)), 201, 2)
        pygame.draw.circle(screen, (255, 255, 255), (int(width/2), int(height/2)), 268, 2)
        pygame.draw.circle(screen, (255, 255, 255), (int(width/2), int(height/2)), 335, 2)
        pygame.draw.line(screen, (255,255,255), (scale[0], int(height/2)), (scale[1], int(height/2)), 1)
        pygame.display.flip()
        fps.tick(30)
    pygame.quit()