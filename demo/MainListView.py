from PySide6 import QtWidgets, QtCore

from aacharts.aachartcreator.PYChartView import PYChartView
from demo.AAOptionsProComposer import AAOptionsProComposer
from demo.MainTreeWidget import CustomCollectionView


class FirstView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        self.pushButton = QtWidgets.QPushButton("Go to Second View")
        layout.addWidget(self.pushButton)

class SecondView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("This is the second view")
        layout.addWidget(self.label)

        self.gridLayout = QtWidgets.QGridLayout()
        for i in range(3):
            for j in range(3):
                button = QtWidgets.QPushButton(f"Button {i*3 + j + 1}")
                chartView = PYChartView()
                testChartModel = AAOptionsProComposer.lollipopChart()
                self.gridLayout.addWidget(chartView, i, j)
                chartView.aa_drawChartWithChartOptions(testChartModel)


        layout.addLayout(self.gridLayout)

        self.backButton = QtWidgets.QPushButton("Back to First View")
        layout.addWidget(self.backButton)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.firstView = FirstView()
        self.secondView = CustomCollectionView()

        self.stackedWidget.addWidget(self.firstView)
        self.stackedWidget.addWidget(self.secondView)

        self.firstView.pushButton.clicked.connect(self.showSecondView)
        self.secondView.backButton.clicked.connect(self.showFirstView)

    def showSecondView(self):
        self.stackedWidget.setCurrentWidget(self.secondView)

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