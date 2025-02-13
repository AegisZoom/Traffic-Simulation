# Sand Pile Modelling: Creating a Traffic Simulation

## COMP90072 - The Art of Scientific Computation

### Grade: 90%

## Introduction

This repository contains all of my work for The Art of Scientific Computation (COMP90072), an elective I took in my Master of Physics. This subject consisted of one assignment worth 100% of the final grade: a custom project based on an application of programming.

There were several possible project streams to pick that the project would have to be based on, and the project would last for several months until completion. I picked the sand-pile modelling stream, where the goal was to use sand-pile modelling to create a prototype solution to some problem based on reality. This project would consist of two components: a program(s) that would satisfy the problem, and a report that woudld explain the design, development, and output of the code. These two components would be due at the same time, so I developed both together as the project progressed.

## An Introduction to Sand-Pile Modelling

As a brief introduction to sand pile modelling, consider the following grid below:

![Stage1](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Stage%201.png)

Currently it is empty, but the reason this compuational method has gained its name is because these grid can metaphorically be filled with randomly placed grains of sand:

![Stage2](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Stage%202.png)

These grains of sand can also be stacked onto each other, meaning more than one may exist on a grid tile:

![Stage3](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Stage%203.png)

However, just like in reality there are limits to stacking too many things narrowly on top of each other. In these models, a threshold value is eventually reached where the grid becomes 'unstable', such as in the grid below with the maroon tile containing four sand grains:

![ToppleBefore](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Topple%20Before.png)

The maroon tile contains too many sand grains, and this it experiences a 'topple', in which it transfers the sand grains to adjacent tiles to return to a stable value once more. In this case, the maroon tile loses all its sand grains, and its left, right, top, and bottom neighbours instantaneously inherit one sand grain each.

![ToppleAfter](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Topple%20After.png)

Eventually, enough sand grains can be placed so that each topple can destabilise neighbouring tiles and induce a chain reaction of topples across the grid. This behaviour is especially notable in larger grids, and is the main attraction of these systems. They have been proven to be highly effective in predicting real-life scenarios, most notably in bushfire modelling.

![largerGrid](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Larger%20Grid.png)
