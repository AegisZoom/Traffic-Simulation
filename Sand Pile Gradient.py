import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap, ListedColormap #Imports colours
import matplotlib.animation as animation
import math
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

    grad_array = [] #Array that stores information on gradient field of matrix

    for row in Set:
        for col in Set:
            if col == 0:
                grad_entry_1 = 0
            else:#use if statement where indexing can be nagative to avoid teleporting sand topple across matrix
                grad_entry_1 = Matrix[row][col-1] - Matrix[row][col] #Gradient between entry and entry left of it
            try:
                grad_entry_2 = Matrix[row][col+1] - Matrix[row][col] # Gradient between entry and entry right of it
            except IndexError:
                grad_entry_2 = 0
            try:
                grad_entry_3 = Matrix[row+1][col] - Matrix[row][col] #Gradient of entry and entry above it
            except IndexError:
                grad_entry_3 = 0
            if row == 0:
                grad_entry_4 = 0
            else:
                grad_entry_4 = Matrix[row-1][col] - Matrix[row][col] #Gradient of entry and entry below it

            grad_entry = [grad_entry_1, grad_entry_2, grad_entry_3, grad_entry_4]#Vector of directional gradients
            grad_array = np.append(grad_array, grad_entry)#Stores into grand gradient field array
    grad_array = grad_array.reshape(dim, dim*4)#Every four entries in row correspond to one entry in Matrix

    Topple_sites = np.argwhere(grad_array < -3)#New condition for toppling: Gradient <-3 in direction
    for Topple in Topple_sites:
        row1 = Topple[0]
        col1 = math.floor(Topple[1]/4)
        Matrix[row1][col1] -= 1
        Rem = Topple[1]%4 #Gets remainder
        if Rem == 0:
            Matrix[row1][col1-1] += 1
        elif Rem == 1:
            Matrix[row1][col1+1] += 1
        elif Rem == 2:
            Matrix[row1+1][col1] += 1
        elif Rem == 3:
            Matrix[row1-1][col1] += 1#Program conflates Rem2 with Rem2 but produces no errors on Matrix???
        #print("Topple at ["+str(row1)+","+str(col1)+"], Rem = "+str(Rem))

    frames.append([plt.imshow(Matrix, vmin=0, vmax=4, cmap=cmap, animated=True)])

plt.colorbar()
plt.clim(0, 5)
ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat=False) # repeat_delay = 1000
plt.show()