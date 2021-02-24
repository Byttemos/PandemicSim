import numpy as np
import pygame

class buttons:
    def __init__ (self,screen,butWidth = 50,butHeight = 50):
        self.static_color = 255,0,0
        self.hover_color = 0,255,0
        self.press_color = 0,0,255
        self.butWidth = butWidth
        self.butHeight = butHeight
        numNodesPlus = self.rect = pygame.Rect(20,20,40,40)
        numNodesMinus = self.rect = pygame.Rect(80,20,40,40)
        pygame.Surface.fill()
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()


    def press(self):
        if self.mouse_x >= 20 and self.mouse_y <= 70 and self.mouse_y >= 20 and self.mouse_y <= 70| self.mouse_x>= 80 and self.mouse_x<= 130 and self.mouse_y >= 20 and self.mouse_y <= 70:
            if pygame.mouse.get_pressed == (1,0,0):
                pygame.Surface.fill(self.press_color)

        

    def hover(self):
        if self.mouse_x >=20 & self.mouse_x <=70 & self.mouse_y >= 20 & self.mouse_y <= 70 or self.mouse_x>=80 & self.mouse_x<= 130 & self.mouse_y >= 20 & self.mouse_y <= 70:
            if pygame.mouse.get_pressed == (1,0,0):
                pygame.Surface.fill(self.hover_color)

    def static(self):
        if self.mouse_x>=20 & self.mouse_x<=70 & self.mouse_y >= 20 & self.mouse_y <= 70| self.mouse_x>=80 & self.mouse_x<= 130 & self.mouse_y >= 20 & self.mouse_y <= 70:
            if pygame.mouse.get_pressed == (1,0,0):
                pygame.Surface.fill(self.static_color)

