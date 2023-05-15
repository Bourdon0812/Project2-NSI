from tkinter import *


class MainInterface:

    def __init__(
            self,
            window: Tk,
            title: str,
            iconPath: str,
            geometry: str,
            minSize: tuple,
            maxSize: tuple,
            background: str
    ):
        self.window: Tk = window
        self.title: str = title
        self.iconPath: str = iconPath
        self.geometry: str = geometry
        self.minSize: tuple = minSize
        self.maxSize: tuple = maxSize
        self.background: str = background

    def genWindow(self):
        '''
        genere la fenetre de base
        :return void:
        '''
        window = self.getWindow()
        window.title(self.getTitle())
        window.iconbitmap(self.getIconPath())
        window.geometry(self.getGeometry())
        window.minsize(self.minSize[0], self.minSize[1])
        window.maxsize(self.maxSize[0], self.maxSize[1])
        window.config(background=self.background)
        window.config()
        window.mainloop()

    def getWindow(self) -> Tk:
        return self.window

    def getTitle(self) -> str:
        return self.title

    def getIconPath(self) -> str:
        return self.iconPath

    def getGeometry(self) -> str:
        return self.geometry

    def getMinSize(self) -> tuple:
        return self.minSize

    def getMaxSize(self) -> tuple:
        return self.maxSize

    def getBackground(self) -> str:
        return self.background
