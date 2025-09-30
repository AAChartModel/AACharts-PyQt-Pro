from PySide6 import QtWidgets, QtCore

from aacharts.aachartcreator.PYChartView import PYChartView
from demo.AAOptionsProComposer import AAOptionsProComposer
from demo.MainTreeWidget import MainTreeWidget
from demo.OfficialChartSampleView import OfficialChartSampleView


class FirstView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        self.pushButton1 = QtWidgets.QPushButton("Go to official chart sample view")
        self.pushButton2 = QtWidgets.QPushButton("Go to Tree View")
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.firstView = FirstView()
        self.officialChartSampleView = OfficialChartSampleView()
        self.mainTreeView = MainTreeWidget()

        self.stackedWidget.addWidget(self.firstView)
        self.stackedWidget.addWidget(self.officialChartSampleView)
        self.stackedWidget.addWidget(self.mainTreeView)

        self.firstView.pushButton1.clicked.connect(self.showOfficialChartSampleView)
        self.firstView.pushButton2.clicked.connect(self.showTreeView)
        self.officialChartSampleView.backButton.clicked.connect(self.showFirstView)
        self.mainTreeView.backButton.clicked.connect(self.showFirstView)

    def showOfficialChartSampleView(self):
        self.stackedWidget.setCurrentWidget(self.officialChartSampleView)

    def showTreeView(self):
        self.stackedWidget.setCurrentWidget(self.mainTreeView)

    def showFirstView(self):
        self.stackedWidget.setCurrentWidget(self.firstView)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     mainWindow = MainWindow()
#     mainWindow.resize(400, 300)
#     mainWindow.show()
#
#     app.exec()