from SideScroller.Objects.ObjectBase import ObjectBase
from SideScroller.Globals.Cache import get_font
from SideScroller.utils import convert_color

import pygame

import PyGEFormObjects.globals as glob


class Button(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        ObjectBase.__init__(self, screen, args, parent)

        self.font_name = self.get_mandatory_arguement("font", str)
        self.font = get_font(self.font_name)

        self.value = self.get_mandatory_arguement("text", str)
        self.text = self.font.render(self.value, True, convert_color(glob.colors["text"]))

        self.outline_color = convert_color(glob.colors["outline"])

        self.w, self.h = self.text.get_size()

        self.padding = 5

        self.outline = pygame.Rect(self.x - self.padding, self.y - self.padding, self.w + (self.padding * 2), self.h + (self.padding * 2))

    def draw(self):
        pygame.draw.rect(self.screen, self.outline_color, self.outline, 1)
        self.draw_to_screen(self.text)

    def onclick(self, button, pos):
        print("click")

    @property
    def rect(self):
        return self.outline.x, self.outline.y, self.outline.w, self.outline.h
