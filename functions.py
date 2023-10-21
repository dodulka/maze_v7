from data import *


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, hp= None, speed= None):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.HP = hp
        self.SPEED = speed
        
class Hero(Sprite):
    def __init__(self, x, y, width, heiht, image= None, hp= 5, speed= 5):
        super().__init__(x, y, width, heiht, image, hp, speed)
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}


    def move(self, window):
            if self.MOVE["UP"] == True:
                self.y -= self.SPEED
            if self.MOVE["DOWN"] == True:
                self.y += self.SPEED
            if self.MOVE["LEFT"] == True:
                self.x -= self.SPEED
            if self.MOVE["RIGHT"] == True:
                self.x += self.SPEED

            pygame.draw.rect(window, (120,120,120), self)
