import pygame
from Creature import Creature
from Food import Food
import types
from random import randint

class World():

    def __init__(self,width = 800,height = 600,caption = "Simulation Window"):
        self.height=height
        self.width=width
        self.display = pygame.display.set_mode([width,height])
        pygame.display.set_caption(caption)

        self.dynamicEntities = set()
        self.staticEntities = set()
        self.children = set()

    def addEntity(self,entity,dynamic = True):
        if dynamic:
            self.children.add(entity)
        else:
            self.staticEntities.add(entity)
    def removeEntity(self,entity):
        self.dynamicEntities = set(filter(lambda x: x != entity,self.dynamicEntities))
        self.staticEntities = set(filter(lambda x: x != entity, self.staticEntities))
    def removeAllDynamicEntities(self):
        self.dynamicEntities = set()
    def removeAllStaticEntities(self):
        self.staticEntities = set()

    def performEdgeCollision(self,entity = None):

        if entity != None:
            #Y collision:
            if entity.y<0:
                entity.setPos(entity.x,0)
            elif entity.y>self.height-entity.size:
                entity.setPos(entity.x,self.height-entity.size)
            #x collision:
            if entity.x<0:
                entity.setPos(0,entity.y)
            if entity.x>self.width-entity.size:
                entity.setPos(self.width-entity.size,entity.y)
        else:
            for entity in self.dynamicEntities:
                self.performEdgeCollision(entity)
    def purgeDeadCreatures(self):
        for entity in self.dynamicEntities:
            if entity.energy<=0:
                self.dynamicEntities = set(filter(lambda x: x != entity,self.dynamicEntities))

    def spawnFood(self):
        x = randint(0,self.width)
        y = randint(0,self.height)

        self.staticEntities.add(Food(self,x,y))

    def growChildren(self):
        for child in self.children:
            self.dynamicEntities.add(child)
        self.children = set()

    def renderEntities(self):
        for entity in self.staticEntities:
            entity.draw()
        for entity in self.dynamicEntities:
            entity.draw()
            #text = pygame.font.Font.render(str(entity.energy),False,[255,0,0])
            #self.display.blit(text,entity.rect)


