# Sand Pile Modelling: Creating a Traffic Simulation

## COMP90072 - The Art of Scientific Computation

### Grade: 90%

## Introduction

This repository contains all of my work for The Art of Scientific Computation (COMP90072), an elective I took in my Master of Physics. 
This subject consisted of one assignment worth 100% of the final grade: a custom project based on an application of programming with a 12-week deadline.
The only requisites for the project were to use sand-pile modelling to create a prototype solution to some problem based on reality, and that it would be accompanied
with a report of up to 20 pages. The report would explain the design, development, and output of the code. These two components would be due at the same time, so I 
developed both together as the project progressed.

Although this project is not directly connected to data science/analysis, I emphasise its importance as it greatly highlights my ability to use creative
practices to develop complex and intuitive programming soltuions like no other project does. Below, I explain what sand-pile modelling is and how it
encompasses the logic of the simulation. I also explain all the files and how to run the program and the various prototypes I constructed.

## Skills Used

- 💾 **Programming**: Used Python as the programming language, PyCharm as the IDE, and the NumPy, SciPy, and Matplotlib libraries.
- 📐 **Problem-Solving**: Inventing mechanics of the traffic simulation, including density-dependent behaviour of vehicles, lane-switching mechanics, traffic lights, vehicle entry and exiting, and more using sand-pile and matrix fundamentals of programming.
- ⚙️ **Agile Methodology**: Implemented cyclical stages of development, so that each feature was gradually rolled in with extensive testing and optimisation one at a time to make the program more scalable and realisable.
- 🔍 **Debugging/Attention to Detail**: Rigorously had to trace the root causes of bugs and glitches in the program due to the variety and complexity of mechanics, especially as the program became larger and more feature-complete. Also lead to further optimisation of the code.
- ✅ **Scope Management**: Planned ambitious but reasonable milestones that could be achieved in the 12-week deadline, and made sure to stick solely to those plans to give leeway for other studies, unexpected events, bug-fixing, and optimisation.
- 📝 **Written Communication**: Submitted a 20-page report of the ideation and development of sand-pile modelling prototypes culminating in the final simulation, as well as in-depth explanations of mechanics, results, and areas of further development.
- 📣 **Verbal Communication**: Showcase my project in an optional live presentation to an audience of peers, tutors, and the subject coordinator.
- ⏰ **Time Management**: Organised weekly schedules and deadlines for individual milestones with leeway for unexpectable obstacles both related to and outside of the project, and prioritised developing the report alongside the program.
- 🔬 **Research**: Extensively investigated techniques and solutions online to implement simulation mechanics and identify unique errors and issues.

## Explaining Sand-Pile Modelling

As a brief introduction to sand pile modelling, consider the following grid below:

![Stage1](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Stage%201.png)

Currently it is empty, but the reason this computational method has gained its name is because these grids can metaphorically be filled with 
randomly placed grains of sand:

![Stage2](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Stage%202.png)

These grains of sand can also be stacked onto each other, meaning more than one may exist on the same grid tile (like a tower):

![Stage3](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Stage%203.png)

However, just like in real life there are limits to stacking things narrowly on top of each other. In these models, a threshold value 
is eventually reached where the grid tile becomes 'unstable', such as in the grid below with the maroon tile containing four sand grains:

![ToppleBefore](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Topple%20Before.png)

The maroon tile contains too many sand grains, and thus it experiences a 'topple', in which it transfers the sand grains to adjacent tiles 
to return to a stable value once more. In this case, the maroon tile loses all its sand grains, and its left, right, top, and bottom neighbours 
instantaneously inherit one sand grain each. There can be many variants to the behaviour of toppling, and this is but one example.

![ToppleAfter](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Topple%20After.png)

Eventually, enough sand grains can be placed so that each topple can destabilise neighbouring tiles and induce a chain reaction of topples across 
the grid. This behaviour is especially notable in larger grids, and is the main attraction of these systems. They have been proven to be highly 
effective in predicting real-life scenarios, most notably in bushfire modelling.

![largerGrid](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Larger%20Grid.png)

At the time of my Master of Physics, I wanted to challenge myself and aim for an ambitious and unorthordox application to sand-pile modelling. I 
settled on traffic, due to the inherent challenge of giving these 'grains' a velocity and destination they would aim to reach. The idea of 
creating topples as a consequence of congestion in traffic was appealing to me, especially given that the topples would function as a behavioural 
change for the movement of vehicles in traffic: cars on their own would move quickly and continuously, while packed cars would move slower and aim 
to spread out as best as they can.  This also had implications for switching between lanes: cars under low densities would tend to stick to their 
lanes, but cars in congestion will often switch lanes the moment they see neighbouring cars outpacing them. The behaviour of vehicles/grains in 
this model could be emulated based on real-life experience. I settled on restricting myself to a freeway for complex reasons explained in my 
report, however there were a number of characterisitics still that were implemented to customise highway simulation: namely timestep durations, 
highway length and width, time-dependent vehicle flux, entry and exit points, and traffic lights.

## Explaining Files and Folders

Python version 3.11.2
matplotlib version 3.7.1
numpy version 2.2.3
scipy version 1.10.1

