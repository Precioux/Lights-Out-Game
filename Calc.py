import numpy as np


class Calculator:
    def __init__(self, matrix,n):
        self.matrix = np.array(matrix)
        self.n = n
        self.check = np.array(False)
        l = 1
        while l < self.elements:
            self.check = np.append(self.check, False, axis=None)
            l += 1

    def printer(self):
        print(self.matrix)

    def findPivot(self, k):
        i = 0
        flag = False
        while not flag:
            if self.matrix[i][k] != 0:
                flag = True
            else:
                i += 1
        return i

    def changeRow(self, i, e):
        if i != e and self.check[i] == False:
            temp = np.array(self.matrix[e])
            self.matrix[e] = self.matrix[i]
            self.matrix[i] = temp
        self.check[e] = True

    def setOne(self, e):
        a = int(self.matrix[e][e])
        if a != 0:
            tmp = self.matrix[e] / a
            self.matrix[e] = tmp

    def setZero(self, e):

        if e + 1 < self.elements:
            c = e + 1
            while c < self.elements:
                n = int(self.matrix[c][e])
                self.matrix[c] = self.matrix[c] - self.matrix[e] * n
                self.setOne(c)
                c += 1

    def makeEchlon(self):
        e = 0
        while e < self.elements:
            i = self.findPivot(e)
            self.changeRow(i, e)
            self.setOne(e)
            e += 1
        k = 0
        while k < self.elements:
            self.setZero(k)
            k += 1

    def reduceIt(self):
        t = 0
        while t < self.elements:
            for i in range(0, self.compounds - 1):
                n = float(self.matrix[t][i])
                if n != 0 and t != i:
                    self.matrix[t] = self.matrix[t] - n * self.matrix[i]
            t += 1

    def getResults(self):
        ans = self.checkFree()
        s = 0
        while s < self.elements:
            a = float(self.matrix[s][self.compounds - 1])
            if a < 0:
                if a == 0:
                    a = float(1)
                else:
                    a = a * (-1)
            if ans != -1:
                print(f"X{s} = {a} X{ans}")
            else:
                print(f"X{s} = {a}")
            s += 1
        if ans != -1:
            print(f"X{ans} is free")

    def checkFree(self):
        ans = -1
        for i in range(0, self.compounds):
            sum = 0
            for j in range(self.elements):
                if self.matrix[j][i] != 0 and self.matrix[j][i] != 1:
                    sum += 1
            if sum == self.elements:
                ans = sum
        return ans

    def ready(self):
        self.printer()
        self.makeEchlon()
        print("Echlon Matrix:")
        self.printer()
        self.reduceIt()
        print("Reduced Echlon Matrix:")
        self.printer()
        print("Results:")
        self.getResults()