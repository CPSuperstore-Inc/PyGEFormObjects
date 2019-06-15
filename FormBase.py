from SideScroller.Objects.ObjectBase import ObjectBase

import pygame


class FormBase(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        ObjectBase.__init__(self, screen, args, parent)
        self.focus = self.get_optional_arguement("focus", False, bool)

    def onclick(self, button, pos):
        self.focus = True

    def onnotclick(self, button, pos):
        self.focus = False