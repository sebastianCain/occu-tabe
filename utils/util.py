import random

def getTableMatrix():
    occu = open("data/occupations.csv", "r")
    streamy = occu.read()

    matrix = [[]]
    
    data = streamy.strip().split("\n")

    for line in range(len(data)):
        
        lineData = data[line].replace('"', '').split(",")
        newData = []
        
        if len(lineData) > 2:
            newData = [",".join(lineData[:len(lineData)-1]), lineData[len(lineData)-1]]
        else:
            newData = lineData
        matrix.append(newData)
    return matrix

def getRandom():
    
    matrix = getTableMatrix()
    percentages = []
    
    for i in range(2, len(matrix)):        
        percentage = float(matrix[i][1])
        percentages.append(percentage)

    r = random.uniform(0, 99.8)
    inc = 0
    for i in range(len(percentages)):
        inc += percentages[i]
        if inc > r:
            return matrix[i+2][0]
    
