import pygame
import numpy

### Globals ###

pygame.init()

adj = [[0, 0], [0, -1], [-1, 0], [0, 1], [1, 0]]

TILE_HEIGHT = 50
TILE_WIDTH = 50
MARGIN = 2


class Game:
    def __init__(self, cells):
        self.cells = cells
        self.clear()
        self.load_level()

    def clear(self):
        self.grid = [[0 for i in range(len(self.cells))] for j in range(len(self.cells))]

    def load_level(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.grid[x][y] = int(self.cells[y][x])

    def draw(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells)):
                i = x * TILE_WIDTH + MARGIN
                j = y * TILE_HEIGHT + MARGIN
                h = TILE_HEIGHT - (2 * MARGIN)
                w = TILE_WIDTH - (2 * MARGIN)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, (105, 210, 231), [i, j, w, h])
                else:
                    pygame.draw.rect(screen, (255, 255, 255), [i, j, w, h])

    def get_adjacent(self, x, y):
        adjs = []
        for i, j in adj:
            if (0 <= i + x < len(self.cells)) and (0 <= j + y < len(self.cells)):
                adjs += [[i + x, j + y]]
        return adjs

    def click(self, pos):
        x = int(pos[0] / TILE_WIDTH)
        y = int(pos[1] / TILE_HEIGHT)
        adjs = self.get_adjacent(x, y)
        for i, j in adjs:
            self.grid[j][i] = (self.grid[j][i] + 1) % 2


def setZero(matrix, n, e):
    if e + 1 < n:
        c = e + 1
        while c < n:
            print(f'c = {c}')
            print(f'pivot row is {matrix[e]}')
            print(f'summing      {matrix[c]}')
            m = matrix[c][e]
            print(f'm is {m}')
            if m == 1 :
                i = 0
                while i + e <= n:
                    if matrix[c][e + i]==1 and matrix[e][i+e]== 1:
                        matrix[c][e+i]=0
                    else:
                        matrix[c][i+e]=matrix[c][i+e]+matrix[e][e+i]
                    i = i+1
            print(f'after summing {matrix[c]}')
            c += 1
        print('A is now :')
        print(matrix)


def changeRow(matrix, check, i, e):
    if i != e and check[i] == False:
        temp = numpy.array(matrix[e])
        matrix[e] = matrix[i]
        matrix[i] = temp
        print("Row changed")
    check[e] = True


def findPivot(matrix, check, col):
    i = 0
    flag = False
    while not flag:
        if matrix[i][col] != 0 and check[i] == False:
            flag = True
        else:
            i += 1
    return i


def one(matrix, e):
    a = int(matrix[e][e])
    if a != 0:
        tmp = matrix[e] / a
        matrix[e] = tmp

def ReduceIt(matrix,n):
    print('lets reduce it')
    print(n)
    t = 0
    while t < n*n:
        for i in range( n*n ):
            print('before')
            print(matrix[t])
            print(matrix[i])
            m = matrix[t][i]
            if m!= 0 and t != i:
                j=0
                while j+i<=n*n:
                    if matrix[t][i+j]==1 and matrix[i][i+j]==1:
                        matrix[t][i+j]=0
                    else:
                        matrix[t][i+j]=matrix[t][i+j]+matrix[i][i+j]
                    j =j+1
                print('after:')
                print(matrix[t])
        print('changed ')
        print(matrix)
        t += 1


    print('after reduction:')
    print(matrix)


def EchlonIt(A, n):
    check = numpy.full((n * n), False)
    e = 0
    while e < n * n:
        print(f'e is {e}')
        print(check)
        i = findPivot(A, check, e)
        print(f'pivot is row {i}')
        changeRow(A, check, i, e)
        one(A, e)
        setZero(A, n * n, e)
        e = e + 1
    # print(f'A after first While')
    # print(A)
    # k = 0
    # while k < n*n:
    #     setZero(A,n*n,k)
    #     k += 1
    print('Final :')
    print(A)


def determinantOfMatrix(mat, n):
    temp = [0] * n  # temporary array for storing row
    total = 1
    det = 1  # initialize result

    # loop for traversing the diagonal elements
    for i in range(0, n):
        index = i  # initialize the index

        # finding the index which has non zero value
        while (index < n and mat[index][i] == 0):
            index += 1

        if (index == n):  # if there is non zero element
            # the determinant of matrix as zero
            continue

        if (index != i):
            # loop for swapping the diagonal element row and index row
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]

            # determinant sign changes when we shift rows
            # go through determinant properties
            det = det * int(pow(-1, index - i))

        # storing the values of diagonal row elements
        for j in range(0, n):
            temp[j] = mat[i][j]

        # traversing every row below the diagonal element
        for j in range(i + 1, n):
            num1 = temp[i]  # value of diagonal element
            num2 = mat[j][i]  # value of next row element

            # traversing every column of row
            # and multiplying to every row
            for k in range(0, n):
                # multiplying to make the diagonal
                # element and next row element equal

                mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])

            total = total * num1  # Det(kA)=kDet(A);

    # multiplying the diagonal elements to get determinant
    for i in range(0, n):
        det = det * mat[i][i]

    return int(det / total)  # Det(kA)/k=Det(A);


def checkA(A, n):
    mat = numpy.copy(A)
    print(determinantOfMatrix(mat, n))


def setOne(A, n, col, i, j):
    row = i * n + j
    A[row][col] = 1


def letsCheat(cells):
    G = cells.copy()
    # let's make A
    n = len(G)
    A = numpy.zeros([n * n, n * n], dtype=int)
    col = 0
    for i in range(n):
        for j in range(n):
            # print(f'For i = {i}  and j = {j}')
            setOne(A, n, col, i, j)
            if i - 1 >= 0:
                # print("yes i-1")
                setOne(A, n, col, i - 1, j)
            if i + 1 < n:
                # print("yes i+1")
                setOne(A, n, col, i + 1, j)
            if j - 1 >= 0:
                # print("yes j-1")
                setOne(A, n, col, i, j - 1)
            if j + 1 < n:
                # print("yes j+1")
                setOne(A, n, col, i, j + 1)
            col = col + 1
    # let's make B
    B = numpy.zeros([n * n, 1], dtype=int)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                B[i * n + j][0] = 1

    print(A)
    print('///////////////////////////////////////////////////////////')
    print(B)
    print('///////////////////////////////////////////////////////////')
    # else :
    checkA(A, n)
    A = numpy.append(A, B, axis=1)
    print("A : B =>")
    print(A)
    EchlonIt(A, n)
    ReduceIt(A,n)



### Main ###
if __name__ == "__main__":
    cells = numpy.array([[1, 0, 1],
                         [0, 1, 0],
                         [1, 0, 1]])
    print(cells)

    # screen = pygame.display.set_mode((len(cells) * TILE_WIDTH, len(cells) * TILE_HEIGHT))
    # screen.fill((167, 219, 216))
    # pygame.display.set_caption("Game")
    #
    # game = Game(cells.T)
    # game.draw()

    clock = pygame.time.Clock()
    keepGoing = True
    letsCheat(cells)
    # while keepGoing:
    #     clock.tick(30)
    #     game.draw()
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             keepGoing = False
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             pos = pygame.mouse.get_pos()
    #             game.click(pos)
    #     pygame.display.flip()
    # pygame.quit()
