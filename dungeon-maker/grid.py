import pygame

class Cell:
    """
        Bundle a cells pygame.Rect with its color so that cells act as a heat map for a random
        walk for more than 1 step on the same cell
    """

    def __init__(self,x,y,w,h,color=(159,43,104)):
        self.cell = pygame.Rect(x,y,w,h)
        self.r,self.g,self.b = color


    # delta passed in by calling function. Darken a cell based on some change in the underlying grid (delta)
    def darken(self,delta):
        if self.r >= 20:
            self.r -= 20*delta
        if self.g >= 20:
            self.g -= 20*delta
        if self.b >= 20:
            self.b -= 20*delta

        while not self.in_bounds(self.r,self.g,self.b):
            self.color_spill()
    
    
    def in_bounds(self,r,g,b):
        within_bounds = True
        if r < 0 or r > 255: within_bounds = False
        if g < 0 or g > 255: within_bounds = False
        if b < 0 or b > 255: within_bounds = False
        return within_bounds


    # Color wrap arounds
    def color_spill(self):
        if self.r < 0:
            self.r *= -1
            self.b += self.r # negative red spills into blue
        elif self.r > 255:
            self.r -= (self.r - 255)
            self.g += (self.r - 255) # red spills into green
        if self.g < 0:
            self.g *= -1
            self.r += self.g # negative green spills into red
        elif self.g > 255:
            self.g -= (self.g - 255)
            self.b += (self.g - 255) # green spills into blue
        if self.b < 0:
            self.b *= -1
            self.g += self.b # negative blue spills into green
        elif self.b > 255:
            self.b -= (self.b - 255)
            self.r += (self.b - 255) # blue spills into red


    def get_color(self):
        return (self.r,self.g,self.b)


    def draw(self,screen,fill=True):
        if fill:
            pygame.draw.rect(screen,self.get_color(),self.cell,width=0)
        else:
            pygame.draw.rect(screen,self.get_color(),self.cell,width=1)


class Grid:
    def __init__(self,rows,cols,vis_offset=20,thick_offset=2):
        self.rows = rows
        self.cols = cols
        self.vis_w = -1
        self.vis_h = -1
        self.vis_offset = vis_offset
        self.thick_offset = thick_offset
        self.grid = []
        self.fill_grid()


    def fill_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                self.grid[i].append(0)


    # TODO: Validation for indices
    def get_value(self,row,col):
        return self.grid[row][col]


    def set_value(self,row,col,val):
        self.grid[row][col] = val


    def set_visible_bounds(self,vis_w,vis_h):
        self.vis_w = vis_w
        self.vis_h = vis_h


    def draw(self,screen):
        # compute the dimension for a cell withing the visible region
        cell_w = self.vis_w/self.cols
        cell_h = self.vis_h/self.rows
        for i in range(self.rows):
            for j in range(self.cols):
                curr_cell = self.get_value(i,j)
                if curr_cell >= 1:
                    # Standard way to draw from grid[i][j] to screen (j,i)
                    x = (j*cell_w)
                    y = (i*cell_h)
                    """
                        Add vis_offset to x and y to position cells withing the visible region
                        Add 2*thick_offset to x and y to comfortably position a cell within the visible region such that the cell will not overlap the 
                        left and top borders
                        Subtract 2*thick_offset from width and height to comfortable position a cell within the visible region such that the cell will not
                        overlap the right and bottom borders
                    """
                    xy_offset = self.vis_offset + self.thick_offset*2
                    wh_offset = -1*self.thick_offset
                    cell = Cell(x + xy_offset,y + xy_offset,cell_w + wh_offset,cell_h + wh_offset)
                    if curr_cell > 1:
                        cell.darken(curr_cell)
                    cell.draw(screen) # draw_cell(screen,cell)


