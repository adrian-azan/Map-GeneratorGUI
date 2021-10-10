from Generator import Generator
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random as ran
from Miner import Miner

class Life(Generator):
    def __init__(self, width, height, limit, noise, lifeTab):
        super().__init__(width+2,height+2)
        self.generation = 0
        self.limit = limit
        self.noise = noise
        self.master = lifeTab

        self.layout = dict()
        self.layout["left"] = tk.Frame(lifeTab)
        self.layout["right"] = tk.Frame(lifeTab)



        self.HeightEntry = tk.Entry(self.layout["right"])
        self.WidthEntry = tk.Entry(self.layout["right"])
        self.GenEntry = tk.Entry(self.layout["right"])
        self.NoiseEntry = tk.Entry(self.layout["right"])
        
    
        self.HeightLabel = tk.Label(self.layout["right"], text="Height")
        self.WidthLabel = tk.Label(self.layout["right"], text="Width")
        self.GenLabel = tk.Label(self.layout["right"], text="Gen Limit")
        self.NoiseLabel = tk.Label(self.layout["right"], text = "Noise %")

        self.lifeButton = tk.Button(self.layout["right"], text="Generate")
        self.lifeButton.bind("<Button-1>", self.generate)

        self.previewButton = tk.Button(self.layout["right"], text="Preview")
        self.previewButton.bind("<Button-1>", self.preview)

        self.canvasMap = tk.Canvas(self.layout["left"])


        self.imageMap = Image.new("RGB", (150,150))
        self.imageMap = ImageTk.PhotoImage(self.imageMap)

        self.ImageLabel = tk.Label(self.layout["left"], image=self.imageMap)
        self.ImageLabel.image = self.ImageLabel


        self.pixelTypes[1] = ("Dirt", (0,0,0),0,0)
        self.pixelTypes[0] = ("Air", (255,255,255),0,0)
        self.pixelTypes[2] = ("Coal", (0,255,0),20,100)


    
    def guiSetUp(self):


        self.layout["left"].grid(row=0,column=0)
        self.layout["right"].grid(row=0,column =1,sticky="NW")


        self.ImageLabel.grid(row=0, column=0)

        self.HeightLabel.grid(row=0,column=0,sticky="NW")
        self.HeightEntry.grid(row=0, column=1, sticky="NW")
        self.WidthLabel.grid(row=1,column=0,sticky="NW")
        self.WidthEntry.grid(row=1,column=1, sticky="NW")
        
        self.GenLabel.grid(row=0,column=2,sticky="NW")
        self.GenEntry.grid(row=0,column=3,sticky="NW")
        self.NoiseLabel.grid(row=1,column=2,sticky="NW")
        self.NoiseEntry.grid(row=1,column=3,sticky="NW")

        self.previewButton.grid(row=3,column=0)
        self.lifeButton.grid(row=4, column=0,sticky="SW")


    def preview(self,event):
        try:
            self.setWidth(self.HeightEntry.get())
            self.setHeight(self.WidthEntry.get())

            self.setLimit(self.GenEntry.get())
            self.setNoise(self.NoiseEntry.get())
            self.restart()
            while self.finished() == False:
                self.life()

            miner = Miner(self.map, self.pixelTypes[2][2], 1)
            for veinAmount in range(self.pixelTypes[2][3]):
                miner.reset()
                x = ran.randint(1, self.width)
                y = ran.randint(1, self.height)
                miner.pos(x, y)
                while miner.move():
                    print(miner.X, miner.Y)
                    try:
                        self.map[miner.Y][miner.X] = 2
                    except:
                        pass

            self.imageMap = self.output("preview", "Life")
            self.imageMap = ImageTk.PhotoImage(self.imageMap)

            self.ImageLabel = tk.Label(self.layout["left"], image=self.imageMap)
            self.ImageLabel.image = self.ImageLabel
            self.ImageLabel.grid(row=0, column=0)

        except ValueError:
            print("Could not set")


    def generate(self,event):
        try:
            self.setWidth(self.HeightEntry.get())
            self.setHeight (self.WidthEntry.get())
            
            self.setLimit(self.GenEntry.get())
            self.setNoise(self.NoiseEntry.get())
            self.restart()
            while self.finished() == False:
                self.life()

            miner = Miner(self.map, self.pixelTypes[2][2],1 )
            for veinAmount in range(self.pixelTypes[2][3]):
                miner.reset()
                x = ran.randint(1,self.width)
                y = ran.randint(1,self.height)
                miner.pos(x,y)
                while miner.move():
                    print(miner.X,miner.Y)
                    try:
                        self.map[miner.Y][miner.X] = 2
                    except:
                        pass

            name = "{}x{}_G{}_{}%.bmp".format(str(self.width), str(self.height),self.generation,self.noise)
            self.imageMap = self.output(name,"Life")
            self.imageMap.save("Life/"+name)

            self.imageMap = ImageTk.PhotoImage(self.imageMap)

            self.ImageLabel = tk.Label(self.layout["left"], image=self.imageMap)
            self.ImageLabel.image = self.ImageLabel
            self.ImageLabel.grid(row=0, column=0)

        except ValueError :
            print("Could not set")

       
    def life(self):
        self.generation += 1
        
        next = [[1 for j in range(self.width)] for i in range(self.height)]

        for i in range(1,self.height-1):
            for j in range(1, self.width-1):
                sumCell = 0
                sumCell += self.map[i+1][j] #bottom
                sumCell += self.map[i-1][j] #top
                sumCell += self.map[i][j+1] #right
                sumCell += self.map[i][j-1] #left
                sumCell += self.map[i+1][j+1] #bottom right
                sumCell += self.map[i+1][j-1] #bottom left
                sumCell += self.map[i-1][j+1] #top right
                sumCell += self.map[i-1][j-1] #top left                

                if sumCell >= 6:
                    next[i][j] = 1
                elif sum == 3:
                    next[i][j] = self.map[i][j]
                else:
                    next[i][j] = 0
        self.map = next
        
    def finished(self):
        return self.generation >= self.limit
    
    def restart(self):
        del self.map
        self.map = [[1 for j in range(self.width)] for i in range(self.height)]
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                chance = ran.randint(0, 100)
                if chance >= self.noise:
                    self.map[i][j] = 0
                else:
                    self.map[i][j] = 1
            self.generation = 0
        
    def setLimit(self,limit):
        try:
            limit = int(limit)            
        except TypeError:
            print("Limit:")
            raise TypeError 
        
        if 1 <= limit <= 100:
            self.limit = limit
        else:
            print("Limit:")
            raise ValueError

    def setNoise(self,noise):
        try:
            noise = int(noise)            
        except TypeError:
            print("Noise:")
            raise TypeError         
        
        if 0 <= noise <= 100:
            self.noise = noise
        else:
            print("Noise:")
            raise ValueError
        
    def setHeight(self,height):
        try:
            height = int(height)            
        except TypeError:
            print("Height:")
            raise TypeError        
        
        if height >= 4:
            self.height = height + 2
        else:
            print("Height:")
            raise ValueError
        
    def setWidth(self, width):
        try:
            width = int(width)            
        except TypeError:
            print("Width")
            raise TypeError 
        
        if width >= 4:
            self.width = width + 2
        else:
            print("Width:")
            raise ValueError        