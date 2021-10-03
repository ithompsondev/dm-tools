from assets import DrawableGrid2
from walker import Walker
import pygame
import sys

pygame.init()

def setup():
    surface = pygame.display.set_mode((800,600))
    rows,cols,steps = (0,0,0)
    if len(sys.argv) != 4:
        print('Usage: python landmass.py <rows> <cols> <steps>')
        sys.exit()
    else:
        rows,cols,steps = (int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    # subtract double the initial offset since subtracting the offset alone from the width and height
    # draws outside of screen bounds, since we start at and offset of 20 we need to subtract 2*20 from w/h
    dgrid2 = DrawableGrid2(rows,cols,20,20,surface.get_width()-40,surface.get_height()-40)
    walker = Walker(steps,dgrid2)
    walker.place_walker()
    walker.walk()
    return (dgrid2,surface)


def main():
    dgrid2,surface = setup()
    dgrid2.apply_shaders()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        surface.fill((200,200,200))
        dgrid2.draw(surface)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
            
