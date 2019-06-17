import pygame
from xmltodict import OrderedDict

from PyGEFormObjects.FormBase import FormBase
from PyGEFormObjects.RadioButton import RadioButton


class RadioGroup(FormBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        FormBase.__init__(self, screen, args, parent)

        self.buttons = []
        self.font_name = self.get_mandatory_arguement("font", str)
        self.padding = 5

        if "RadioButton" in args:
            y = self.y
            if type(args["RadioButton"]) is OrderedDict:
                args["RadioButton"] = [args["RadioButton"]]
            for b in args["RadioButton"]:
                arg = {}
                arg.update(args)
                arg.update(b)
                arg["@y"] = y
                rad = RadioButton(self.screen, arg, parent)
                self.buttons.append(rad)
                y += rad.h + self.padding

    def draw(self):
        for rad in self.buttons:        # type: RadioButton
            rad.draw()

    def onmousedown(self, button, pos):
        states = []
        for rad in self.buttons:        # type: RadioButton
            states.append(rad.is_touching_mouse())

        if True in states:
            for i in range(len(states)):
                self.buttons[i].checked = states[i]
