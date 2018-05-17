import numpy as num
def tanh(x, deriv = False):
    if(deriv==True):
        return (4*num.exp(-2*x))/((1+num.exp(-2*x))**2)
    return (2/(1+num.exp(-2*x)))-1
def numto28bit(x):
    out = []
    for i in range(x):
        out.append(1)
    for i in range(28-x):
        out.append(0)
    return out
test = open("mnist/mnist_test.csv", "r")
train = open("mnist/mnist_train.csv", "r")
trainread = []
trainin = []
data = input("How many data points would you like to calculate?")
iterations = input("How many iterations would you like to run?")
for i in range(int(data)):
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
syn0 = 2*num.random.random((28,28))-1
syn1 = 2*num.random.random((28,1))-1
syn2 = 2*num.random.random((1,28))-1
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
        #correcting error mathematically to change weights by less
        l3_delta = l3_error*tanh(l3, deriv=True)
        l2_error = l3_delta.dot(syn2.T)
        l2_delta = l2_error*tanh(l2, deriv=True)
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error * tanh(l1,deriv=True)
        syn2 += l2.T.dot(l3_delta)
        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)
print("Error: " + str(num.mean(num.abs(l3_error))))

