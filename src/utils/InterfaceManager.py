from src.interface.MainInterface import MainInterface
from tkinter import *

mainInterfaceData: dict = {
    "title": "Pronote",
    "icon": '../resources/icon.ico',
    "geometry": "720x480",
    "minSize": (720, 480),
    "maxSize": (720, 480),
    "background": "#535353"
}

eleveMoyenneButtonName: str = "eleveMoyenneButton"
devoirMoyenneButtonName: str = "devoirMoyenneButton"
viewAllMoyenneButtonName: str = "viewAllMoyennesButton"

customButtonsData: dict = {
    eleveMoyenneButtonName: {
        "title": "Voir la moyenne d'un éléve           ",
        "id": 0
    },
    devoirMoyenneButtonName: {
        "title": "Voir la moyenne d'un devoir         ",
        "id": 1
    },
    viewAllMoyenneButtonName: {
        "title": "Voir la moyenne de tout les éléves",
        "id": 2
    }
}

window: Tk = Tk()


def init():
    '''
    init program
    :return void:
    '''
    main: MainInterface = MainInterface(
        window,
        mainInterfaceData["title"],
        mainInterfaceData["icon"],
        mainInterfaceData["geometry"],
        mainInterfaceData["minSize"],
        mainInterfaceData["maxSize"],
        mainInterfaceData["background"]
    )
