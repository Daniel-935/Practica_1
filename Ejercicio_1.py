import csv

trainingSet = []
with open('XOR_trn.csv','r') as trainFile:

    #*Crea un lector del archivo csv para poder iterar entre filas
    csvReader = csv.reader(trainFile)

    for row in csvReader:
        trainingSet.append(row)

print(trainingSet)