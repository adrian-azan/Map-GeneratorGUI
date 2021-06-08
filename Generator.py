from PIL import ImageTk, Image
import numpy as np

class Generator:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.map = [[1 for j in range(width)] for i in range(height)]
        self.pixelTypes = dict()

    def output(self, fileName):
        new_image = Image.new("RGB", (len(self.map), len(self.map[0])))
        pixels = new_image.load()
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == 1:
                    pixels[row, col] = (0,0,0)
                else:
                    pixels[row, col] = (255,255,255)

        if fileName.find(".") == -1:
            fileName += ".bmp"
        new_image.save(fileName)







