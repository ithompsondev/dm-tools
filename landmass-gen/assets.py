import pygame
import biomes
import random

class DrawableCell:

    def __init__(self,value,color=(255,255,255)):
        self.value = value
        self.color = color


    def set_value(self,new_value):
        self.value = new_value


    def get_value(self):
        return self.value


    def set_color(self,new_color):
        self.color = new_color


    def get_color(self):
        return self.color


    def darken_color(self):
        # Darken this cell's current color
        pass


    def lighten_color(self):
        # Lighten this cell's current color
        pass


    def mul_color(self,delta):
        r,g,b = self.get_color()
        self.set_color((r*delta,g*delta,b*delta))


    def invert_color(self):
        # Invert this cell'c current color
        pass


    def draw(self,surface,x,y,w,h):
        pygame.draw.rect(surface,self.color,pygame.Rect(x,y,w,h))


class DrawableGrid2:

    def __init__(self,rows,cols,x,y,width,height,biome):
        self.dgrid = self.new_grid(rows,cols)
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Cells are contained within a grid, so a grid holds cell width and height info
        self.cell_width = int(width/cols)
        self.cell_height = int(height/rows)
        self.max_step_count = -1 # keep track of the max step count
        self.color = (0,0,0)
        self.biome = biome


    def new_grid(self,rows,cols):
        grid2 = []
        for i in range(rows):
            grid2.append([])
            for j in range(cols):
                grid2[i].append(DrawableCell(0))
        return grid2


    def get_cell(self,row,col):
        return self.dgrid[row][col]


    def set_cell(self,row,col,value):
        self.dgrid[row][col].set_value(value)


    def set_color(self,rgb):
        self.color = rgb


    def apply_shaders(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.get_cell(i,j)
                steps = cell.get_value()
                shader = (self.max_step_count - (steps - 1))/self.max_step_count
                cell.mul_color(shader)


    def draw(self,surface):
        # Drawable region
        pygame.draw.rect(surface,self.color,pygame.Rect(self.x,self.y,self.width,self.height))
        for i in range(self.rows):
            for j in range(self.cols):
                dcell = self.get_cell(i,j)
                steps = dcell.get_value()
                if steps >= 1:
                    # if steps = 1 then shader = (max - 0)/max which is the default color, increased steps lead to darker colors
                    cell_x = self.x + j*self.cell_width # start at self.x if the grid is position at an offset from x = 0 (surface top left corner)
                    cell_y = self.y + i*self.cell_height # start at self.y if the grid is positioned at an offset from y = 0 (surface top left corner)
                    dcell.draw(surface,cell_x,cell_y,self.cell_width,self.cell_height)
 
