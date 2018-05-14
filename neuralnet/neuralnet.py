import numpy as num
from mnist import MNIST
def tanh(x, deriv = False):
    if(deriv==True):
        return (4*num.exp(-2*x))/((1+num.exp(-2*x))**2)
    return (2/(1+num.exp(-2*x)))-1
mndata = MNIST("./mnist")
images, labels = mndata.load_training()
