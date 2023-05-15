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
        self.genWindow()
        self.baseFrame: Frame = Frame(self.window, bg=self.getBackground())
        # Obliger de stocker l'image en propriete de la class pour pas quue la variable se detruise apres
        # execution d'une fonction
        self.imageHeader: PhotoImage = PhotoImage(file="../resources/header.png").zoom(2).subsample(20)
        self.genHeader()

        self.baseFrame.pack(fill=X)
        window.mainloop()

    def genWindow(self):
        '''
        genere la fenetre de base
        :return void:
        '''
        window = self.getWindow()
        window.title(self.getTitle())
        window.iconbitmap(self.getIconPath())
        window.geometry(self.getGeometry())
        window.minsize(self.getMinSize()[0], self.getMinSize()[1])
        window.maxsize(self.getMaxSize()[0], self.getMaxSize()[1])
        window.config(background=self.background)
        window.config()

    def genHeader(self):
        '''
        genere le bandeau situé en haut de la page avec l'image du professeur et le titre
        :return: void
        '''
        header_frame = Frame(self.getBaseFrame(), bg="green")
        header_frame.pack(fill=X)

        canvas = Canvas(header_frame, width=75, height=75, bg="green", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT)

        canvas.create_image(75 / 2, 75 / 2, image=self.imageHeader)

        title: Label = Label(
            header_frame,
            text="Interface professeur",
            font=("Arial", 30),
            fg="white",
            bg="green",
            relief=SUNKEN
        )
        title.pack(side=LEFT, padx=125, pady=10)

    def genButtons(self):
        '''
        genère les buttons de l'interface
        :return:
        '''

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

    def getBaseFrame(self) -> Frame:
        return self.baseFrame
