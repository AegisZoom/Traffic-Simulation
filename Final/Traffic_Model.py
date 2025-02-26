import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap, ListedColormap  # Imports colours
import matplotlib.animation as animation
import math
import random
import pickle
# The pickled file named Stuff is created from Simulation_Example, run that script first!
Load_Characteristics = str(input("Insert name of file containing pickled characteristics (default = Stuff): "))
file = open(Load_Characteristics, 'rb')
data = pickle.load(file)
file.close()
entrances_l = data[0]  # This and the following variables were pickled by Simulation_Example into a file named Stuff
entrances_r = data[1]
exits_l = data[2]
exits_r = data[3]
Traffic_row = data[4]
Probs_Highway_l = data[5]
Probs_Highway_r = data[6]
Probs_Entrance_l = data[7]
Probs_Entrance_r = data[8]
Clock_Time = data[9]
highway_length = data[10]  # Used to be manual input, relegated to input from external script

Grad_Probs = [[0, 0, 0, 10, 8, 8, 3, 0, 0],  # Entry = 1         This table is used for when cars can switch lanes
              [0, 0, 10, 8, 6, 1, 0, 0, 0],  # Entry = 2
              [0, 10, 9, 8, 2, 0, 0, 0, 0],  # Entry = 3
              [10, 10, 9, 1, 0, 0, 0, 0, 0]]  # Entry = 4
#             -4, -3, -2,-1,+0,+1,+2,+3,+4

lanes = int(input("Enter number of lanes (standard = 4): "))

Traffic_count_1 = []
Traffic_count_2 = []
for ok in np.arange(len(Traffic_row)):
    Traffic_count_1.append(random.choice(np.arange(21)))  # randomises when traffic lights initially activate
    Traffic_count_2.append(0)

Matrix = np.zeros(highway_length * (2 * lanes + 1))
Matrix = Matrix.reshape(highway_length, 2 * lanes + 1)  # Constructed a 100x(2*lanes + 1) matrix of zeros
for row in np.arange(highway_length):  # Middle column is where road barriers are
    Matrix[row][lanes] = 5

Timestep = int(input("Enter timesteps per time (standard = 10): "))
Trials = len(Probs_Highway_l) * Timestep
Trials = np.arange(int(Trials))

cmap = ListedColormap(["black", "beige", "yellow", "orange", "red", "blue"])
frames = []
fig = plt.figure()

Turn_count = 0  # Prevents cars from moving multiple times per time step
Turn_count_Next = 0
Turn_count_Left = 0

S_Lanes = np.arange(lanes)
S_Lanes2 = np.arange(lanes) + lanes + 1
S_Lanes2 = np.flip(S_Lanes2)  # Reverses horizontal iteration direction on other side of highway, reasoning...
S_Lanes = np.append(S_Lanes, S_Lanes2)  # ... explained in report in detail

