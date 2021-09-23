import sys
import _thread as thread
import threading
from time import sleep
from PyQt5 import QtWidgets
from GAS import GAS_class
from Mattias_GUI import Ui_Sim
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class GUI_setup(QtWidgets.QMainWindow, threading.Thread):
    def __init__(self, g1, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.g1 = g1
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.ui = Ui_Sim()
        self.ui.setupUi(self)
        self.ui.addBot.clicked.connect(self.addABot)
        self.ui.removeBot.clicked.connect(self.removeABot)
        self.ui.amountBotsSlider.valueChanged.connect(self.botSlider)
        self.ui.amountBotsSlider_2.valueChanged.connect(self.mutationRate)

    def showUI(self):
        self.show()

    def graph(self, x, y):
        self.graphWidget.plot(x,y)

    def mutationRate(self):
        self.g1.params.mutation_rate = self.ui.amountBotsSlider_2.value()

    def botSlider(self):
        slider_bots = self.ui.amountBotsSlider.value()
        self.g1.params.min_bots = slider_bots
        self.ui.showAmountOfBots.setText(str(slider_bots))


    def addABot(self):
        self.g1.params.min_bots += 1
        self.ui.showAmountOfBots.setText(str(self.g1.params.min_bots))
        self.ui.amountBotsSlider.setValue(self.g1.params.min_bots)

    def removeABot(self):
        self.g1.params.min_bots -= 1
        self.ui.showAmountOfBots.setText(str(self.g1.params.min_bots))
        self.ui.amountBotsSlider.setValue(self.g1.params.min_bots)


