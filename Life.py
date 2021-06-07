from Generator import Generator
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class Life(Generator):
    def __init__(self, width, height, limit, noise, lifeTab):
        super().__init__(width+1,height+1)
        self.generation = 0
        self.limit = limit
        self.noise = noise
        
        self.HeightEntry = tk.Entry(lifeTab)
        self.WidthEntry = tk.Entry(lifeTab)
        self.GenEntry = tk.Entry(lifeTab)
        self.NoiseEntry = tk.Entry(lifeTab)
        
    
        self.HeightLabel = tk.Label(lifeTab, text="Height")
        self.WidthLabel = tk.Label(lifeTab, text="Width")
        self.GenLabel = tk.Label(lifeTab, text="Gen Limit")
        self.NoiseLabel = tk.Label(lifeTab, text = "Noise %")       
        
        self.canvasMap = tk.Canvas(lifeTab)
    
    def guiSetUp(self):
        self.HeightLabel.grid(row=1,column=1,sticky="W")
        self.WidthLabel.grid(row=2,column=1,sticky="W")
        self.HeightEntry.grid(row=1,column=2,sticky="W")
        self.WidthEntry.grid(row=2,column=2, sticky="W")
        
        self.GenLabel.grid(row=1,column=3,sticky="W")
        self.GenEntry.grid(row=1,column=4,sticky="W")
        self.NoiseLabel.grid(row=2,column=3,sticky="W")
        self.NoiseEntry.grid(row=2,column=4,sticky="W")     
        
    def generate(self,event):
        try:
            self.setHeight(self.HeightEntry.get())
            self.setWidth(self.WidthEntry.get())
            
            self.setLimit(self.GenEntry.get())
            self.setNoise(self.NoiseEntry.get())
            while self.finished() == False:
                self.life()
                print("finished")
                    
        except ValueError:
            print("Could not set")
       
    def life(self):
        self.generation += 1
        
        next = [[1 for j in range(self.width)] for i in range(self.height)]
        #print(self.height,self.width)
        for i in range(1,self.height-1):
            for j in range(1, self.width-1):
                sumCell = 0
                print(i,j)
                sumCell += self.map[i+1][j] #bottom
                sumCell += self.map[i-1][j] #top
                sumCell += self.map[i][j+1] #right
                sumCell += self.map[i][j-1] #lef
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
            self.height = height + 1
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
            self.width = width + 1
        else:
            print("Width:")
            raise ValueError        