import numpy as np
import matplotlib.pyplot as plt
import random

dim = input("Enter dimension of square matrix: ")
dim = int(dim)

Matrix = np.zeros(dim*dim)

Matrix = Matrix.reshape(dim, dim)  # Constructed a dimxdim matrix of zeros

Trials = input("Enter number of sand piles dropped: ")

Set = np.arange(dim)
Ridge = len(Set)-1

Trials = np.arange(int(Trials))

for j in Trials:
    x = np.random.choice(Set)
    y = np.random.choice(Set)
    Matrix[x][y] += 1  # Adds one sand block to random position
    for row in Set:
        for col in Set:
            if Matrix[row][col] >= 4:  # collapses entry of sand if >=4
                a = False
                b = False
                if row == 0:
                    a = True
                    if col == 0:
                        Matrix[0][0] -= 4
                        Matrix[1][0] += 1
                        Matrix[0][1] += 1
                    elif col == Ridge:
                        Matrix[0][Ridge] -= 4
                        Matrix[1][Ridge] += 1
                        Matrix[0][Ridge - 1] += 1
                    else:
                        Matrix[0][col] -= 4
                        Matrix[0][col+1] += 1
                        Matrix[0][col-1] += 1
                        Matrix[1][col] += 1

                if row == Ridge:
                    b = True
                    if col == 0:
                        Matrix[Ridge][0] -= 4
                        Matrix[Ridge-1][0] += 1
                        Matrix[Ridge][1] += 1
                    elif col == Ridge:
                        Matrix[Ridge][Ridge] -= 4
                        Matrix[Ridge - 1][Ridge] += 1
                        Matrix[Ridge][Ridge - 1] += 1
                    else:
                        Matrix[Ridge][col] -= 4
                        Matrix[Ridge][col+1] += 1
                        Matrix[Ridge][col-1] += 1
                        Matrix[Ridge-1][col] += 1

                if a is False and b is False:  # If entry not on border of matrix
                    Matrix[row][col] -= 4
                    Matrix[row][col + 1] += 1
                    Matrix[row][col - 1] += 1
                    Matrix[row - 1][col] += 1
                    Matrix[row + 1][col] += 1

    plt.imshow(Matrix)  # Visualises Matrix
    plt.colorbar()
    plt.show()

