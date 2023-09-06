
class Perceptron:

    def __init__(self):

        self.w0 = 0.0
        self.w1 = 0.0
        self.bias = 0.0
        self.x0 = 0.0
        self.x1 = 0.0
        self.y = 0.0

    #* Getters y setters
    def setW0(self,w):
        self.w0 = w

    def getW0(self):
        return self.w0
    
    def setW1(self,w):
        self.w1 = w

    def getW1(self):
        return self.w1
    
    def setBias(self, b):
        self.bias = b

    def getBias(self):
        return self.bias

    def setX0(self, x):
        self.x0 = x
    
    def getX0(self):
        return self.x0
    
    def setX1(self, x):
        self.x1 = x

    def getX1(self):
        return self.x1
    
    def setY(self, v):
        self.y = v

    def getY(self):
        return self.y

    #*Funcion de activacion
    def funcActivacion(self, out):
        if out>=0:
            return 1
        return -1
    