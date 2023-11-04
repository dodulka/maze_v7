from data import *


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height=None, speed=None, hp=None, image=None):
        super().__init__(x, y, width, height)
        self.HP = hp
        self.SPEED = speed
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[1]
        self.IMAGE_NOW = self.IMAGE
        self.IMAGE_COUNT = 0
    
    def move_image(self):
        self.IMAGE_COUNT += 1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]

class Hero(Sprite):
    def __init__(self, x, y, width, height, image=None, hp=5, speed=5):
        super().__init__(x, y, width, height, speed, hp, image)
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
        self.DIRECTION = False

    def move(self, window):
        if self.MOVE["UP"] == True and self.y > 0:
            self.y -= self.SPEED
        if self.MOVE["DOWN"] == True and self.y + self.height < setting_win["HEIGHT"]:
            self.y += self.SPEED
        if self.MOVE["LEFT"] == True and self.x > 0: 
            self.x -= self.SPEED
            self.DIRECTION = False
        if self.MOVE["RIGHT"] == True and self.x + self.width < setting_win["WIDTH"]: 
            self.x += self.SPEED
            self.DIRECTION = True

        if self.MOVE["UP"] == False and self.MOVE["DOWN"] == False and self.MOVE["LEFT"] == False and self.MOVE["RIGHT"] == False:
            self.IMAGE = self.IMAGE_LIST[1]
        else:
            self.move_image()

        if self.DIRECTION == True:
            self.IMAGE_NOW = pygame.transform.flip(self.IMAGE, True, False)
        else:
            self.IMAGE_NOW = self.IMAGE

        window.blit(self.IMAGE_NOW, (self.x, self.y))
       

class Bot(Sprite):
    def __init__(self, x, y, width, height, image= None, hp= None, speed= 5, horizontal= None, vertical= None):
        super().__init__(x, y, width, height, image, hp, speed)
        self.HORIZONTAL = horizontal
        self.VERTICAL = vertical
        self.BULLET = pygame.Rect(self.x, self.centery, 20, 10)

    def move(self, window):
        if self.HORIZONTAL == True:
            self.x += self.SPEED
        if self.VERTICAL == True:
            self.y += self.SPEED
        
        if self.x < 0 or self.right > setting_win["WIDTH"] or self.f.bottom > setting_win["HEIGHT"] or self.collidelist(wall_list) != -1:
            self.SPEED *= -1 
        
        window.blit(self.IMAGE_NOW, (self.x, self.y))
        self.move_image()

        def shoot(self,window,hero):
            window.blit(self.IMAGE_NOW, (self.x, self.y))
            self.move_image()
            if self.HORIZONTAL == True:
                self.BULLET.x += self.SPEED
            if self.VERTICAL == True:
                self.BULLET.y += self.SPEED
            if self.BULLET.coliderect(hero):
                self.BULLET.x = self.x
                self.BULLET.y = self.centery
                hero.HP -= 1
                hero.x, hero.y = 10, 10
            if self.BULLET.x < 0 or self.BULLET.right > setting_win["WIDTH"] or self.BULLET.y < 0 or self.BULLET.y > setting_win["HEIGHT"]
                self.BULLET.y = self.centery
            window.blit(self.IMAGE_NOW, (self.x, self.y))
            
def create_wall(map_now):
    x, y = 0, 0
    index_x, index_y = 0, 0
    width = 20

    for string in  map_now:
        for elem in string:
            #vertical
            if elem == "1":
                index = index_y
                for i in range(index, len(map_now)):
                    if map_now[i][index_x] == "2":
                        wall_list.append(pygame.Rect(x, y, width, (i - index_y) * width + width))
                        break
            #horizontal
            if elem == "3":
                index = index_x
                for i in range(index, len(map_now[0])):
                    if map_now[index_y][i] == "2":
                        wall_list.append(pygame.Rect(x, y, (i - index_x) * width + width, width))
                        break
            x += width
            index_x += 1
        x = 0
        index_x = 0
        y += width
        index_y += 1

create_wall(maps["MAP1"])