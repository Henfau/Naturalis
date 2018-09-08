from Entity import Entity
import random
import copy

class Creature(Entity):

    def __init__(self,world,startingEnergy,brain,x=200,y=200):
        super(Creature, self).__init__(world,50,x,y)
        self.brain = brain
        self.energy = startingEnergy
        self.speed = 7
        self.value = 1000
        world.addEntity(self)

    def expendEnergy(self):

        if self.energy>=1500:
            self.energy-=700
            self.breed()

        self.energy-=2


    def makeAction(self):
        #neural net input for the weeeen!
        foodX,foodY = self.findClosestFood()
        creX,creY = self.findClosestCreature()

        inputList = [foodX,foodY,creX,creY]
        for element in inputList:
            element /=1000

        result = self.brain.activate(inputList)
        val = (result[0] ** 2 + result[1] ** 2) ** (1 / 2)
        if val != 0:
            result[0],result[1]=result[0]/val,result[1]/val
        self.move(result[0],result[1])

    def consume(self,food):

        self.energy+= food.value
        self.world.removeEntity(food)
    def findClosestCreature(self):
        bestVector = [10000, 10000]
        for f in self.world.dynamicEntities:
            if self.rect.colliderect(f.rect):
                #Mulighet for kannibalisme her
                pass
            if bestVector[0] ** 2 + bestVector[1] ** 2 > (f.x - self.x) ** 2 + (f.y - self.y) ** 2:
                bestVector = [f.x - self.x, f.y - self.y]
        if bestVector == [10000, 10000]:
            return 0, 0
        return bestVector[0], bestVector[1]


    def findClosestFood(self):

        bestVector = [10000, 10000]
        for f in self.world.staticEntities:
            if self.rect.colliderect(f.rect):
                self.consume(f)
                break
            if bestVector[0] ** 2 + bestVector[1] ** 2 > (f.x - self.x) ** 2 + (f.y - self.y) ** 2:
                bestVector = [f.x - self.x, f.y - self.y]
        if bestVector == [10000,10000]:
            return 0,0
        return bestVector[0],bestVector[1]


    def breed(self):
        print("BREEDING")
        offspringBrain = copy.deepcopy(self.brain)
        offspringBrain.mutate(0.1)
        child = Creature(self.world,500,offspringBrain,x=self.x,y=self.y)
        child.speed +=random.uniform(-0.2,0.2)*child.speed