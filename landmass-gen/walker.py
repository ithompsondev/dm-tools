import random

class Walker:

    def __init__(self,steps,dgrid2):
        self.steps = steps
        self.dgrid2 = dgrid2
        self.right_bound = dgrid2.cols
        self.bot_bound = dgrid2.rows
        self.x,self.y = self.place_walker()


    def place_walker(self):
        ci = int(self.dgrid2.rows/2)
        cj = int(self.dgrid2.cols/2)
        self.dgrid2.set_cell(ci,cj,1)
        return (ci,cj)

    
    def color_landscape(self):
        # color the landscape after a walk has taken place so as to do the calculations once and not every frame in an animation
        for i in range(self.dgrid2.rows):
            for j in range(self.dgrid2.cols):
                self.color_cell(self.dgrid2.get_cell(i,j))



    def color_cell(self,cell):
        # Set brackets to use in if statement, similar to walk() method
        land_bracket = self.dgrid2.biome.get_landscape_distrib()
        veg_bracket = self.dgrid2.biome.get_vegetation_distrib() + land_bracket
        mount_bracket = self.dgrid2.biome.get_mountain_distrib() + veg_bracket
        water_bracket = self.dgrid2.biome.get_water_distrib() + mount_bracket
        r = random.random()
        if r < land_bracket:
            cell.set_color(self.dgrid2.biome.get_landscape_color())
        elif r < veg_bracket:
            cell.set_color(self.dgrid2.biome.get_vegetation_color())
        elif r < mount_bracket:
            cell.set_color(self.dgrid2.biome.get_mountain_color())
        else:
            cell.set_color(self.dgrid2.biome.get_water_color())


    def is_valid_step(self,x,y):
        # x represents column number
        # y represents row number
        if x < 0 or x >= self.right_bound: return False
        if y < 0 or y >= self.bot_bound: return False
        return True


    def step_left(self):
        step_x = self.x - 1 # check move before making move
        if self.is_valid_step(step_x,self.y):
            self.x = step_x
            prev_step_count = self.dgrid2.get_cell(self.y,self.x).get_value()
            self.dgrid2.set_cell(self.y,self.x,prev_step_count + 1)
            return (prev_step_count + 1)
        else:
            return -1


    def step_right(self):
        step_x = self.x + 1
        if self.is_valid_step(step_x,self.y):
            self.x = step_x
            prev_step_count = self.dgrid2.get_cell(self.y,self.x).get_value()
            self.dgrid2.set_cell(self.y,self.x,prev_step_count + 1)
            return (prev_step_count + 1)
        else:
            return -1


    def step_up(self):
        step_y = self.y - 1
        if self.is_valid_step(self.x,step_y):
            self.y = step_y
            prev_step_count = self.dgrid2.get_cell(self.y,self.x).get_value()
            self.dgrid2.set_cell(self.y,self.x,prev_step_count + 1)
            return (prev_step_count + 1)
        else:
            return -1


    def step_down(self):
        step_y = self.y + 1
        if self.is_valid_step(self.x,step_y):
            self.y = step_y
            prev_step_count = self.dgrid2.get_cell(self.y,self.x).get_value()
            self.dgrid2.set_cell(self.y,self.x,prev_step_count + 1)
            return (prev_step_count + 1)
        else:
            return -1


    def walk(self):
        steps = 0
        for i in range(self.steps):
            r = random.random()
            if r < 0.25:
                steps = self.step_left()
            elif r < 0.5:
                steps = self.step_right()
            elif r < 0.75:
                steps = self.step_up()
            else:
                steps = self.step_down()
            if steps > self.dgrid2.max_step_count:
                self.dgrid2.max_step_count = steps

