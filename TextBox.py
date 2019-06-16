from SideScroller.Globals.Cache import get_font

import pygame

import PyGEFormObjects.globals as glob
from PyGEFormObjects.FormBase import FormBase


class TextBox(FormBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent):
        FormBase.__init__(self, screen, args, parent)

        self.font_name = self.get_mandatory_arguement("font", str)
        self.font = get_font(self.font_name)

        self.value = self.get_optional_arguement("text", "", list)      # type: list
        self.numeric = bool(self.get_optional_arguement("numeric", False, int))     # type: list
        self.padding = 5

        self.text = None
        self.outline = None
        self.update_text()

    def update_text(self):
        self.text = self.font.render("".join(self.value), True, glob.colors["text"])
        self.w, self.h = self.text.get_size()
        self.outline = pygame.Rect(self.x - self.padding, self.y - self.padding, self.w + (self.padding * 2), self.h + (self.padding * 2))

    def draw(self):
        pygame.draw.rect(self.screen, glob.colors["outline"], self.outline, 1)
        self.draw_to_screen(item=self.text)

    def onkeydown(self, unicode, key, modifier, scancode):
        if self.focus:
            if key == 8:
                if len(self.value) >=1:
                    del self.value[-1]
            elif key > 31:
                # printable charcters only please :)
                if self.numeric:
                    if unicode.isdigit():
                        self.value.append(unicode)
                else:
                    self.value.append(unicode)

            self.update_text()

    @property
    def rect(self):
        return self.outline.x, self.outline.y, self.outline.w, self.outline.h
