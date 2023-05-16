from tkinter import *
from tkinter.messagebox import *
from src.utils.InterfaceManager import *
from src.interface.MainInterface import *


def onClick(customButtonId: int, currentInterface: MainInterface):
    '''
    fonction executer lorsqu'un des 3 customButton est cliqué
    :param customButtonId:
    :param currentInterface:
    :return:
    '''
    if currentInterface.hasSubInterfaceOpen():
        showerror("Pronote", "Vous avez déjà une sous fenêtre d'ouverte")
        return

    if customButtonId == customButtonsData[eleveMoyenneButtonName]["id"]:
        openMoyenneSubInterface(customButtonId, currentInterface)

    elif customButtonId == customButtonsData[devoirMoyenneButtonName]["id"]:
        openMoyenneSubInterface(customButtonId, currentInterface)

    elif customButtonId == customButtonsData[viewAllMoyenneButtonName]["id"]:
        openViewAllMoyenneSubInterface(customButtonId, currentInterface)
