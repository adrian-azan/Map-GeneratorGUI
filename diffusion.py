import random as ran
from Miner import Miner
import os.path

from Generator import Generator


class Diffusion(Generator):

    def __init__(self,w,h,g):
        super().__init__(w,h,g)
        self.Tom = Miner(self.map,400,1)
        self.Tom.pos(self.width/2,self.height/2)

    def restart(self):
        self.map = [[1 for j in range(self.width)] for i in range(self.height)]
        self.space = 0
        self.Tom.reset()
        self.Tom.pos(self.width/2, self.height/2)


    def diffusion(self):
        change = False
        Tom = self.Tom
        while self.space < self.spaceGoal and change == False:
            while Tom.endurance > 0 and change == False:
                direction = int(ran.randint(0, 4))
                # print(direction)
                if direction == 0 and Tom.X + Tom.size < self.width - 1:
                    Tom.X += Tom.size
                elif direction == 1 and Tom.Y + Tom.size < self.height - 1:
                    Tom.Y += Tom.size
                elif direction == 2 and Tom.X - Tom.size > 0:
                    Tom.X -= Tom.size
                elif direction == 3 and Tom.Y - Tom.size > 0:
                    Tom.Y -= Tom.size

                if self.map[Tom.Y][Tom.X] == 1:
                    self.map[Tom.Y][Tom.X] = 0
                    change = True
                    self.space += 1

                self.Tom.endurance -= 1

            if self.Tom.endurance <= 0:
                self.Tom.reset()


    def finished(self):
        if self.space >= self.spaceGoal:
            return True
        return False



