from tkinter import *
from src.interface.MoyenneSubInterface import MoyenneSubInterface
from src.utils.PronoteManager import *

def onRelease(interface: MoyenneSubInterface):
    '''
    Fonction call lorsqu'une touche est relaché dans un input d'une Sous page
    :param interface: MoyenneSubInterface
    :return:
    '''
    from src.utils.InterfaceManager import customButtonsData, eleveMoyenneButtonName, devoirMoyenneButtonName

    input: Entry = interface.getInput()
    frame: Frame = interface.getContentFrame()
    inputContent = input.get()

    if interface.getId() == customButtonsData[eleveMoyenneButtonName]["id"]:
        if not getMoyenneByEleve(inputContent) is None:
            red_square = Label(frame, bg="green", width=4, height=2)
            red_square.grid(row=1, column=2, sticky="w", padx=10, pady=30)
        else:
            red_square = Label(frame, bg="red", width=4, height=2)
            red_square.grid(row=1, column=2, sticky="w", padx=10, pady=30)

    elif interface.getId() == customButtonsData[devoirMoyenneButtonName]["id"]:
        if not getMoyenneByDevoir(inputContent) is None:
            red_square = Label(frame, bg="green", width=4, height=2)
            red_square.grid(row=1, column=2, sticky="w", padx=10, pady=30)
        else:
            red_square = Label(frame, bg="red", width=4, height=2)
            red_square.grid(row=1, column=2, sticky="w", padx=10, pady=30)
