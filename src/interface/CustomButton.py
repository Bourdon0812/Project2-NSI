from tkinter import *


class CustomButton(Button):
    '''
    CustomButton extends Tkinter.Button
    '''

    def setUniqueId(self, uniqueId: int):
        self.uniqueId = uniqueId

    def getUniqueId(self) -> int:
        return self.uniqueId
