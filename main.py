import sys
from time import sleep

from eBoiler import Ui_eBoiler

from PyQt5 import QtWidgets

class GUI_setup(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_eBoiler()
        self.ui.setupUi(self)
        self.ui.Equipment1.setStyleSheet("Background: red")
        self.ui.ChangeColorButton.clicked.connect(self.changeColor)
        self.ui.disappearButton.clicked.connect(self.disappear)
        self.ui.appearButton.clicked.connect(self.appear)


    def disappear(self):
        visible = self.ui.Panel.isVisible()
        if visible:
            print('its visible')
        else:
            print('its invisible')

        self.ui.Panel.setVisible(False)

        visible = self.ui.Panel.isVisible()
        if visible:
            print('its visible')
        else:
            print('its invisible')

    def appear(self):
        self.ui.Panel.setVisible(True)

    def changeColor(self):

        self.ui.Equipment1.setStyleSheet("Background: green")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    sys.exit(app.exec_())