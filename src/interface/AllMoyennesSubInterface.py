from tkinter import *


class AllMoyenneSubInterface:

    def __init__(self):
        self.window: Tk = Tk()
        self.id = id

    def getWindow(self) -> Tk:
        return self.window

    def onQuit(self):
        self.getWindow().destroy()

