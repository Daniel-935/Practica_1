from Perceptron import Perceptron

import csv
import numpy as np

trainingSet = []
with open('XOR_trn.csv','r') as trainFile:

    #*Crea un lector del archivo csv para poder iterar entre filas
    csvReader = csv.reader(trainFile)

    for row in csvReader:
        trainingSet.append(row)


#*Se crea el objeto perceptron
myPerceptron = Perceptron()
#* Se inicializan las variables iniciales
myPerceptron.setBias(np.random.rand())
myPerceptron.setW0(np.random.rand())
myPerceptron.setW1(np.random.rand())
#* Inicia el perceptron
myPerceptron.trainPerceptron(trainingSet)

#*Una vez terminado, muestra los pesos finales y el bias

print(f"Pesos finales. w0 = {myPerceptron.getW0()} w1 = {myPerceptron.getW1()} y Bias = {myPerceptron.getBias()}")

#* Prueba del perceptron
testSet = []
with open('XOR_tst.csv','r') as trainFile:

    csvReader = csv.reader(trainFile)

    for row in csvReader:
        testSet.append(row)

myPerceptron.testPerceptron(testSet)

print(f"Pesos finales despues del test. w0 = {myPerceptron.getW0()} w1 = {myPerceptron.getW1()} y Bias = {myPerceptron.getBias()}")