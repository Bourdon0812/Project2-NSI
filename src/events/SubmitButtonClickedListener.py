from src.interface.MoyenneSubInterface import *
from src.utils.InterfaceManager import *
from src.utils.PronoteManager import *
from tkinter.messagebox import *


def onClick(interface: MoyenneSubInterface):
    inputContent: str = interface.getInput().get()
    frame = interface.getContentFrame()

    if interface.getId() == customButtonsData[eleveMoyenneButtonName]["id"]:
        moy = getMoyenneByEleve(inputContent)
        if not moy is None:
            response = Label(
                frame,
                fg="green",
                bg="#535353",
                font=("Arial", 24),
                text="La moyenne de " + inputContent + " est de " + str(moy)
            )
            response.grid(row=3, column=0, columnspan=5, sticky="w", padx=10, pady=30)
        else:
            showerror("Pronote", inputContent + " n'est pas un élève de l'établissement")

    elif interface.getId() == customButtonsData[devoirMoyenneButtonName]["id"]:
        moy = getMoyenneByDevoir(inputContent)
        if not moy is None:
            response = Label(
                frame,
                fg="green",
                bg="#535353",
                font=("Arial", 24),
                text="La moyenne du devoir " + inputContent + " est de " + str(moy))
            response.grid(row=3, column=0, columnspan=5, sticky="w", padx=10, pady=30)
        else:
            showerror("Pronote", inputContent + " n'est pas un devoir")