from tkinter import *
from src.interface.CustomButton import *
from src.interface.MoyenneSubInterface import MoyenneSubInterface
from src.interface.AllMoyennesSubInterface import AllMoyenneSubInterface


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
        self.genButtons()
        self.subInterface = None
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

    def genHeader(self):
        '''
        genere le bandeau situé en haut de la page avec l'image du professeur et le titre
        :return: void
        '''
        header_frame = Frame(self.getBaseFrame(), bg="blue", pady=20)
        header_frame.pack(fill=X)

        canvas = Canvas(header_frame, width=75, height=75, bg="blue", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT)

        canvas.create_image(75 / 2, 75 / 2, image=self.imageHeader)

        title: Label = Label(
            header_frame,
            text="Interface professeur",
            font=("Arial", 30),
            fg="white",
            bg="red",
            relief=SUNKEN
        )
        title.pack(side=LEFT, padx=125, pady=10)

    def genButtons(self):
        '''
        genère les buttons de l'interface
        :return: void
        '''
        from src.events.CustomButtonClickedListener import onClick
        from src.utils.InterfaceManager import \
            customButtonsData, \
            eleveMoyenneButtonName, \
            devoirMoyenneButtonName, \
            viewAllMoyenneButtonName
        button_frame: Frame = Frame(self.getBaseFrame(), bg="#535353", pady=40)
        button_frame.pack(side=LEFT, fill=BOTH, expand=True)

        exitButton: Button = Button(button_frame, text="Quitter pronote", bg="red", fg="white", command=self.onQuit)
        exitButton.grid(row=0, column=0, sticky="ne", padx=0, pady=10)

        getMoyenneByEleveButton: CustomButton = CustomButton(
            button_frame,
            text=customButtonsData[eleveMoyenneButtonName]["title"],
            bg="blue",
            fg="white",
            command=lambda: onClick(customButtonsData[eleveMoyenneButtonName]["id"], self)
        )
        getMoyenneByEleveButton.setUniqueId(customButtonsData[eleveMoyenneButtonName]["id"])
        getMoyenneByEleveButton.grid(row=0, column=0, sticky="w", padx=250, pady=15)

        getMoyenneDevoirButton: CustomButton = CustomButton(
            button_frame,
            text=customButtonsData[devoirMoyenneButtonName]["title"],
            bg="blue",
            fg="white",
            command=lambda: onClick(customButtonsData[devoirMoyenneButtonName]["id"], self)
        )
        getMoyenneDevoirButton.setUniqueId(customButtonsData[devoirMoyenneButtonName]["id"])
        getMoyenneDevoirButton.grid(row=1, column=0, sticky="w", padx=250, pady=15)

        viewMoyennesButton: CustomButton = CustomButton(
            button_frame,
            text=customButtonsData[viewAllMoyenneButtonName]["title"],
            bg="blue",
            fg="white",
            command=lambda: onClick(customButtonsData[viewAllMoyenneButtonName]["id"], self)
        )
        viewMoyennesButton.setUniqueId(customButtonsData[viewAllMoyenneButtonName]["id"])
        viewMoyennesButton.grid(row=2, column=0, sticky="w", padx=250, pady=15)

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

    def hasSubInterfaceOpen(self) -> bool:
        return not self.getSubInterface() is None

    def setSubInterfaceOpen(self, subInterface: MoyenneSubInterface | AllMoyenneSubInterface | None):
        self.subInterface = subInterface

    def getSubInterface(self) -> None | MoyenneSubInterface | AllMoyenneSubInterface:
        return self.subInterface

    def onQuit(self):
        if self.hasSubInterfaceOpen():
            self.getSubInterface().onQuit()
        self.getWindow().destroy()
