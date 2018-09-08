from naturalis import NeuralNetwork
import pygame
import random


class Creature():

    def __init__(self,rect):
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self.brain = NeuralNetwork(2,5,3,2)
        self.energy = 1000


    def act(self,bestVector):
        res = self.brain.activate(bestVector)
        val = (res[0]**2+res[1]**2)**(1/2)
        self.x+=res[0]/val
        self.y+=res[1]/val

        self.rect.x = self.x
        self.rect.y = self.y
        return res[0]/val,res[1]/val


    def getX(self):
        return self.rect.x
    def getY(self):
        return self.rect.y
    def setPos(self,x,y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

if __name__ == "__main__":

    rec = pygame.Rect(200,200,50,50)
    random.seed(2)

    c = Creature(rec)
    print(c.act())

    for i in range(10000):
        c.act()
        #print(rec.x,rec.y)
    print(c.act())