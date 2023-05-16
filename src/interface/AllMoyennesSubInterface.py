from tkinter import *

class AllMoyenneSubInterface:

    def __init__(self, id):
        from src.utils.InterfaceManager import subInterfaceData
        self.window: Tk = Tk()
        self.baseFrame: Frame = Frame(self.window, bg="white")
        self.data = subInterfaceData[id]


    def genWindow(self):
        window: Tk = self.getWindow()
        window.title(self.getData()["title"])
        window.iconbitmap(self.getData()["icon"])
        window.geometry(self.getData()["geometry"])
        window.minsize(self.getData()["minSize"][0], self.getData()["minSize"][1])
        window.maxsize(self.getData()["maxSize"][0], self.getData()["maxSize"][1])
        window.config(background=self.getData()["background"])

        self.baseFrame.pack(fill=BOTH, expand=True)
        self.genHeader()
        self.genContent()
        window.protocol("WM_DELETE_WINDOW", self.onQuit)
        window.mainloop()

    def genHeader(self):
        header_frame = Frame(self.getBaseFrame(), bg="#17AA67", pady=20)
        header_frame.pack(fill=X)

        title: Label = Label(
            header_frame,
            text="Moyenne des élèves",
            font=("Arial", 30),
            fg="white",
            bg="#17AA67",
        )
        title.pack(side=LEFT, padx=125, pady=10)

    def genContent(self):
        from src.utils.PronoteManager import moyennesDecroissant, getTable

        content_frame = Frame(self.baseFrame, bg=self.getData()["background"])
        content_frame.pack(fill=BOTH, expand=True)

        scrollbar = Scrollbar(content_frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas = Canvas(content_frame, bg=self.getData()["background"], yscrollcommand=scrollbar.set)
        canvas.pack(fill=BOTH, expand=True)

        inner_frame = Frame(canvas, bg=self.getData()["background"])
        inner_frame.pack(fill=BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        canvas.create_window(0, 0, anchor=NW, window=inner_frame)

        def onCanvasConfigure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind('<Configure>', onCanvasConfigure)

        exitButton: Button = Button(inner_frame, text="Revenir à la page principale", bg="red", fg="white",
        command=self.onQuit)
        exitButton.grid(row=0, column=4, sticky="ne", padx=40, pady=5)
        moyennes = moyennesDecroissant(getTable())
        for i in range(len(moyennes)):
            nom: Label = Label(inner_frame, text=moyennes[i][0])
            nom.grid(row=i + 1, column=0, sticky="ne", padx=40, pady=5)
            note: Label = Label(inner_frame, text=moyennes[i][1])
            note.grid(row=i + 1, column=1, sticky="ne", padx=40, pady=5)

    def getWindow(self) -> Tk:
        return self.window

    def getBaseFrame(self):
        return self.baseFrame

    def getData(self):
        return self.data

    def onQuit(self):
        from src.utils.InterfaceManager import closeSubInterface
        self.getWindow().destroy()
        closeSubInterface()



