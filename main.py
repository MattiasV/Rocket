import sys

from eBoiler import Ui_eBoiler

from PyQt5 import QtWidgets

class GUI_setup(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_eBoiler()
        self.ui.setupUi(self)

        self.ui.TutorialPushButton.clicked.connect(self.tutorial)
        self.ui.Equipment1.colorCount(self)


    def tutorial(self):
        self.statusBar().showMessage('Pressed on the tutorial button', 2000)
        QtWidgets.QMessageBox.information(self,'Succes', 'Tutorial messagebox opened')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    sys.exit(app.exec_())