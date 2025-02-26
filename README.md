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
is eventually reached where the grid tile becomes 'unstable', such as in the left grid below with the maroon tile containing four sand grains:

![Topple](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Topple.png)

The maroon tile contains too many sand grains, and thus it experiences a 'topple', in which it transfers the sand grains to adjacent tiles 
to return to a stable value once more. In this case, the maroon tile loses all its sand grains, and its left, right, top, and bottom neighbours 
instantaneously inherit one sand grain each. There can be many variants to the behaviour of toppling, and this is but one example.

Eventually, enough sand grains can be placed so that each topple can destabilise neighbouring tiles and induce a chain reaction of topples across 
the grid. This behaviour is especially notable in larger grids, and is the main attraction of these systems. They have been proven to be highly 
effective in predicting real-life scenarios, most notably in bushfire modelling.

![largerGrid](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Larger%20Grid.png)

With the mechanics of sand-pile modelling explained, I can explain the premise of the traffic simulation. These topple behaviours can also be applied
to traffic. Drivers prefer to keep safe distances between each other, but sometimes this isn't possible. Traffic congestion is a big problem Melbourne
faces, so frequently vehicles are tightly packed and make slow progress on the road. If there is an opportunity to create more space and thus more speed,
any driver will take it, and this defines a topple for the simulation. This is a simple approximation of driving behaviour, but an effecive one as demonsrated
by the example of the simulation below.

![Animation](https://github.com/AegisZoom/Traffic-Simulation/blob/Add-Files/Sand%20Pile%20Examples/Traffic_Animation.gif)

The biggest challenge for developing this simulation is that unlike static sand-pile models, vehicles have a destination and a velocity. They change their movement and
behaviour when they get clustered, which can happen from traffic lights (flashing blue horizontal streaks), entry and exit points, neighboruing lanes, and so on.
For more details, feel free to read my report.

## Files, Folders and Specifications

In this directory, the report for this project is found in the file titled *COMP90072 Report 993443.pdf* which details the developmental processes and design of the traffic simulator and the prototypes before it. *Traffic_Simulation.mp4* contains the simulation animation played above, which the program produces when it runs each simulation.

The *Sand Pile Examples* folder only contains the images and animations used to construct this page, and is not necessary nor important otherwise. The *Prototypes* folder
contains the sand-pile prototypes I developed to familiarise myself with this style of program, and to learn its limitations before I started constructing the proper simulator. *Sand Pile Gradient.py* was the final prototype I developed before I decided the direction and programming techniques that would define the simulator. For more details on each, please refer to the report.

The *Final* folder houses the files necessary to run the simulation. It was designed to have its parameters customised by the user to test out different scenarios, and the program will provide example parameters to input for new users as well. To run the simulation, refer to these instructions:

1. Download the *Final* folder.
2. Open the program in a PyCharm IDE or equivalent. It is important that both Python files can run in the same window, because the simulation is dependent on both.
3. Run *Simulation_Example.py*, which loads simulation parameters to be read by *Traffic_Model.py*. You can edit the parameters to visualise traffic flow under different circumstances, including traffic flux, timestep advancement, and more. It is not recommended to change these parameters unless you have experience with the simulator and have fully read the report.
4. Run *Traffic_Model.py* and input extra parameters (the program provides default values). It will take some time to produce the simulation, but eventually an animation will play. If you have installed ffmpeg, the program will save the animation when you close the animation window as a mp4 file.

*Note: The simulation was developed with the following Python and library versions in mind. These versions have since been superseded and your experience may vary.*

*python version 3.11.2*

*matplotlib version 3.7.1*

*numpy version 2.2.3*

*scipy version 1.10.1*

*Note: It is also recommended to have ffmpeg installed on your computer, otherwise the program cannot save the simulation as an mp4 file to replay. This simulator makes heavy use
of random processes and so inputting the same paramaters again will not result in the same simulation. The simulation will still be produced even without ffmpeg however.*
