import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap, ListedColormap #Imports colours
import matplotlib.animation as animation
import random

dim = input("Enter dimension of square matrix: ")
dim = int(dim)

Matrix = np.zeros(dim*dim)

Matrix = Matrix.reshape(dim, dim)  # Constructed a dimxdim matrix of zeros

Trials = input("Enter number of sand piles dropped: ")

Set = np.arange(dim)

cmap = ListedColormap(["black", "beige", "yellow", "orange", "red"])

Trials = np.arange(int(Trials))
frames = []
fig = plt.figure()

for j in Trials:
    x = np.random.choice(Set)
    y = np.random.choice(Set)
    Matrix[x][y] += 1  # Adds one sand block to random position

    Topple_sites = np.argwhere(Matrix > 3)
    for Topple in Topple_sites:
        row = Topple[0]
        col = Topple[1]
        Matrix[row][col] -= 4
        try:
            Matrix[row + 1][col] += 1
        except IndexError:
            pass
        try:
            Matrix[row - 1][col] += 1
        except IndexError:
            pass
        try:
            Matrix[row][col + 1] += 1
        except IndexError:
            pass
        try:
            Matrix[row][col - 1] += 1
        except IndexError:
            pass

    frames.append([plt.imshow(Matrix, vmin = 0, vmax = 4, cmap=cmap, animated=True)])
plt.colorbar()
plt.clim(0, 5)
ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat=False) #repeat_delay = 1000
# ani.save('movie.mp4')
plt.show()