for j in Trials:
    Time = math.floor(j / Timestep)

    for ok2 in np.arange(len(Traffic_row)):  # Portion of code that handles (de)activation of traffic lights
        if Traffic_count_1[ok2] < 20:
            Traffic_count_1[ok2] += 1
        else:
            Traffic_count_2[ok2] += 1
            if Traffic_count_2[ok2] == 10:
                Traffic_count_1[ok2] = 0
                Traffic_count_2[ok2] = 0
                for go in S_Lanes:
                    Matrix[Traffic_row[ok2]][go] = 0
            else:
                for stop in S_Lanes:
                    Matrix[Traffic_row[ok2]][stop] = 5
                    Matrix[Traffic_row[ok2] - 1][lanes - 1] += np.random.choice(Probs_Entrance_l[Time])
                    Matrix[Traffic_row[ok2] + 1][lanes + 1] += np.random.choice(Probs_Entrance_r[Time])
                    if Matrix[Traffic_row[ok2] - 1][lanes - 1] > 4:
                        Matrix[Traffic_row[ok2] - 1][lanes - 1] = 4
                    if Matrix[Traffic_row[ok2] + 1][lanes + 1] > 4:
                        Matrix[Traffic_row[ok2] + 1][lanes + 1] = 4

    for roww in np.arange(highway_length):  # Iterating ove rows of matrix
        if len(np.argwhere(exits_l == roww)) > 0:  # cars exiting left side of highway
            Leave = np.array(random.choices([0, 1], weights=[2, 1], k=int(Matrix[roww][0])))  # 30% chance of car exit
            Matrix[roww][0] -= len(np.argwhere(Leave == 1))
        if len(np.argwhere(exits_r == highway_length - roww - 1)) > 0:  # cars exiting right side of highway
            Leave = np.array(random.choices([0, 1], weights=[2, 1], k=int(Matrix[roww][2 * lanes])))  # 30% chance exit
            Matrix[roww][2 * lanes] -= len(np.argwhere(Leave == 1))
        if len(np.argwhere(Traffic_row == roww + 1)) > 0:  # cars exiting from traffic lights
            Leave = np.array(random.choices([0, 1], weights=[2, 1], k=int(Matrix[roww][0])))  # 30% chance of car exit
            Matrix[roww][0] -= len(np.argwhere(Leave == 1))
            Leave = np.array(random.choices([0, 1], weights=[2, 1], k=int(Matrix[roww][lanes - 1])))  # 30% chance
            Matrix[roww][lanes - 1] -= len(np.argwhere(Leave == 1))
            Leave = np.array(random.choices([0, 1], weights=[2, 1], k=int(Matrix[roww][2 * lanes])))  # 30% chance exit
            Matrix[roww][2 * lanes] -= len(np.argwhere(Leave == 1))
            Leave = np.array(random.choices([0, 1], weights=[2, 1], k=int(Matrix[roww][lanes + 1])))  # 30% chance exit
            Matrix[roww][lanes + 1] -= len(np.argwhere(Leave == 1))

        for col in S_Lanes:  # Iterating over columns of matrix
            if col < lanes:
                Phase = 1
                row = roww
            elif col > lanes:
                Phase = -1  # Reverses direction where cars move on other side of highway
                row = highway_length - roww - 1  # Reverses vertical iteration direction of other side of matrix
            entry = int(Matrix[row][col])

            if col == 0 or col == 2 * lanes:
                Turn_left = 4  # High number to set turning probability to zero
            else:  # use if statement where indexing can be negative to avoid teleporting cars across matrix
                Turn_left = int(Matrix[row][col - Phase]) - entry  # Gradient between entry and entry left of it

            Turn_right = int(Matrix[row][col + Phase]) - entry  # Gradient between entry and entry right of it

            if roww == 0:
                Straight_1 = -entry
            else:
                Straight_1 = int(Matrix[row - Phase][col]) - entry  # Gradient of entry and entry above it

            if roww == 0 or roww == 1:
                Straight_2 = -entry
            else:
                Straight_2 = int(Matrix[row - Phase * 2][col]) - entry  # Gradient of entry two entries above it

            if 0 < entry < 5:  # Cars switching lanes
                T_l_weight = Grad_Probs[entry - 1][Turn_left + 4]
                T_r_weight = Grad_Probs[entry - 1][Turn_right + 4]
                S_weight = 4 * Grad_Probs[entry - 1][Straight_1 + 4]

                try:
                    Turn = np.array(random.choices([-1, 0, 1], weights=[T_l_weight, S_weight, T_r_weight],
                                                   k=entry - Turn_count))
                except ValueError:  # for when sum of weights is zero when cars can't switch lanes at all
                    Turn = [0]
                for lol in np.arange(len(np.argwhere(Turn == 1))):
                    if Matrix[row][col + Phase] < 4 and Matrix[row][col] > 0:
                        Matrix[row][col] -= 1
                        Matrix[row][col + Phase] += 1
                        Turn_count_Next += 1
                for lol in np.arange(len(np.argwhere(Turn == -1))):
                    if Matrix[row][col - Phase] < 4 and Matrix[row][col] > 0:
                        Matrix[row][col] -= 1
                        Matrix[row][col - Phase] += 1
                        Turn_count_Left += 1
                ################################  Updating values of entry and Straight Gradients  ##################
                entry = Matrix[row][col]
                if roww == 0:
                    Straight_1 = -entry
                else:
                    Straight_1 = int(Matrix[row - Phase][col]) - entry  # Gradient of entry and entry above it

                if roww == 0 or roww == 1:
                    Straight_2 = -entry
                else:
                    Straight_2 = int(Matrix[row - Phase * 2][col]) - entry  # Gradient of entry two entries above it
                ####################  Updating cars that switched to lane already iterated upon  ######################
                if Turn_count_Left > 0:
                    entry_left = Matrix[row][col - Phase]
                    if roww == 0:
                        Straight_1_Left = -entry_left
                    else:
                        Straight_1_Left = int(Matrix[row - Phase][col - Phase]) - entry_left
                    if roww == 0 or roww == 1:
                        Straight_2_Left = -entry_left
                    else:
                        Straight_2_Left = int(Matrix[row - Phase * 2][col - Phase]) - entry_left
                    if entry_left == 1:  # Left entry was initially empty
                        if Straight_2_Left < 3 and Straight_1_Left == -1:
                            Matrix[row][col - Phase] -= 1
                            if roww > 1:
                                Matrix[row - Phase * 2][col - Phase] += 1
                        elif 3 > Straight_1_Left:
                            Matrix[row][col - Phase] -= 1
                            if roww > 0:
                                Matrix[row - Phase][col - Phase] += 1

                    elif entry_left == 2:
                        if 0 >= Straight_2_Left > -2 == Straight_1_Left:
                            Matrix[row][col - Phase] -= Turn_count_Left
                            if roww > 1:
                                Matrix[row - Phase * 2][col - Phase] += Turn_count_Left
                        elif Straight_2_Left == 1 and Straight_1_Left == -2:
                            if Turn_count_Left == 1:
                                Matrix[row][col - Phase] -= 1
                                if roww > 1:
                                    Matrix[row - Phase * 2][col - Phase] += 1
                            elif Turn_count_Left == 2:
                                Matrix[row][col - Phase] -= 2
                                if roww == 1:
                                    Matrix[row - Phase][col - Phase] += 1
                                elif roww > 1:
                                    Matrix[row - Phase][col - Phase] += 1
                                    Matrix[row - Phase * 2][col - Phase] += 1
                        elif 0 >= Straight_1_Left >= -2:
                            Matrix[row][col - Phase] -= Turn_count_Left
                            if roww > 0:
                                Matrix[row - Phase][col - Phase] += Turn_count_Left
                        elif Straight_1_Left == 1:
                            Matrix[row][col - Phase] -= 1
                            if roww > 0:
                                Matrix[row - Phase][col - Phase] += 1

                    elif entry_left == 3:  # only one car will have a 50% chance of moving ahead if clear
                        if Straight_1_Left < 1:
                            Move = random.choices([0, 1])[0]  # 50% chance of moving ahead
                            Matrix[row][col - Phase] -= Move
                            if roww > 0:
                                Matrix[row - Phase][col - Phase] += Move
                    # cars won't move at all if left entry becomes 4
            ######################  Evolving cars in current entry in straight direction  #######################
            if len(np.argwhere(Traffic_row == row - Phase)) > 0:  # Checks if row is directly behind traffic light
                Index = np.argwhere(Traffic_row == row - Phase)[0][0]
                Check = Traffic_count_1[Index]
            else:
                Check = 100
            if Check == 100 or Check < 17:  # 16<Check<20 equivalent to yellow light effect of traffic lights
                if entry == 1:
                    if Straight_2 < 3 and Straight_1 == -1:
                        Matrix[row][col] -= 1
                        if roww > 1:
                            Matrix[row - Phase * 2][col] += 1
                    elif 3 > Straight_1:
                        Matrix[row][col] -= 1
                        if roww > 0:
                            Matrix[row - Phase][col] += 1

                elif entry == 2:
                    if 0 >= Straight_2 > -2 == Straight_1:
                        Matrix[row][col] -= 2
                        if roww > 1:
                            Matrix[row - Phase * 2][col] += 2
                    elif Straight_2 == 1 and Straight_1 == -2:
                        Matrix[row][col] -= 2
                        if roww == 1:
                            Matrix[row - Phase][col] += 1
                        elif roww > 1:
                            Matrix[row - Phase][col] += 1
                            Matrix[row - Phase * 2][col] += 1
                    elif 0 >= Straight_1 >= -2:
                        Matrix[row][col] -= 2
                        if roww > 0:
                            Matrix[row - Phase][col] += 2
                    elif Straight_1 == 1:
                        Matrix[row][col] -= 1
                        if roww > 0:
                            Matrix[row - Phase][col] += 1

                elif entry == 3:
                    if Turn_count == 3:
                        pass
                    elif Straight_2 == 0 and Straight_1 == -3:
                        Matrix[row][col] -= 3 - Turn_count
                        if roww == 1:
                            if Turn_count == 2:
                                Matrix[row - Phase][col] += 1
                            else:
                                Matrix[row - Phase][col] += 2
                        elif roww > 1:
                            if Turn_count == 2:
                                Matrix[row - Phase][col] += 1  # Matrix[row - 2][col] += 0 is redundant
                            else:
                                Matrix[row - Phase][col] += 2
                                Matrix[row - Phase * 2][col] += 1 - Turn_count
                    elif Straight_2 == -1 and Straight_1 == -3:
                        Matrix[row][col] -= 3 - Turn_count
                        if roww == 1:
                            Matrix[row - Phase][col] += 1
                        elif roww > 1:
                            Matrix[row - Phase][col] += 1
                            Matrix[row - Phase * 2][col] += 2 - Turn_count
                    elif -2 > Straight_2 > -3 == Straight_1:
                        Matrix[row][col] -= 3 - Turn_count
                        Disperse_3 = random.choices([0, 1])[0]  # 50% chance of Dispersion occurring
                        if roww == 1:
                            Matrix[row - 1 * Phase][col] += 3 - Turn_count - Disperse_3
                        elif roww > 1:
                            Matrix[row - Phase][col] += 3 - Turn_count - Disperse_3
                            Matrix[row - Phase * 2][col] += Disperse_3
                            # If dispersion occurs, one car enters second upper entry
                    elif Straight_1 == 0:
                        Matrix[row][col] -= 1
                        if roww > 0:
                            Matrix[row - Phase][col] += 1
                    elif Straight_1 == -1:
                        Matrix[row][col] -= 2 - Turn_count
                        if roww > 0:
                            Matrix[row - Phase][col] += 2 - Turn_count
                    elif Straight_1 == -2 or Straight_1 == -3:
                        Matrix[row][col] -= 3 - Turn_count
                        if roww > 0:
                            Matrix[row - Phase][col] += 3 - Turn_count

                elif entry == 4:
                    if Turn_count == 4:
                        pass  # Add probs
                    elif Straight_2 < 0 and Straight_1 == -4:
                        Disperse_4 = random.choices([0, 1, 2], weights=[1, 4, 5])[0]  # 50% chance of Dispersion occur
                        if Disperse_4 == 1:  # Cars move altogether one entry ahead, except ones that turned in
                            Matrix[row][col] = 0 + Turn_count
                            if roww > 0:
                                Matrix[row - Phase][col] = 4 - Turn_count
                        elif Disperse_4 == 2:  # Cars disperse
                            Matrix[row][col] -= 3 - Turn_count
                            if Turn_count < 3:
                                if roww == 1:
                                    Matrix[row - Phase][col] += 2 - Turn_count  # One car went ahead and exited
                                elif roww > 1:
                                    if Turn_count == 2:
                                        Matrix[row - Phase * 2][col] += 1  # Matrix[row - 1][col] += 0 is redundant
                                    elif Turn_count == 1:
                                        Matrix[row - Phase][col] += 1
                                        Matrix[row - Phase * 2][col] += 1
                                    elif Turn_count == 0:
                                        Matrix[row - Phase][col] += 2
                                        Matrix[row - Phase * 2][col] += 1
                    elif Straight_1 == -4:
                        Matrix[row][col] -= 4 - Turn_count
                        if roww > 0:
                            Matrix[row - Phase][col] += 4 - Turn_count
                    elif 0 > Straight_1 > -4:
                        Matrix[row][col] -= 1
                        if roww > 0:
                            Matrix[row - Phase][col] += 1

            Turn_count = Turn_count_Next  # Updates/resets Turn_Count values
            Turn_count_Next = 0
            Turn_count_Left = 0

        if len(np.argwhere(entrances_l == roww)) > 0:  # Cars entering highway from left side
            Matrix[roww][0] += np.random.choice(Probs_Entrance_l[Time])
            if Matrix[roww][0] > 4:
                Matrix[roww][0] = 4
        if len(np.argwhere(entrances_l == highway_length - roww - 1)) > 0:  # Cars entering highway from right side
            Matrix[roww][2 * lanes] += np.random.choice(Probs_Entrance_r[Time])
            if Matrix[roww][2 * lanes] > 4:
                Matrix[roww][2 * lanes] = 4
    for Lane in np.arange(lanes):  # Cars directly entering left side of highway
        Matrix[highway_length - 1][Lane] = Matrix[highway_length - 1][Lane] + np.random.choice(
            Probs_Highway_l[Time])
        if Matrix[highway_length - 1][Lane] > 4:
            Matrix[highway_length - 1][Lane] = 4
    for Lane in S_Lanes2:  # Cars directly entering right side of highway
        Matrix[0][Lane] += np.random.choice(Probs_Highway_r[Time])
        if Matrix[0][Lane] > 4:
            Matrix[0][Lane] = 4
    frames.append([plt.imshow(Matrix, vmin=0, vmax=5, cmap=cmap, animated=True)])  # Appends frames of animation
plt.colorbar()
plt.clim(0, 5)
plt.xlabel("Lanes  (x 3m)")
plt.ylabel("Along Highway (x 15m)")
plt.title("Simulation of Highway Traffic Flow")
ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat=False)  # Plays animation
plt.show()
ani.save(filename="Traffic_Animation.mp4")  # Saves animation as mp4 file
