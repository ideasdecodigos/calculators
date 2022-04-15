
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.temperature import Ui_Temperature
from model.length import Length
from model.time import Time
from model.main_defs import Modules
from model.properties import Properties

class Temperature(QMainWindow, Modules):    
    def __init__(self):
        super(Temperature,self).__init__()
        self.ui = Ui_Temperature()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/imgs/temp.png"))
        
        Properties.newProperties(self) 
        
        #*******BUTTON'S ACTIONS        
        self.ui.btn1.clicked.connect(lambda:self.getBtnText(self.ui.btn1))
        self.ui.btn2.clicked.connect(lambda:self.getBtnText(self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda:self.getBtnText(self.ui.btn3))
        self.ui.btn4.clicked.connect(lambda:self.getBtnText(self.ui.btn4))
        self.ui.btn5.clicked.connect(lambda:self.getBtnText(self.ui.btn5))
        self.ui.btn6.clicked.connect(lambda:self.getBtnText(self.ui.btn6))
        self.ui.btn7.clicked.connect(lambda:self.getBtnText(self.ui.btn7))
        self.ui.btn8.clicked.connect(lambda:self.getBtnText(self.ui.btn8))
        self.ui.btn9.clicked.connect(lambda:self.getBtnText(self.ui.btn9))
        self.ui.btn0.clicked.connect(lambda:self.getBtnText(self.ui.btn0))
        self.ui.btn_dot.clicked.connect(lambda:Modules.setDot(self.ui.label_text))
        self.ui.btn_del_one.clicked.connect(self.deleteOne)
        # self.ui.btn_clear.clicked.connect(self.deleteAll)
        self.ui.btn_clear.clicked.connect(self.oproperties)
        self.ui.comboBox1.currentIndexChanged.connect(self.calculate)
        self.ui.comboBox2.currentIndexChanged.connect(self.calculate)
        self.ui.btn_inverse.clicked.connect(self.inverseText)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        # self.ui.actionStandar.triggered.connect(self.openStandarCalculator)
        self.ui.actionLenght.triggered.connect(self.openLengthCalculator)
        self.ui.actionStandar.triggered.connect(self.openTimeCalculator)
        self.calculate()
    
    
    def oproperties(self):
        self. wind = Properties()
        self.wind.show()
        
    
    #****FUNCTIONS CREATION    
    def getBtnText(self, btn):
        """
        get the buttons text and set it to labelOne
        
        """
        txt = ''        
        if self.ui.label_text.text() != '0':
            txt = self.ui.label_text.text()
        if len(txt) <= 16:
            txt += btn.text()
            self.ui.label_text.setText(txt)            
        self.calculate() 
        
   
    def inverseText(self):
        txt = float(self.ui.label_text.text())
        txt *= -1
        txt = str(txt)
        if txt.endswith('.0'):
            lessOne = len(txt)
            lessOne -= 2
            txt = txt[:lessOne]
        self.ui.label_text.setText(txt)
        self.calculate()
        
    def deleteOne(self):
        txt = str(self.ui.label_text.text())
        lessOne = len(txt)
        lessOne -= 1
        txt = txt[:lessOne]        
        self.ui.label_text.setText(txt)
        if len(txt) == 0 or txt == '-':
            self.ui.label_text.setText('0')
        self.calculate()
        
    def deleteAll(self):
        self.ui.label_text.setText('0')
        self.calculate()

    def calculate(self):
        val = float(self.ui.label_text.text())
        firstTemp = self.ui.comboBox1.currentText()
        secondTemp = self.ui.comboBox2.currentText()    
        
        if firstTemp == secondTemp:
            self.ui.label_result.setText(str(val))
            
            #°F = 1.8 °C + 32°
        elif ((firstTemp == 'Celsius') and (secondTemp == 'Fahrenheit')):
            
            temp = 1.8 * val + 32
            temp = round(temp, 4)
            self.ui.label_result.setText(Modules.delDecimal(temp))
            
            #K = °C + 273°
        elif ((firstTemp == 'Celsius') and (secondTemp == 'Kelvin')):
            temp = val + 273.15
            temp = round(temp, 4)
            self.ui.label_result.setText(Modules.delDecimal(temp))
            
            #K = 5/9 (ºF – 32) + 273.15
        elif ((firstTemp == 'Fahrenheit') and (secondTemp == 'Kelvin')):
            temp = 5/9 * (val - 32) + 273.15
            temp = round(temp, 4)
            self.ui.label_result.setText(Modules.delDecimal(temp))
            
            #°C =5/9(°F-32°)
        elif ((firstTemp == 'Fahrenheit') and (secondTemp == 'Celsius')):
            temp = 5/9 * (val - 32)
            temp = round(temp, 4)
            self.ui.label_result.setText(Modules.delDecimal(temp))         
            
            #°C = K - 273°
        elif ((firstTemp == 'Kelvin') and (secondTemp == 'Celsius')):
            temp = val - 273.15
            temp = round(temp, 4)
            self.ui.label_result.setText(Modules.delDecimal(temp))
            
            #ºF = 1.8(K – 273.15) + 32.
        elif ((firstTemp == 'Kelvin') and (secondTemp == 'Fahrenheit')):
            temp = 1.8 * (val - 273.15) + 32
            temp = round(temp, 4)
            self.ui.label_result.setText(Modules.delDecimal(temp))
            
    