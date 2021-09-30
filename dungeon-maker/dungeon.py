import random
import pygame
from grid import Grid
from render import Render
import offset
import color

pygame.init()

def is_wall(grid,i,j):
    return grid.get_value(i,j) == 0


def is_valid(row,col,rbound,dbound):
    can_move = True
    if row < 0:
        can_move = False
    elif row >= rbound:
        can_move = False
    elif col < 0:
        can_move = False
    elif col >= dbound:
        can_move = False
    return can_move


def random_walk(grid,steps):
    """
        Perform a random walk allowing the walker to revisit previously visited cells. Increment
        a cell's value if a cell is revisited.
    """
    center_row = int(grid.rows/2)
    center_col = int(grid.cols/2)

    # equal likelihood of L,R,U,D
    curr_row = center_row
    curr_col = center_col
    grid.set_value(curr_row,curr_col,1)
    row_bound = grid.rows
    col_bound = grid.cols
    for i in range(steps):
        r = random.random()
        if r < 0.25 and is_valid(curr_row,curr_col-1,row_bound,col_bound):
            # left
            curr_col -= 1
            grid.set_value(curr_row,curr_col,grid.get_value(curr_row,curr_col) + 1)
        elif r < 0.50 and is_valid(curr_row,curr_col+1,row_bound,col_bound):
            # right
            curr_col += 1
            grid.set_value(curr_row,curr_col,grid.get_value(curr_row,curr_col) + 1)
        elif r < 0.75 and is_valid(curr_row-1,curr_col,row_bound,col_bound):
            # up
            curr_row -= 1
            grid.set_value(curr_row,curr_col,grid.get_value(curr_row,curr_col) + 1)
        elif r <= 1.0 and is_valid(curr_row+1,curr_col,row_bound,col_bound):
            # down
            curr_row += 1
            grid.set_value(curr_row,curr_col,grid.get_value(curr_row,curr_col) + 1)


# TODO: Fix, SEGFAULTS here
def save_dungeon_img(screen,dname):
    pygame.image.save(screen,f'{dname}.png')


def init_display(width,height):
    return pygame.display.set_mode((width,height))


def get_dimensions(screen):
    return (screen.get_width(),screen.get_height())


# TODO: Add to seperate class
# TODO: Globalize offset values as well as thickness 
def create_visible_region(scr_w,scr_h,offset_w=offset.WIDTH,offset_h=offset.HEIGHT):
    return pygame.Rect(0 + offset_w,0 + offset_h,scr_w - 2*offset_w, scr_h - 2*offset_h)


def draw_visible_region(screen,visible_region,thickness=offset.THICKNESS):
    # Draw the viewable region as a black background surrounded by gold border
    pygame.draw.rect(screen,color.colors['BLACK'],visible_region,width=0)
    pygame.draw.rect(screen,color.colors['GOLD'],visible_region,width=thickness)


def game_loop(screen,grid):
    w,h, = get_dimensions(screen)
    visible_region = create_visible_region(w,h)
    grid.set_visible_bounds(visible_region.width,visible_region.height)
    renderer = Render(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(color.colors['WHITE'])
        draw_visible_region(screen,visible_region)
        renderer.render(grid)
        pygame.display.flip()
    pygame.quit()


# TODO: PLEASE DOCUMENT YOUR CODE [50%]
# TODO: Possible settings tweak to darken only red or only blue or only green. Keep spill the same
# TODO: tweaking chances of moving left and right, up or down (gradients?)
# TODO: Fix the thickness offset when drawing cells as to not overlap down and right borders
# TODO: Save the screen to PNG or JPG image.
# TODO: Refactor code into meaningful classes like Cell, possibly a color class, Renderer.
# TODO: Create a GENERAL menuing system
# TODO: Step animations. Push a MOVE object (x_prev,y_prev,x_curr,y_curr) to a Queue for queued rendering
def main():
    rows = int(input('rows: '))
    cols = int(input('columns: '))
    steps = int(input('steps: '))
    dname = input('dungeon name: ')
    # grid = new_grid(rows,cols)
    grid = Grid(rows,cols)
    random_walk(grid,steps)
    screen = init_display(800,600)
    game_loop(screen,grid)
    # save_dungeon_img(screen,dname), SEGFAULT HERE


if __name__ == '__main__':
    main()
