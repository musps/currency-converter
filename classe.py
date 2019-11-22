from currency_converter import CurrencyConverter
from PySide2 import QtCore
from PySide2.QtWidgets import QDialog, QLineEdit, QPushButton, QHBoxLayout, QComboBox

def parseToFloat(value, valueOnError = None):
    try:
        return round(float(value), 2)
    except ValueError:
        return valueOnError

class CurrencyConverter(QDialog):
    c = CurrencyConverter()
    ui_max_width = 150
    currencies = []
    value1 = 1
    value2 = None
    device1 = 'EUR'
    devise2 = 'USD'

    def __init__(self, parent = None):
        super(CurrencyConverter, self).__init__(parent)
        self.setWindowTitle('Convertisseur de devises')
        self.setStyleSheet('background-color: #333;')
        self.setMinimumSize(800, 220)
        self.initCurrencies()
        self.addForm()

    def initCurrencies(self):
        self.currencies = sorted(self.c.currencies)

    def initDefaultCurrency(self, selec, code):
        index = selec.findText(code, QtCore.Qt.MatchFixedString)
        if index >= 0:
            selec.setCurrentIndex(index)

    def onInputChange(self, action, force = False):
        device1 = self.device1_select.currentText()
        devise2 = self.device2_select.currentText()
        value1 = self.device1_input.text()
        value2 = self.device2_input.text()
        value1 = parseToFloat(value1, 0)
        value2 = parseToFloat(value2, 0)

        if action == 'UPDATE_INPUT_1' and (force or value1 != parseToFloat(self.value1)):
            if value1 < 0:
              self.device2_input.setText(str(0.0))
              return

            nextValue = parseToFloat(self.c.convert(value1, device1, devise2))
            self.value1 = value1
            self.value2 = nextValue
            self.device2_input.setText(str(nextValue))

        if action == 'UPDATE_INPUT_2' and (force or value2 != parseToFloat(self.value2)):
            if value2 < 0:
              self.device1_input.setText(str(0.0))
              return

            nextValue = parseToFloat(self.c.convert(value2, devise2, device1))
            self.value2 = value2
            self.value1 = nextValue
            self.device1_input.setText(str(nextValue))

    def onDeviceChange(self, action, index):
        currency = self.currencies[index]
        if action == 'UPDATE_SELECT_1':
            self.onInputChange('UPDATE_INPUT_2', True)
        if action == 'UPDATE_SELECT_2':
            self.onInputChange('UPDATE_INPUT_1', True)

    def initDefaultValues(self):
        self.onInputChange('UPDATE_INPUT_1', True)

    def onInput1Change(self, value):
        self.onInputChange('UPDATE_INPUT_1')

    def onInput2Change(self, value):
        self.onInputChange('UPDATE_INPUT_2')

    def onDevice1Change(self, i):
        self.onDeviceChange('UPDATE_SELECT_1', i)

    def onDevice2Change(self, i):
        self.onDeviceChange('UPDATE_SELECT_2', i)

    def onClickDeviceInvert(self):
        device1 = self.device1_select.currentText()
        devise2 = self.device2_select.currentText()
        value1 = self.device1_input.text()
        value2 = self.device2_input.text()

        self.initDefaultCurrency(self.device1_select, devise2)
        self.initDefaultCurrency(self.device2_select, device1)
        self.device1_input.setText(str(value2))
        self.device2_input.setText(str(value1))

    def addForm(self):
        layout = QHBoxLayout()

        self.device1_select = QComboBox()
        self.device1_input = QLineEdit()
        self.device2_select = QComboBox()
        self.device2_input = QLineEdit()
        self.device_invert = QPushButton('Inverser devises')

        self.device_invert.clicked.connect(self.onClickDeviceInvert)

        self.device1_select.setFixedWidth(self.ui_max_width)
        self.device2_select.setFixedWidth(self.ui_max_width)
        self.device1_select.addItems(self.currencies)
        self.device2_select.addItems(self.currencies)

        self.initDefaultCurrency(self.device1_select, self.device1)
        self.initDefaultCurrency(self.device2_select, self.devise2)

        self.device1_select.currentIndexChanged.connect(self.onDevice1Change)
        self.device2_select.currentIndexChanged.connect(self.onDevice2Change)

        self.device1_input.setFixedWidth(self.ui_max_width)
        self.device2_input.setFixedWidth(self.ui_max_width)

        self.device1_input.setText(str(self.value1))
        self.initDefaultValues()

        self.device1_input.textChanged.connect(self.onInput1Change)
        self.device2_input.textChanged.connect(self.onInput2Change)

        self.device1_select.setStyleSheet("color: white;")
        self.device2_select.setStyleSheet("color: white;")
        self.device1_input.setStyleSheet("color: white;")
        self.device2_input.setStyleSheet("color: white;")
        self.device_invert.setStyleSheet("color: white;")

        layout.addWidget(self.device1_select)
        layout.addWidget(self.device1_input)
        layout.addWidget(self.device2_select)
        layout.addWidget(self.device2_input)
        layout.addWidget(self.device_invert)
        self.setLayout(layout)
