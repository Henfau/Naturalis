import pygame

class Entity():

    def __init__(self,world,size = 50,x = 200,y = 200):
        self.world = world
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x,y,size,size)

    def setPos(self,x,y):
        self.x = x
        self.y = y

        self.rect.x = x
        self.rect.y = y

    def move(self,x,y):
        self.x += x
        self.y += y
        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self,color = [0,0,0]):
        pygame.draw.rect(self.world.display,color,self.rect)

    def makeAction(self):
        pass
