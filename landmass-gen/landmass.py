from assets import DrawableGrid2
from walker import Walker
from biomes import get_biome,Biome
import pygame
import sys

pygame.init()

VISIBLE_REGION_OFFSET = 20

# TODO: Document code
def setup():
    surface = pygame.display.set_mode((800,600))
    rows,cols,steps = (0,0,0)
    if len(sys.argv) != 5:
        print('Usage: python landmass.py <biome> <rows> <cols> <steps>')
        sys.exit()
    else:
        rows,cols,steps = (int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
    biome = get_biome(sys.argv[1])
    if biome == None:
        print('biomes: tropic|temperate|desert|tundra|grassland|savanna')
        sys.exit()
    # subtract double the initial offset since subtracting the offset alone from the width and height
    # draws outside of screen bounds, since we start at and offset of 20 we need to subtract 2*20 from w/h
    dgrid2 = DrawableGrid2(
            rows,
            cols,
            VISIBLE_REGION_OFFSET,
            VISIBLE_REGION_OFFSET,
            surface.get_width() - VISIBLE_REGION_OFFSET*2,
            surface.get_height() - VISIBLE_REGION_OFFSET*2,
            Biome(biome)
    )
    walker = Walker(steps,dgrid2)
    walker.place_walker()
    walker.walk()
    walker.color_landscape()
    dgrid2.apply_shaders()
    print(dgrid2)
    return (dgrid2,surface)


def main():
    dgrid2,surface = setup()
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
            
