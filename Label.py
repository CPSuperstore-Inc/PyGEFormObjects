from SideScroller.Objects.ObjectBase import ObjectBase
from SideScroller.Globals.Cache import get_font
from SideScroller.utils import convert_color

import pygame

import PyGEFormObjects.globals as glob


class Label(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        ObjectBase.__init__(self, screen, args, parent)

        self.font_name = self.get_mandatory_arguement("font", str)
        self.font = get_font(self.font_name)

        self.value = self.get_mandatory_arguement("text", str)
        self.text = self.font.render(self.value, True, convert_color(glob.colors["text"]))

        self.w, self.h = self.text.get_size()


    def draw(self):
        self.draw_to_screen(self.text)

