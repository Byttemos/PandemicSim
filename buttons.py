import numpy as np
import pygame

class buttons:
    def __init__ (self,screen,butWidth = 50,butHeight = 50):
        self.static_color = 255,0,0
        self.hover_color = 0,255,0
        self.press_color = 0,0,255
        self.butWidth = butWidth
        self.butHeight = butHeight
        numNodesPlus = self.rect = Rect(20,20,40,40)
        numNodesMinus = self.rect = Rect(80,20,40,40)
        pygame.Surface.fill()
        mouse_x,mouse_y = pygame.mouse.get_pos()


    def press(self):
    if mouse_x>= 20 and mouse_x<= 70 and mouse_y >= 20 and mouse_y <= 70| mouse_x>= 80 and mouse_x<= 130 and mouse_y >= 20 and mouse_y <= 70:
        if pygame.mouse.get_pressed == (1,0,0):
            pygame.Surface.fill()=self.press_color

        

    def hover(self)
    if mouse_x>=20 & mouse_x<=70 & mouse_y >= 20 & mouse_y <= 70 or mouse_x>=80 & mouse_x<= 130 & mouse_y >= 20 & mouse_y <= 70:
        if pygame.mouse.get_pressed == (1,0,0):
            pygame.Surface.fill()=self.hover.color

    def static(self)
    if mouse_x>=20 & mouse_x<=70 & mouse_y >= 20 & mouse_y <= 70| mouse_x>=80 & mouse_x<= 130 & mouse_y >= 20 & mouse_y <= 70:
        if pygame.mouse.get_pressed == (1,0,0):
            pygame.Surface.fill()=self.static_color

