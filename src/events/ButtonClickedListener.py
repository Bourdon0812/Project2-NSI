from tkinter import *
from src.utils.InterfaceManager import *


def onClick(customButtonId: int):
    '''
    fonction executer lorsqu'un des 3 customButton est cliqué
    :param customButtonId:
    :param currentInterface:
    :return:
    '''
    if customButtonId == customButtonsData[eleveMoyenneButtonName]["id"]:
        print("1")
        #currentInterface.onQuit()
    elif customButtonId == customButtonsData[devoirMoyenneButtonName]["id"]:
        print("2")
        #currentInterface.onQuit()
    elif customButtonId == customButtonsData[viewAllMoyenneButtonName]["id"]:
        print("3")
        #currentInterface.onQuit()
