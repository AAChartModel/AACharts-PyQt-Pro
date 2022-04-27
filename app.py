import random
import sys

# from PyQt6.QtCore import QUrl
# from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QMessageBox
# from PySide6 import QtWebEngineWidgets, QtWidgets, QtCore
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
# import webview
import wx
from wx.html2 import WebView

# from PyQt6.QtWebEngineWidgets import QWebEnginePage
# from PyQt6.QtWebEngineWidgets import QWebEngineView

import simplejson
import json


import jsonpickle

from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aachartcreator.AAChartView import AAChartView
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aachartcreator.PYChartView import PYChartView
from aacharts.aaenum.AAEnum import AAChartType, AAChartAnimationType
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aatool.AAJsonConverter import AAJsonConverter
from demo.MainTreeWidget import MainTreeWidget


def main():

    app = wx.App()
    app.MainLoop()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainTreeWidget()
    widget.resize(300, 1200)
    widget.show()

    sys.exit(app.exec())
