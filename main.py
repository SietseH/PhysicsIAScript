# Data

RaceBikeTire = [[100],[[248, -11],[253, -9], [258, -8], [263, -7],
[267, -4], [274, -2], [279, -1], [284, 0], [288, 2], [294, 3]]]

NormalBikeTire = [[50], [[249, -9], [253, -8], [257, -6], [263, -5],
[268, -3], [275, -2], [278, 0], [278, 0], [283, 0], [288, 1], [294, 2]]]

ThicBikeTire = [[65],[[247, -9], [253, -8], [258, -7], [263, -6],
[268, -4], [275, -1], [279, 0], [284, 0], [288, 0], [294, 2]]]

PsiToPascal = 6894.76

def psiPascal(name):
    output = name * PsiToPascal
    return output

def initialPoint(data):
    psi = data[0][0]
    for point in data[1]:
        if point[1] == 0:
           return point, psi, data


def theoPressure(point):
    dataset = []
    data = point[2]
    p1 = psiPascal(data[0][0])
    T1 = point[0][0]
    del data[0]
    #print(data)
    for set in data[0]:

        T2 = set[0]
        #print(T2, T1, p1)
        p2 = (p1 * T2)/T1
        dataset.append([T2, p2])
    return dataset
    


print(theoPressure(initialPoint(RaceBikeTire)))
print(theoPressure(initialPoint(NormalBikeTire)))
print(theoPressure(initialPoint(ThicBikeTire)))