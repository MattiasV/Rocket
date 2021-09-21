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
        self.ui.progressBarButton.clicked.connect(self.progressbar)


    def progressbar(self):
        for i in range(101):
            sleep(i / 1000)
            self.ui.progressBar.setValue(i)


    def disappear(self):
        visible = self.ui.Panel_1.isVisible()
        if visible:
            print('its visible')
        else:
            print('its invisible')

        self.ui.Panel_1.setVisible(False)
        #sleep(1)
        self.ui.Panel_2.setVisible(True)

        visible2 = self.ui.Panel_2.isVisible()
        if visible2:
            print('its visible 2')
        else:
            print('its invisible 2')

    def appear(self):
        self.ui.Panel.setVisible(True)

    def changeColor(self):

        self.ui.Equipment1.setStyleSheet("Background: green")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    sys.exit(app.exec_())