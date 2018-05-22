import numpy as num
import time
import os
def tanh(x, deriv = False): #activation function and derivative
    if(deriv==True):
        return (4*num.exp(-2*x))/((1+num.exp(-2*x))**2)
    return (2/(1+num.exp(-2*x)))-1
def numto28bit(x): #converts target value to (28, 1) matrix
    out = []
    for i in range(x):
        out.append(1)
    for i in range(28-x):
        out.append(0)
    return out
num.random.seed(1)
test = open("mnist/mnist_test.csv", "r")
train = open("mnist/mnist_train.csv", "r")
trainread = []
trainin = []
data = input("How many data points would you like to calculate? ") #asks user for number of data points
iterations = input("How many iterations would you like to run? ") #asks user for iterations of selected data
start_time = time.time() #initializes timer
for i in range(int(data)): #reads # of data points specified by user and enters them into list
    out = train.readline().strip("\n").split(",")
    out = [int(i) for i in out]
    trainread.append(out)
test.close()
train.close()
for line in trainread:
    target = line[0]
    values = line[1:]
    matrix = []
    for i in range(28):
        matrix.append(values[0:28])
        values = values[28:]
    trainin.append([target, matrix])
syn0 = 2*num.random.random((28,28))-1 #initializes random weights with mean of 0
syn1 = 2*num.random.random((28,28))-1
syn2 = 2*num.random.random((28,1))-1
#data loading ends, training begins
for i in range(int(iterations)):
    for item in trainin:
        l0 = num.array(item[1])
        l1 = tanh(num.dot(l0,syn0))
        l2 = tanh(num.dot(l1, syn1))
        l3 = tanh(num.dot(l2, syn2))
        Y = num.array(numto28bit(item[0]))
        #training error check
        l3_error = Y - l3
        l3_delta = l3_error * tanh(l3, deriv=True) #adjusts change in weights by derivative of activation function so as to reduce the change (delta) in layer weights
        l2_error = l3_delta.dot(syn2)
        l2_delta = l2_error * tanh(l2, deriv=True)
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error * tanh(l1,deriv=True)
        syn2 += l2.dot(l3_delta) #adjusts layer weights accordingly
        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)
    os.system('cls' if os.name == 'nt' else 'clear') #clears terminal
    print(Y)
    print(l3_error)
    print("Error: " + str(num.mean(num.abs(l3_error))))
print("--- %s seconds ---" % (time.time() - start_time)) #"stops" timer
