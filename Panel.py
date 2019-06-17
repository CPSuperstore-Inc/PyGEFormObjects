from SideScroller.Globals.Cache import get_font

import pygame

import PyGEFormObjects.globals as glob
from PyGEFormObjects.FormBase import FormBase


class Panel(FormBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        FormBase.__init__(self, screen, args, parent)

        self.w = self.get_mandatory_arguement("w", int)
        self.h = self.get_mandatory_arguement("h", int)

        self.panel = pygame.Rect(self.x, self.y, self.w, self.h)

        self.background = glob.colors["background"]

    def draw(self):
        pygame.draw.rect(self.screen, self.background, self.panel)
