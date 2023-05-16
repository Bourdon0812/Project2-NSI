from tkinter import *

from src.interface.MainInterface import MainInterface

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
        "title": "Voir la moyenne de tout les élèves",
        "id": 2
    }
}

subInterfaceData: dict = {
    customButtonsData[eleveMoyenneButtonName]["id"]: {
        "title": "Pronote",
        "icon": '../resources/icon.ico',
        "geometry": "720x480",
        "minSize": (720, 480),
        "maxSize": (720, 480),
        "background": "#535353",
        "header": "Moyenne élève",
        "labelInput": "Saisissez nom de l'élève : "
    },
    customButtonsData[devoirMoyenneButtonName]["id"]: {
        "title": "Pronote",
        "icon": '../resources/icon.ico',
        "geometry": "720x480",
        "minSize": (720, 480),
        "maxSize": (720, 480),
        "background": "#535353",
        "header": "Moyenne devoir",
        "labelInput": "Saisissez nom du devoir : "
    },
    customButtonsData[viewAllMoyenneButtonName]["id"]: {
        "title": "Pronote",
        "icon": '../resources/icon.ico',
        "geometry": "480x480",
        "minSize": (480, 480),
        "maxSize": (480, 1080),
        "background": "white",
        "header": "moyennes",
    }
}

window: Tk = Tk()

mainInterface: MainInterface | None = None


def initInterfaceManager() -> None:
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


def getSubInterfaceData(id: int) -> dict:
    return subInterfaceData[id]


def openMoyenneSubInterface(id: int, currentInterface: MainInterface) -> None:
    global mainInterface
    if mainInterface is None:
        mainInterface = currentInterface
    from src.interface.MoyenneSubInterface import MoyenneSubInterface
    subInterface: MoyenneSubInterface = MoyenneSubInterface(id)
    currentInterface.setSubInterfaceOpen(subInterface)
    subInterface.genWindow()


def closeSubInterface() -> None:
    global mainInterface
    if not mainInterface is None:
        mainInterface.setSubInterfaceOpen(None)


def openViewAllMoyenneSubInterface(id, currentInterface: MainInterface) -> None:
    from src.interface.AllMoyennesSubInterface import AllMoyenneSubInterface
    subInterface: AllMoyenneSubInterface = AllMoyenneSubInterface(id)
    subInterface.genWindow()
    currentInterface.setSubInterfaceOpen(subInterface)
