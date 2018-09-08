from naturalis import NeuralNetwork
import pygame
from Entities.world import World
from Creature import Creature

white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

DISPLAYWIDTH = 1600
DISPLAYHEIGHT = 900


def main():
    F = 0
    pygame.init()

    world = World(width = DISPLAYWIDTH,height=DISPLAYHEIGHT)
    defaultBrain = NeuralNetwork(4,5,3,2)
    box = Creature(world,999,defaultBrain)
    clock = pygame.time.Clock()
    world.spawnFood()
    running = True
    while running:
        clock.tick()
        #Event phase
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
                pygame.quit()

        #Update phase
        for entity in world.dynamicEntities:
            entity.expendEnergy()
            entity.makeAction()


        F+=1
        if F == 15:
            world.spawnFood()
            F=0

        world.performEdgeCollision()
        world.purgeDeadCreatures()
        world.growChildren()
        if not world.dynamicEntities:
            world.staticEntities = set()
            world.dynamicEntities.add(Creature(world,999,NeuralNetwork(4,5,3,2)))
            world.spawnFood()

        #Render phase
        world.display.fill(white)

        world.renderEntities()

        pygame.display.update()

if __name__ == "__main__":
    main()