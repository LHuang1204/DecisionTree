from math import log

## incomplete, only calculate categorial attributes, but not numerical attributes
def calEntropy(dataset):
    num = len(dataset)
    labelNum = {}
    for label in dataset:
        currentLabel = label[-1]
        if currentLabel not in labelNum.key():
            labelNum[currentLabel] = 0
        labelNum[currentLabel] += 1
    entropy = 0.0
    for key in labelNum:
        p = labelNum[key] / num
        entropy -= p * log(p, 2)
    return entropy

## split dataset
def splitDataset(dataset, axis, value):
    newData = []
    for choice in dataset:
        if choice[axis] == value:
            reducedChoice = choice[:axis]
            reducedChoice.extend(choice[axis + 1:])
            newData.append(reducedChoice)
    return newData

def createDataset():
    dataset = [['sunny', 85, 85, 'false', 'no'],
               ['sunny', 80, 90, 'true', 'no'],
               ['overcast', 83, 86, 'false', 'yes'],
               ['rainy', 70, 96, 'false', 'yes',],
               ['rainy', 68, 80, 'false', 'yes'],
               ['rainy', 65, 70, 'true', 'no'],
               ['overcast', 64, 65, 'true', 'yes'],
               ['sunny', 72, 95, 'false', 'no'],
               ['sunny', 69, 70, 'false', 'yes'],
               ['rainy', 75, 80, 'false', 'yes'],
               ['sunny', 75, 70, 'true', 'yes'],
               ['overcast', 72, 90, 'true', 'yes'],
               ['overcast', 81, 75, 'false', 'yes'],
               ['rainy', 71, 91, 'true', 'no']]
    label = ['overlook', 'temperature', 'humidity', 'windy', 'play']
    return dataset, label

## choose the label with highest entropy
def highEntropy(dataset):
    numChoice = len(dataset[0]) - 1
    baseEntropy = calEntropy(dataset)
    bestInfoGainRatio = 0.0
    best = -1
    ## incomplete

    return best

def createTree(dataset, label):
    list = [example[-1] for example in dataset]
    if list.count(list[0]) == len(list):
        return list[0]
    best = highEntropy(dataset)
    bestLabel = label[best]
    tree = {best: {}}
    del(label[best])
    value = [example[best] for example in dataset]
    unique = set(value)
    for value in unique:
        subLabels = label[:]
        tree[bestLabel][value] = createTree(splitDataset(dataset, best, value), subLabels)
    return tree

dataset, labels = createDataset()
tree = createTree(dataset, labels)
print(tree)