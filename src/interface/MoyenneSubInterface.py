from tkinter import *


class MoyenneSubInterface:

    def __init__(self, openWithButtonId: int):
        from src.utils.InterfaceManager import getSubInterfaceData
        self.window: Tk = Tk()
        self.id = openWithButtonId
        self.data = getSubInterfaceData(openWithButtonId)
        self.baseFrame: Frame = Frame(self.window, bg=self.getData()["background"])
        self.contentFrame: Frame | None = None

        self.input: Entry | None = None

    def genWindow(self):
        window: Tk = self.getWindow()
        window.title(self.getData()["title"])
        window.iconbitmap(self.getData()["icon"])
        window.geometry(self.getData()["geometry"])
        window.minsize(self.getData()["minSize"][0], self.getData()["minSize"][1])
        window.maxsize(self.getData()["maxSize"][0], self.getData()["maxSize"][1])
        window.config(background=self.getData()["background"])

        self.baseFrame.pack(fill=X)
        self.genHeader()
        self.genContent()
        window.protocol("WM_DELETE_WINDOW", self.onQuit)
        window.mainloop()

    def genHeader(self):
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
        title.pack(side=LEFT, padx=250, pady=10)

    def genContent(self):
        from src.events.KeyReleaseListener import onRelease
        from src.events.SubmitButtonClickedListener import onClick
        content_frame = Frame(self.baseFrame, bg=self.getData()["background"], pady=50)
        self.contentFrame = content_frame
        content_frame.pack(fill=BOTH, expand=True)

        exitButton: Button = Button(content_frame, text="Revenir page principal", bg="red", fg="white",
                                    command=self.onQuit)
        exitButton.grid(row=0, column=4, sticky="ne", padx=40, pady=5)

        text = self.getData()["labelInput"]
        instruction: Label = Label(content_frame, text=text, bg="#535353", font=("Arial", 15), fg="white")
        instruction.grid(row=1, column=0, sticky="w", padx=10, pady=30)

        input_entry = Entry(content_frame)
        input_entry.grid(row=1, column=1, sticky="w", padx=10, pady=30)
        input_entry.bind("<KeyRelease>", lambda event: onRelease(self))
        self.input = input_entry

        red_square = Label(content_frame, bg="red", width=4, height=2)
        red_square.grid(row=1, column=2, sticky="w", padx=10, pady=30)

        send_button = Button(content_frame, text="Envoyer", bg="blue", command=lambda: onClick(self))
        send_button.grid(row=1, column=3, sticky="w", padx=10, pady=30)

    def getId(self) -> int:
        return self.id

    def getData(self) -> dict:
        return self.data

    def getWindow(self) -> Tk:
        return self.window

    def getInput(self) -> None | Entry:
        return self.input

    def getContentFrame(self) -> None | Frame:
        return self.contentFrame

    def onQuit(self):
        from src.utils.InterfaceManager import closeSubInterface
        self.getWindow().destroy()
        closeSubInterface()