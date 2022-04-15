
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.length import Ui_Length
from PySide6.QtGui import QIcon

class Length(QMainWindow):    
    def __init__(self, args):
        super(Length,self).__init__(args)
        self.ui = Ui_Length()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/imgs/scientific.png"))
        
       
        
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
        self.ui.btn_dot.clicked.connect(self.setDot)
        self.ui.btn_del_one.clicked.connect(self.deleteOne)
        # self.ui.btn_clear.clicked.connect(self.deleteAll)
        self.ui.btn_clear.clicked.connect(self.calculate( self.ui.comboBox2))
        # self.ui.comboBox1.currentIndexChanged.connect(self.calculate)
        self.ui.comboBox1.currentIndexChanged.connect(lambda:self.calculate(self.ui.comboBox1))
        self.ui.comboBox2.currentIndexChanged.connect(lambda:self.calculate(self.ui.comboBox2))
        self.ui.actionAbout.triggered.connect(self.about)
        # self.ui.actionStandar.triggered.connect(self.openStandarCalculator)
        # self.calculate()
        
    
    
        
    def about(self):
        QMessageBox.information(self,'Info','This is a temperature calculator v1.0.0\nDeveloped by IDCSchools \n \napr 01, 2022')
        
    
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
        
        self.calculate(self.ui.comboBox2) 
        
    def setDot(self):
        txt = str(self.ui.label_text.text())
        if '.' not in txt:
                self.ui.label_text.setText(txt + '.')

    def deleteOne(self):
        txt = str(self.ui.label_text.text())
        lessOne = len(txt)
        lessOne -= 1
        txt = txt[:lessOne]        
        self.ui.label_text.setText(txt)
        if len(txt) == 0 or txt == '-':
            self.ui.label_text.setText('0')
        self.calculate(self.ui.comboBox2)
        
    def deleteAll(self):
        self.ui.label_text.setText('0')
        self.calculate(self.ui.comboBox2)

    def calculate(self, btnBox):
        unit =  btnBox.currentText()
        # entryVal = float(self.ui.label_text.text())
        # firstLen = self.ui.comboBox1.currentText()
        # secondLen = self.ui.comboBox2.currentText() 
    
        
        m = float(self.ui.label_text.text())
        km = m / 1000
        
        cm = m * 100
        mm = cm * 10
                
        if unit == 'Meters':
            self.ui.label_result.setText(str(m))
        elif unit == 'Kilometers':
            self.ui.label_result.setText(str(km))        
        elif unit == 'Centimeters':
            self.ui.label_result.setText(str(cm))
        elif unit == 'Millimeters':
            self.ui.label_result.setText(str(mm))
                    # temp = 1.8 * (val - 273.15) + 32
            # temp = round(temp, 4)
            # self.ui.label_result.setText(self.delDecimal(temp))
            
    def delDecimal(self, numFloat):
        """
        Delete Decimals equal to '.0' and return an integer number
        for example:
        >>> delDecimal(489.000)
        489
        
        If module is mayor than '.00' or '.0' then it will return a float number
        >>> delDecimal(590.902)
        590.902
        
        """
        txt = str(numFloat)
        if txt.endswith('.0'):
            lessOne = len(txt)
            lessOne -= 2
            txt = txt[:lessOne] 
        return txt
