from Entity import Entity

class Food(Entity):

    def __init__(self,world,x,y):

        super(Food, self).__init__(world,size=5,x=x,y=y)
        self.value = 300
        world.addEntity(self,dynamic=False)
