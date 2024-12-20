import sys
from PySide6 import QtWidgets

from demo.MainListView import MainWindow
# import wx
from demo.MainTreeWidget import MainTreeWidget

def main():
    # app = wx.App()
    app.MainLoop()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     widget = MainTreeWidget()
#     widget.resize(300, 1200)
#     widget.show()
#
#     sys.exit(app.exec())





if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(300, 1200)
    widget.show()

    sys.exit(app.exec())