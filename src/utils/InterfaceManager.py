from src.interface.MainInterface import MainInterface
from tkinter import *

data: dict = {
    "title": "Pronote",
    "icon": '../resources/icon.ico',
    "geometry": "720x480",
    "minSize": (720, 480),
    "maxSize": (720, 480),
    "background": "#535353"
}

window: Tk = Tk()


def init():
    '''
    init program
    :return void:
    '''
    main: MainInterface = MainInterface(
        window,
        data["title"],
        data["icon"],
        data["geometry"],
        data["minSize"],
        data["maxSize"],
        data["background"]
    )
