from tkinter import *


class MoyenneSubInterface:

    def __init__(self, openWithButtonId: int):
        from src.utils.InterfaceManager import getSubInterfaceData
        self.window: Tk = Tk()
        self.id = openWithButtonId
        self.data = getSubInterfaceData(openWithButtonId)
        self.baseFrame: Frame = Frame(self.window, bg=self.getData()["background"])

    def genWindow(self):
        window: Tk = self.getWindow()
        window.title(self.getData()["title"])
        window.iconbitmap(self.getData()["icon"])
        window.geometry(self.getData()["geometry"])
        window.minsize(self.getData()["minSize"][0], self.getData()["minSize"][1])
        window.maxsize(self.getData()["maxSize"][0], self.getData()["maxSize"][0])
        window.config(background=self.getData()["background"])

        self.baseFrame.pack(fill=X)
        self.genHeader()
        window.protocol("WM_DELETE_WINDOW", self.onQuit)
        window.mainloop()

    def genHeader(self):
        '''
        genere le bandeau situé en haut de la page avec l'image du professeur et le titre
        :return: void
        '''
        header_frame = Frame(self.baseFrame, bg="blue", pady=20)
        header_frame.pack(fill=X)
        text = self.getData()["header"]
        title: Label = Label(
            header_frame,
            text=text,
            font=("Arial", 24),
            fg="white",
            bg="red",
            relief=SUNKEN
        )
        title.pack(side=LEFT, padx=50, pady=10)

    def getId(self) -> int:
        return self.id

    def getData(self) -> dict:
        return self.data

    def getWindow(self) -> Tk:
        return self.window

    def onQuit(self):
        from src.utils.InterfaceManager import closeSubInterface
        self.getWindow().destroy()
        closeSubInterface()


