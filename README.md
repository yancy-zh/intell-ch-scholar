# Serial Heatmap Visualizer 
This is a heat map visualization graphic user interface developed with PyQt4 GUI and Pyqtgraph libraries. The application
 can receive the data of 64 values from the serial port and display the values with the corresponding colors on a 16*4 grid,
  named as "heat map" here. The 64 values contain the measured temperature in the nearby area of the sensor. The color of 
  each cell in the scatter plot represents the temperature that is labeled on this cell. 

## Getting Started
To get the depository of this project, click "clone or download" in github, copy the address that is showing, which is 
the [Github repo of serial heatamp project](https://github.com/yancy-zh/serialHeatmap.git). Use this address in your 
local Git client software, such as [TortiseGit](https://tortoisegit.org/download/), or simply the
 [Git Bash command line tool](https://git-scm.com/downloads) to clone this repository to your local machine. 
TortoiseGit supports Windows sytem, while the normal Git bash terminal supports all available operation systems. 

### Prerequisites
To use the source codes of this project, a python based development environment should be installed in your system, such
 as: PyCharm, Eclipse, Visual Studio Code. 
 The requirements for the software and package versions are as below:
 - Python 3.6+
 - PyQt4 4.11
 - pyqtgraph 0.10
 - pyserial 3.4
 When the python IDE is ready, import or open the project from the cloned repository. 
### Structure of this software
1. The ui_main.py contains the user interface including buttons and a display window of the heatmap, and a screenshot of
which can be found under <root_of_the_project>/heatmap_GUI.png. 
2. The file main.py contains the classes to monitor the serial port input, and transfer the incoming data to a heatmap 
for display.  
### Starting to run
To display the heap map from the sensor through the serial port, click the button "start monitoring". The monitoring of 
the serial port can be stopped by clicking "stop monitoring", but it can not be started again by the buttons unless the 
application is restarted. 

To demonstrate with dummy data, click the "demo with random data" button to display a group of random temperature values.
 Check the "keep updating" box to refresh the heat map continuously.
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
This software is developed based on a Python UI template provided by [Scott W Harden](https://www.swharden.com/wp/home/). 
