import math
import random
import copy

class Node():

    def __init__(self,nextLayerWidth,bias = False):
        self.nextLayerWidth = nextLayerWidth
        self.bias = bias
        self.input = 0

        self.value = 1
        self.weights = []
        for i in range(0,nextLayerWidth):
            self.weights.append(random.uniform(-1,1))

    def activate(self):
        if not self.bias:
            self.value = self.sigmoid(self.input)


    def mutate(self,factor):
        for i in range(0,len(self.weights)):
            self.weights[i]+=random.uniform(-factor,factor)*self.weights[i]

    def sigmoid(self,x):
        return x
        return 1 / (1 + math.e ** -x)
    def getDerivative(self):
        return self.value*(1-self.value)
    def changeRandomWeight(self):

        self.weights[random.randint(0,self.nextLayerWidth-1)]=random.uniform(-10,10)

    def __str__(self):
        return "Node with weights: "+str(self.weights)+"\n"

class Layer():

    def __init__(self,width,nextLayerWidth):
        self.width = width
        self.nextLayerWidth = nextLayerWidth
        self.nodes = []
        for i in range(0,width):
            self.nodes.append(Node(nextLayerWidth))
        self.nodes.append(Node(nextLayerWidth,bias=True))

    def forwardPropagate(self,values):
        L = [0]*self.nextLayerWidth

        for i in range(0,self.width):
            self.nodes[i].input = values[i]
            self.nodes[i].activate()
            for j in range(0,self.nextLayerWidth):
                L[j]+=self.nodes[i].value*self.nodes[i].weights[j]
        return L
    def changeRandomWeight(self):
        self.nodes[random.randint(0,self.width-1)].changeRandomWeight()
    def mutate(self,factor):
        for node in self.nodes:
            node.mutate(factor)
    def __str__(self):
        S = "Layer with nodes: "
        for i in range(0,len(self.nodes)):
            S+=str(self.nodes[i])
        S+='\n'
        return S

class NeuralNetwork():

    def __init__(self,inputNodes,width,depth,outputNodes):
        self.width = width
        self.depth = depth
        self.outputNodes = outputNodes
        self.inputNodes = inputNodes
        self.layers = [Layer(inputNodes,width)]
        for i in range(0,depth-1):
            self.layers.append(Layer(width,width))
        self.layers.append(Layer(width,outputNodes))
        self.cost = 0

    def activate(self,inputValues):
        val = inputValues
        for layer in self.layers:
            val = layer.forwardPropagate(val)
        return val
    def calculateCost(self,actualoutput,desiredoutput):
        C = 0
        for i in range(self.outputNodes):
            err = abs(actualoutput[i]-desiredoutput[i])
            C+=err
        return C
    def changeRandomWeight(self):
        self.layers[random.randint(0,len(self.layers)-1)].changeRandomWeight()
    def mutate(self,factor):
        for layer in self.layers:
            layer.mutate(factor)
    def setCost(self,cost):
        self.cost = cost
    def getCost(self):
        return self.cost
    def __repr__(self):
        return str(self.cost)
    def __str__(self):
        S = ""
        for layer in self.layers:
            S+=str(layer)
        return S




def calculateCost(net,display=False):
    totalCost = 0

    totalCost += net.calculateCost(net.activate([0, 0]), [0])
    totalCost += net.calculateCost(net.activate([0, 1]), [1])
    totalCost += net.calculateCost(net.activate([1, 0]), [1])
    totalCost += net.calculateCost(net.activate([1, 1]), [0])


    if display:


        print("00", str(net.activate([0, 0])))
        print("01", str(net.activate([0, 1])))
        print("10", str(net.activate([1, 0])))
        print("11", str(net.activate([1, 1])))

    return totalCost

"""
myNet = NeuralNetwork(1,2,2,1)
print(myNet.activate([0]))
print(myNet.activate([10]))


if __name__ == "__main__":
    random.seed(25)


    currentNewcomers = []
    currentGeneration = []
    for i in range(25):
        currentNewcomers.append(NeuralNetwork(2,3,1,1))
    for i in range(0,1):
        for net in currentNewcomers:
            net.cost = calculateCost(net)

        for net in currentNewcomers:
            currentGeneration.append(net)



        print(currentNewcomers)

"""

