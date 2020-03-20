'''
Created on 16.03.2020

@author: Yao Zhang
'''
This is a heat map visualization graphic user interface developed with PyQt4 GUI and Pyqtgraph libraries. The application can receive the data of 64 values from the serial port and display the values with the corresponding colors on a 16*4 grid, named as "heat map" here. The 64 values contain the measured temperature in the nearby area of the sensor. The color of each cell in the scatter plot represents the temperature that is labeled on this cell. 

To display the heap map from the sensor through the serial port, click the button "start monitoring". The monitoring of the serial port can be stopped by clicking "stop monitoring", but it can not be started again by the buttons unless the application is restarted. 

To demonstrate with dummy data, click the "demo with random data" button to display a group of random temperature values. Check the "keep updating" box to refresh the heat map continuously.

