# -- coding: utf-8 --
"""
Created on Tue Jul  7 20:30:25 2020
IDE : Spyder
ANACONDA Distribution
@author: LALIT ARORA
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QLabel, QFrame, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import time

last_solved_cell = []

values =[[3, 0, 0, 7, 0, 1, 2, 0, 0], 
          [2, 0, 0, 0, 0, 3, 0, 1, 4], 
          [0, 5, 4, 6, 0, 0, 7, 0, 0], 
          [0, 9, 0, 3, 0, 2, 0, 8, 0], 
          [8, 0, 7, 0, 0, 0, 0, 6, 5], 
          [0, 0, 0, 8, 7, 0, 9, 0, 0], 
          [0, 0, 3, 2, 0, 9, 0, 0, 6], 
          [0, 1, 6, 0, 0, 0, 4, 2, 0], 
          [7, 0, 0, 0, 3, 6, 0, 0, 0]] 

class Ui_ElectKitv1(object):
    def setupUi(self, ElectKitv1):
        ElectKitv1.setObjectName("ElectKitv1")
        ElectKitv1.resize(616, 443)
        ElectKitv1.setMaximumSize(QtCore.QSize(616, 443))
        self.grid_layout = QGridLayout(ElectKitv1)
        self.current_grid = values
        self.labels = {}

        for i in range(len(values)):
            for j in range(len(values[0])):
                value = values[i][j]
                self.labels[(i, j)] = QLabel('label {},{}'.format(i, j))
                self.labels[(i,j)].setText(str(value))
                self.labels[(i,j)].setFixedSize(80, 80)
                self.labels[(i,j)].setFrameShape(QFrame.Panel)
                self.labels[(i,j)].setFrameShadow(QFrame.Sunken)
                self.labels[(i,j)].setLineWidth(1)
                self.labels[(i,j)].setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                newfont = QtGui.QFont("Times", 26)
                self.labels[(i,j)].setFont(newfont)
                position = (i,j)
                self.grid_layout.addWidget(self.labels[(i,j)], *position)
        self.beautify_board()
        self.retranslateUi(ElectKitv1)
        QtCore.QMetaObject.connectSlotsByName(ElectKitv1)
        #self.solve_sudoku()

    def retranslateUi(self, ElectKitv1):
        _translate = QtCore.QCoreApplication.translate
        ElectKitv1.setWindowTitle(_translate("ElectKitv1", "SUDOKU SOLVER"))
    
    
    def beautify_board(self):
        grey_background = []
        for i in range(0,3):
            for j in range(3,6):
                grey_background.append((i,j))
        for i in range(3,6):
            for j in range(0,3):
                grey_background.append((i,j))
        for i in range(3,6):
            for j in range(6,9):
                grey_background.append((i,j))
        for i in range(6,9):
            for j in range(3,6):
                grey_background.append((i,j))
        
        for i in range(len(values)):
            for j in range(len(values[0])):
                if values[i][j] != 0:
                    if (i,j) in grey_background:
                        self.labels[(i,j)].setStyleSheet("background-color: lightgrey; color: red;")
                    else:
                        self.labels[(i,j)].setStyleSheet("color: red;")
                else:
                    if (i,j) in grey_background:
                        self.labels[(i,j)].setStyleSheet("background-color: lightgrey; color: blue;")
                    else:
                        self.labels[(i,j)].setStyleSheet("color: blue;")

    def solve_sudoku(self):
        self.threadClass = ThreadClass()
        self.threadClass.signal_value.connect(self.update_board)
        self.threadClass.start()

    def update_board(self,signal):
        print(signal)
        [a,b,c] = signal.split('_')
        self.labels[(int(a),int(b))].setText(str(c))
        

class ThreadClass (QThread):
    
    signal_value = pyqtSignal(str)
    
    def _init_(self,parent=None):
        super(ThreadClass,self)._init_(parent)
        
        
        
    def isSafetoaddinrow(self,grid,row,column,num):
        if num in grid[row]:
            return False
        else:
            return True

    def isSafetoaddincol(self,grid,row,column,num):
        length = len(grid)
        for i in range(length):
            if grid[i][column]==num:
                return False
        
        return True

    def isSafetoaddinbox(self,grid,row,column,num):
        row_start = 3*int(row/3)
        col_start = 3*int(column/3)
        for i in range(row_start,row_start+3):
            for j in range(col_start,col_start+3):
                if grid[i][j]==num:
                    return False
        return True

    def isSafetoadd(self,grid,row,column,num):
        sig = str(row)+""+str(column)+""+str(num)
        time.sleep(0.1)
        self.signal_value.emit(sig)
        return self.isSafetoaddinbox(grid,row,column,num) and self.isSafetoaddincol(grid,row,column,num) and self.isSafetoaddinrow(grid,row,column,num)
    
    def checkemptyspace(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    return (i,j)
        return (-1,-1)
    

    def solvecell(self,grid,row,column,last):
        if grid[row][column] != 0 and last != 1 :
            return True
        for i in range(grid[row][column]+1,10):
            if (self.isSafetoadd(grid,row,column,i)):
                grid[row][column] = i
                last_solved_cell.append((row,column))
                return True
        grid[row][column] = 0
        coordinates = last_solved_cell.pop()
        return (self.solvecell(grid,coordinates[0],coordinates[1],1))
    
    def run(self):
        row = 0
        col = 0
        grid = values
        while (row != -1 or col != -1):
            if self.solvecell(grid,row,col,0):
                (row,col) = self.checkemptyspace(grid)
        

if _name_ == "_main_":
    import sys
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    ElectKitv1 = QtWidgets.QWidget()
    ui = Ui_ElectKitv1()
    ui.setupUi(ElectKitv1)
    ElectKitv1.show()
    sys.exit(app.exec_())