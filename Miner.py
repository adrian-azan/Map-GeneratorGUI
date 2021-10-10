import random as ran


class Miner:
    def __init__(self,map,endurance,size):
        self.map = map
        self.maxEndurance = endurance
        self.endurance = endurance
        self.size = size
        self.X = 0
        self.Y = 0
        self.ID = 1

    def reset(self):
        self.endurance = self.maxEndurance
        self.ID += 1

    def pos(self,x,y):
        self.X = int(x)
        self.Y = int(y)

    def move(self):
        direction = int(ran.randint(0, 4))

        if direction == 0 and self.X + self.size < len(self.map[0]) - 1:
            self.X += self.size
        elif direction == 1 and self.Y + self.size < len(self.map) - 1:
            self.Y += self.size
        elif direction == 2 and self.X - self.size > 0:
            self.X -= self.size
        elif direction == 3 and self.Y - self.size > 0:
            self.Y -= self.size

        self.endurance -= 1
        return self.endurance > 0