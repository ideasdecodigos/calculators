from PySide6.QtWidgets import  QMainWindow, QMessageBox
from views.properties import Ui_Properties
from configparser import ConfigParser
from pathlib import Path

class Properties(QMainWindow):    
    def __init__(self):
        super(Properties,self).__init__()
        self.ui=Ui_Properties()
        self.ui.setupUi(self)
        #config file path
        self.configFilePath ='src/files/db.ini'
        
        
        self.ui.pushButtonReset.clicked.connect(self.read)
        self.ui.pushButtonSave.clicked.connect(self.changeProperties)
        
        
    def read(self):
        self.config = ConfigParser()
        self.config.read(self.configFilePath)
        
        if self.config.has_section('properties'):
            print('yes, it has')
            self.properties = list(self.config['properties'])
        else:
            print('No, it has not')
            self.config.add_section('properties')
            self.config.set('properties', 'bgColor', 'yellow')
            self.config.set('properties', 'ftColor', 'darkblue')
            self.config.set('properties', 'decimalsLen', '4')
            with open(self.configFilePath, 'w') as conf:
                self.config.write(conf)
                QMessageBox.information(self,'Info', 'Config file created successfully!', QMessageBox.Ok)
        
    def changeProperties(self):
        self.config = ConfigParser()
        
        if Path(self.configFilePath).exists():
            self.config.read(self.configFilePath)
            if self.config.has_section('properties'):
                try:
                    self.config['properties']['bgColor'] = self.ui.comboBoxBgColor.currentText()
                    self.config['properties']['ftColor'] = self.ui.comboBoxFtColor.currentText()
                    self.config['properties']['decimalsLen'] =str(self.ui.spinBoxDecimal.value()) 
                    with open(self.configFilePath, 'w') as conf:
                        self.config.write(conf)
                        QMessageBox.information(self,'Info', 'Restart the app to see the changes!', QMessageBox.Ok)                  
                except:
                    QMessageBox.warning(self,'Warning', 'An error occurred!', QMessageBox.Ok) 
            else:
                QMessageBox.warning(self,'Warning', 'Section not found!', QMessageBox.Ok) 
            
        else:
            QMessageBox.warning(self,'Warning', 'File not found', QMessageBox.Ok) 

    def newProperties(self):
        self.config = ConfigParser()     
        
        if Path('src/files/db.ini').exists():
            self.config.read('src/files/db.ini')
            if self.config.has_section('properties'):
                try:                    
                    bgColor =  self.config['properties']['bgColor'] 
                    ftColor = self.config['properties']['ftColor'] 
                    dcLen = self.config['properties']['decimalsLen']
                    style = "background:{0};color:{1};"
                    style = style.format(bgColor, ftColor)
                    self.setStyleSheet("QWidget{"+ style +"}")
                except:
                    pass
