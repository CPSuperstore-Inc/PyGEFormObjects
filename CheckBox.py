from SideScroller.Globals.Cache import get_font

import pygame

import PyGEFormObjects.globals as glob
from PyGEFormObjects.FormBase import FormBase
from PyGEFormObjects.Label import Label


class CheckBox(FormBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        FormBase.__init__(self, screen, args, parent)
        self.label = Label(screen, args, parent)

        self.padding = 5
        self.fill_padding = 5

        self.label.move(self.label.h + self.padding, 0, fire_onscreen_event=False)

        self.checked = self.get_optional_arguement("text", str)

        self.outline_color = glob.colors["outline"]
        self.inside_color = glob.colors["inside"]

        self.w, self.h = self.label.get_size()

        self.outline = pygame.Rect(self.x, self.y, self.label.h, self.label.h)
        self.internal = pygame.Rect(self.x + self.fill_padding, self.y + self.fill_padding, self.label.h - (self.fill_padding * 2), self.label.h - (self.fill_padding * 2))

    def draw(self):
        pygame.draw.rect(self.screen, self.outline_color, self.outline, 1)
        if self.checked:
            pygame.draw.rect(self.screen, self.inside_color, self.internal, 0)
        self.label.draw()

    def onclick(self, button, pos):
        self.checked = not self.checked

    @property
    def rect(self):
        return self.outline.x, self.outline.y, self.outline.w, self.outline.h
