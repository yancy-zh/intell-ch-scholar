# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import pyqtgraph
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setGeometry(self.topleftX, self.topleftY, self.width, self.height)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))

        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        
        self.demoBtn = QtGui.QPushButton(self.centralwidget)
        self.demoBtn.setObjectName(_fromUtf8("demoBtn"))

        self.horizontalLayout.addWidget(self.startButton)
        self.horizontalLayout.addWidget(self.stopButton)
        self.horizontalLayout.addWidget(self.demoBtn)
        
        self.chkMore = QtGui.QCheckBox(self.centralwidget)
        self.chkMore.setObjectName(_fromUtf8("chkMore"))
        self.horizontalLayout.addWidget(self.chkMore)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.grPlot = pyqtgraph.PlotWidget(self.centralwidget) # insert a plot widget is from pyqtgraph
        self.vb = pyqtgraph.ViewBox()
        self.grPlot.addItem(self.vb)
        self.grPlot.setObjectName(_fromUtf8("grPlot")) 
        
        self.graph_text = pyqtgraph.TextItem()
        
        self.grPlot.addItem(self.graph_text)
        self.verticalLayout.addWidget(self.grPlot)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.startButton.setText(_translate("MainWindow", "start monitoring", None))
        self.stopButton.setText(_translate("MainWindow", "stop monitoring", None))
        self.demoBtn.setText(_translate("MainWindow", "demo with random data", None))
        self.chkMore.setText(_translate("MainWindow", "keep updating", None))
