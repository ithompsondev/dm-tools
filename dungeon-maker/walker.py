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

