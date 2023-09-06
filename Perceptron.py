import numpy as np

class Perceptron:

    def __init__(self):

        self.w0 = 0.0
        self.w1 = 0.0
        self.bias = 0.0
        self.x0 = 0.0
        self.x1 = 0.0
        self.y = 0.0

    #*Funcion de activacion
    def funcActivacion(self, out):
        if out>=0:
            return 1
        return -1
    
    def sumatoria(self):

        return (self.x0*self.w0) + (self.x1*self.w1) + self.bias
    
    def ajustaPesos(self,factorAprendizaje, error):

        self.setBias(factorAprendizaje*error)
        self.setW0(factorAprendizaje * error * self.x0)
        self.setW1(factorAprendizaje * error * self.x1)

    #*Funcion que servirá tanto para entrenamiento como para los datos reales
    #!data = datos del csv
    def startPerceptron(self, data, factorAprendizaje=0.4,maxEpocas=100):

        row = []
        error = 0

        for epoca in range(maxEpocas):

            error = 0
            #! Si obtiene un valor distinto al esperado, sale del loop y comienza de nuevo
            for i in range(len(data)):

                #* Coloca las entradas
                row = data[i]
                self.setX0(float(row[0]))
                self.setX1(float(row[1]))
                self.setY(float(row[2]))
                #*Obtiene el valor Y
                sum = (self.sumatoria())

                #*Calcula el error (valor deseado - Y)
                error = self.getY() - (self.funcActivacion(sum))

                #! Si el error es diferente de 0, se ajustan los pesos y comienza de nuevo
                if error != 0:
                    self.ajustaPesos(factorAprendizaje, error)
                    break


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