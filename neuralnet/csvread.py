train = open("mnist/mnist_train.csv", "r")
data = train.readline().strip("\n").split(",")
data = data[1:]
data2 = []
for item in data:
    if len(str(item)) == 3:
        data2.append(str(item))
    elif len(str(item)) == 2:
        data2.append("0"+str(item))
    elif len(str(item)) == 1:
        data2.append("00"+str(item))
for i in range(28):
    print(" ".join(data2[0:28]))
    data2 = data2[28:]