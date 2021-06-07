class Generator:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.map = [[1 for j in range(width)] for i in range(height)]
        