import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton 
from PyQt5.QtWidgets import QLabel, QLCDNumber
import PyQt5.QtGui as QtGui
import math

 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(400, 300, 400, 300)
        self.setWindowTitle('calculator!') 
        
        self.label = QLabel(self)
        self.label.setText("")
        self.label.setGeometry(200, 500, 500, 20)
        self.label.move(10, 30)  
        
        self.label2 = QLabel(self)
        self.label2.setText("")
        self.label2.setGeometry(200, 500, 500, 20)
        self.label2.move(10, 15)          
        
        self.btn1 = QPushButton('1', self)
        self.btn1.resize(50, 50)
        self.btn1.move(10, 60)
        self.btn1.clicked.connect(self.priny) 
        
        self.btn2 = QPushButton('2', self)
        self.btn2.resize(50, 50)
        self.btn2.move(70, 60) 
        self.btn2.clicked.connect(self.priny) 
        
        self.btn3 = QPushButton('3', self)
        self.btn3.resize(50, 50)
        self.btn3.move(130, 60) 
        self.btn3.clicked.connect(self.priny) 
        
        self.btn4 = QPushButton('4', self)
        self.btn4.resize(50, 50)
        self.btn4.move(10, 120) 
        self.btn4.clicked.connect(self.priny) 
        
        self.btn5 = QPushButton('5', self)
        self.btn5.resize(50, 50)
        self.btn5.move(70, 120) 
        self.btn5.clicked.connect(self.priny) 
        
        self.btn6 = QPushButton('6', self)
        self.btn6.resize(50, 50)
        self.btn6.move(130, 120)
        self.btn6.clicked.connect(self.priny) 
        
        self.btn7 = QPushButton('7', self)
        self.btn7.resize(50, 50)
        self.btn7.move(10, 180)  
        self.btn7.clicked.connect(self.priny) 
        
        self.btn8 = QPushButton('8', self)
        self.btn8.resize(50, 50)
        self.btn8.move(70, 180) 
        self.btn8.clicked.connect(self.priny) 
        
        self.btn9 = QPushButton('9', self)
        self.btn9.resize(50, 50)
        self.btn9.move(130, 180) 
        self.btn9.clicked.connect(self.priny) 
        
        self.btn0 = QPushButton('0', self)
        self.btn0.resize(50, 50)
        self.btn0.move(10, 240) 
        self.btn0.clicked.connect(self.priny) 
        
        self.btndot = QPushButton('.', self)
        self.btndot.resize(50, 50)
        self.btndot.move(70, 240) 
        self.btndot.clicked.connect(self.priny) 
        
        self.btneq = QPushButton('=', self)
        self.btneq.resize(50, 50)
        self.btneq.move(130, 240)  
        self.btneq.clicked.connect(self.priny) 
        
        self.lf = QPushButton('(', self)
        self.lf.resize(40, 40)
        self.lf.move(190, 60)  
        self.lf.clicked.connect(self.priny)         
         
        self.rt = QPushButton(')', self)
        self.rt.resize(40, 40)
        self.rt.move(240, 60)  
        self.rt.clicked.connect(self.priny)                 
        self.plus = QPushButton('+', self)
        self.plus.resize(40, 40)
        self.plus.move(190, 110)  
        self.plus.clicked.connect(self.priny)        
        
        self.minus = QPushButton('-', self)
        self.minus.resize(40, 40)
        self.minus.move(240, 110)  
        self.minus.clicked.connect(self.priny)
        
        self.times = QPushButton('*', self)
        self.times.resize(40, 40)
        self.times.move(190, 160)  
        self.times.clicked.connect(self.priny)
        
        self.divide = QPushButton('/', self)
        self.divide.resize(40, 40)
        self.divide.move(240, 160)  
        self.divide.clicked.connect(self.priny) 
        
        self.deg = QPushButton('^', self)
        self.deg.resize(40, 40)
        self.deg.move(190, 210)  
        self.deg.clicked.connect(self.priny)  
        
        
        
        self.sqroot = QPushButton('sqrt(', self)
        self.sqroot.resize(40, 40)
        self.sqroot.move(240, 210)  
        self.sqroot.clicked.connect(self.priny)  
        
        self.sin = QPushButton('sin(', self)
        self.sin.resize(40, 40)
        self.sin.move(290, 110)  
        self.sin.clicked.connect(self.priny)         
        
        self.cos = QPushButton('cos(', self)
        self.cos.resize(40, 40)
        self.cos.move(340, 110)  
        self.cos.clicked.connect(self.priny)               
        
        self.tan = QPushButton('tan(', self)
        self.tan.resize(40, 40)
        self.tan.move(290, 160)  
        self.tan.clicked.connect(self.priny) 
        
        self.log = QPushButton('log(', self)
        self.log.resize(40, 40)
        self.log.move(340, 160)  
        self.log.clicked.connect(self.priny)     
        
        self.pi = QPushButton('π', self)
        self.pi.resize(40, 40)
        self.pi.move(290, 210)  
        self.pi.clicked.connect(self.priny)           
        
        self.fact = QPushButton('factorial(', self)
        self.fact.resize(50, 30)
        self.fact.move(190, 260)  
        self.fact.clicked.connect(self.priny)          


        self.clr = QPushButton('CLR ALL', self)
        self.clr.resize(50, 40)
        self.clr.move(290, 60)  
        self.clr.clicked.connect(self.priny)  
        
        self.sqroot = QPushButton('CE', self)
        self.sqroot.resize(50, 40)
        self.sqroot.move(340, 60)  
        self.sqroot.clicked.connect(self.priny)         
        
        
        self.show()                 
 
    def priny(self):
        t1 = str(self.label.text())
        t2 = str((self.sender().text()))
        if t2 == 'CLR ALL':
            self.label.setText('')
            self.label2.setText('')
        elif t2 == 'CE':
            t1 = t1[:-1]
            self.label.setText(t1)
        elif t2 == '=':
                line = t1.replace('sqrt(' , 'math.sqrt(')
                line = line.replace('^' , '**') 
                
                line = line.replace('sin(' , 'math.sin(')
                line = line.replace('cos(' , 'math.cos(')
                line = line.replace('tan(' , 'math.tan(')
                line = line.replace('log(' , 'math.log(')
                line = line.replace('π', '3.14159265359')
                line = line.replace('factorial(', 'math.factorial(')
                

                try: 
                    answer = str(eval(str(line)))
                    self.label.setText(answer)
                    self.label2.setText(t1 + ' =')
                except Exception as e:
                    mstk = str(type(e))[8:]
                    line2 = mstk[:-2]                    
                    self.label.setText(line2)
                    self.label2.setText(t1)
        else:
            line = t1 + t2
            self.label.setText(t1 + t2)
           
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())  
