'''
Created on 15.03.2020

@author: Yao Zhang
'''

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys
import ui_main # import the ui
import numpy as np
import time
import pyqtgraph
import serial
import threading

class HeatmapVisApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    # draw the gui
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') # before loading widget
        super(HeatmapVisApp, self).__init__(parent) # referring to the base class explicitly
        self.topleftX = 40
        self.topleftY = 100
        self.width = 1760
        self.height = 546
        self.num_rows = 4
        self.num_cols = 16
        self.min_val = 10
        self.max_val = 80
        self.defaultColorMap = np.linspace(self.min_val, self.max_val, self.num_cols * self.num_rows, dtype = float)
        self.setupUi(self)
        self.grPlot.plotItem.setXRange(.5, 15.1)
        self.grPlot.plotItem.setYRange(.5, 4.7)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        
        # monitor the data from the serial port and update the visualization
        self.monitor = SerialMonitor()
        self.monitor.bufferUpdated.connect(self.update)
        self.startButton.clicked.connect(self.monitor.start)
        self.stopButton.clicked.connect(self.monitor.stop)
        self.demoBtn.clicked.connect(self.update)
        
    def update(self, *args, **kwargs):
        t1=time.clock() # get the current processor time
        # generate an array with exactly 64 temperature values range from (min_val, max_val)
        dataList = self.defaultColorMap
        if kwargs is not None:
            for key, value in kwargs.items():
                print("%s == %s" %(key,value))
                if key == 'defaultColorMap':
                    if value == True:
                        print ("initializing the GUI")
                        dataList = self.defaultColorMap
                        
        if args is not None and len(args) != 0:
            if isinstance(args[0], (bool)):
                dataList = np.random.rand(self.num_cols * self.num_rows) * (self.max_val - self.min_val) + np.ones(self.num_cols * self.num_rows, dtype = float) * self.min_val
            elif isinstance(args[0], (list)):
                dataList = args[0]
            else:
                print("unexpected data type in the arguments!")
        elif len(args) == 0 and len(kwargs) == 0:
                dataList = np.random.rand(self.num_cols * self.num_rows) * (self.max_val - self.min_val) + np.ones(self.num_cols * self.num_rows, dtype = float) * self.min_val
                
        values_to_visualize = dataList
        
        # store the temperature data in a dictionary
        data_with_position={'value': values_to_visualize,
                    'pos_y_rows': np.arange(self.num_rows, 0, -1).repeat(self.num_cols),
                    'pos_x_cols': np.tile(np.arange(1, self.num_cols+1), self.num_rows)}
#
        len_of_data = len(values_to_visualize)
        color_ls = []
        pens = []
        brushes = []
        # generate the colors for each temperature value, the pens and brushes to render the points
        for ii in np.arange(len_of_data):
            curr_color = QtGui.QColor(0,0,0) if data_with_position['value'][ii] is np.NaN else pyqtgraph.hsvColor((1 - (data_with_position['value'][ii]-self.min_val)/(self.max_val - self.min_val)) * .65, alpha = .9) # alpha decides transparency channel
            color_ls.append(curr_color)
            pens.append(pyqtgraph.mkPen(color=curr_color, width=100))
            brushes.append(pyqtgraph.mkBrush(color=curr_color, width=100))
#         print "temperature val: {}".format(values_to_visualize)
#         print "percentage of temperature val: {}".format((data_with_position['value']-self.min_val)/(self.max_val - self.min_val))

        # display the heat map using a scatter plot
        self.grPlot.scatterPlot(data_with_position['pos_x_cols'], data_with_position['pos_y_rows'], pxMode = False, symbol = 'd', pen=pens, brush = brushes, size = .25, antialias=True, clear=True)
        
        plotVb = self.grPlot.getPlotItem().getViewBox()
        plotVb.setMouseEnabled(x = False, y = False)         # disable the scaling
        
        # remove the old text item, insert labels for temperature values
        self.grPlot.removeItem(self.graph_text)
        # format the text with the html style sheet
        html_table_css = """
            <table width = \"1360\" height = \"340\" cellpadding = \"34\">
           <tr> 
           <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td> 
           </tr>
           
           <tr>
           
           <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>
           </tr>   
           
            <tr>
                <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>
            </tr>
            
            <tr>
                <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>     <td>%0.0f</td>     <td>%0.0f</td> <td>%0.0f</td>
            </tr>

         </table>"""
        
        self.graph_text = pyqtgraph.TextItem(anchor = (0, 0), html = html_table_css %tuple(data_with_position['value']), color = 'k')
        self.graph_text.setPos(0.5, 4.5)
        self.graph_text.setFont(QtGui.QFont("TypeWriter", 16, QtGui.QFont.Bold))
        self.grPlot.addItem(self.graph_text, ignorebounds = True)
        self.graph_text.show()
        
        print("update took %.02f ms"%((time.clock()-t1)*1000))
        if self.chkMore.isChecked():
            QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

class SerialMonitor(QtCore.QObject):
    bufferUpdated = QtCore.pyqtSignal(object)
    
    def __init__(self):
        super(SerialMonitor, self).__init__()
        self.serial_args = dict(port = 'COM3',
                                baudrate = 115200,
                                timeout = 0.3)
        self.running = False
        self.thread = threading.Thread(target=self.serial_monitor_thread)

    def start(self):
        self.running = True
        if not self.thread._Thread__started.is_set():
            self.thread.start()
            print("Serial Monitor has started")

    def stop(self):
        self.running = False
        print("Serial Monitor has stopped")

    def serial_monitor_thread(self):
        while self.running is True:
            ser = serial.Serial(**self.serial_args)
            # read 1000 bytes and cut the line by timeout
            msg = ser.read(1000)
            if msg:
                try:
                    if( 'IR_DATA' in msg):
                        ir_data = msg.split(':')
                        pure_temperature_values = []
                        parsed_data = ir_data[1].split(',')[0:-1]
                        print("original temperature data: {} \n and the length is {}".format(parsed_data, len(parsed_data)))
                        for ss in parsed_data:
                            floatVal = 0.0
                            try:
                                floatVal = float(ss)
                            except ValueError: # if the value is not a float, append NaN to the list
                                floatVal = np.nan
                            
                            pure_temperature_values.append(floatVal)
#                         print "parsed data array: {}".format(pure_temperature_values)
                        if len(pure_temperature_values) == 64:
#                             print pure_temperature_values
                            self.bufferUpdated.emit(pure_temperature_values)
                        else:
                            pass
                except ValueError:
                    print('Wrong data')
            else:
                pass
            ser.close()
            
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = HeatmapVisApp()
    form.show()
    form.update(defaultColorMap = True) # start by plotting the standard color map
    app.exec_()
    
    print("DONE")