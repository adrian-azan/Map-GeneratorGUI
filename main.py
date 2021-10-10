import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from Life import Life


if __name__ == "__main__":
    
    root = tk.Tk()    
    root.geometry("960x540")
    
    control = ttk.Notebook(root)
    lifeTab = ttk.Frame(control)
    

    lifeGenerator = Life(100,100,4,80,lifeTab)
    lifeGenerator.guiSetUp()

    """
    lifeButton = tk.Button(lifeTab,text="Generate")
    lifeButton.bind("<Button-1>",lifeGenerator.generate)
    lifeButton.grid(row=3,column=1)
    """


    """
    lifeGenerator.output("sample.png")
    imageMap = Image.open("sample.png")
    imageMap = ImageTk.PhotoImage(imageMap)
    
    label1 = tk.Label(lifeTab,image=imageMap)
    label1.image = imageMap
    label1.grid(row=0,column=1,columnspan=3)
    """
    
    diffuseTab = ttk.Frame(control)
    
    control.add(lifeTab, text="Life")
    control.add(diffuseTab, text="Diffuse")
    control.grid()
    
    root.mainloop()
    