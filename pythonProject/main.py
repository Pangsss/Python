from PyQt5 import QtWidgets

from MainPage import Ui_MainPage
from Display import Ui_Form


class first_window(QtWidgets, Ui_MainPage):
    def __int__(self, parent = None):
        super(Ui_MainPage, self).__int__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Display)


    def 
