from .ui import Ui_CalculatorWindow
from PyQt5 import QtWidgets

from sympy import sympify


class CalculatorWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CalculatorWindow()
        self.ui.setupUi(self)
        self.txt = ''
        
        self.ui.left_pt_btn.clicked.connect(self.on_click)
        self.ui.right_pt_btn.clicked.connect(self.on_click)
        self.ui.seven_btn.clicked.connect(self.on_click)
        self.ui.eight_btn.clicked.connect(self.on_click)
        self.ui.nine_btn.clicked.connect(self.on_click)
        self.ui.four_btn.clicked.connect(self.on_click)
        self.ui.five_btn.clicked.connect(self.on_click)
        self.ui.six_btn.clicked.connect(self.on_click)
        self.ui.one_btn.clicked.connect(self.on_click)
        self.ui.two_btn.clicked.connect(self.on_click)
        self.ui.three_btn.clicked.connect(self.on_click)
        self.ui.zero_btn.clicked.connect(self.on_click)
        self.ui.minus_btn.clicked.connect(self.on_click)
        self.ui.parcent_btn.clicked.connect(self.on_click)
        self.ui.multiplication_btn.clicked.connect(self.on_click)
        self.ui.plus_btn.clicked.connect(self.on_click)
        self.ui.devisions_btn.clicked.connect(self.on_click)
        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.equals_btn.clicked.connect(self.equal)
        self.ui.back_btn.clicked.connect(self.trim_last_char)
    
    def on_click(self):
        self.txt += self.sender().text()
        self.ui.result_input_lbl.setText(self.txt)
        self.ui.expression_lbl.setText('')
        self.ui.error_lbl.setText('')
    
    def equal(self):
        try:
            result = str(sympify(self.txt))
            if 'zoo' in result:
                raise ZeroDivisionError
            self.ui.result_input_lbl.setText(result)
            self.ui.expression_lbl.setText(self.txt + '=')
            self.txt = result
        except (SyntaxError, ValueError, ZeroDivisionError):
            self.ui.error_lbl.setText('Incorrect expression')
    
    def trim_last_char(self):
        self.txt = self.txt[:-1]
        self.ui.result_input_lbl.setText(self.txt)
      
    def clear(self) -> None:
        self.txt = ''
        self.ui.result_input_lbl.setText(self.txt)
        self.ui.expression_lbl.setText('')