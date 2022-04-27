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


class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(1024, 768))
        web_view = WebView.New(self)
        web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        web_view.RunScript("alert('测试运行 JS')")
        web_view.RunScript("document.write('Hello from wx.Widgets!')")
        web_view.RunScript("document.write('--------------这个世上本没有路, 走的人多了,也便成了路Hello from wx.Widgets!')")


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(1300, 450))

        self.InitUI()

    def InitUI(self):

        self.optionsJson = ""

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, 'New', size=(90, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, 'Rename', size=(90, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, 'Delete', size=(90, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, 'Clear', size=(90, 30))

        self.web_view = AAChartView(btnPanel, size=(900,600))

        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        # self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)
        vbox.Add(self.web_view, 0, wx.TOP, 5)


        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 1, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('wx.ListBox')


        # 添加事件处理
        self.Bind(wx.EVT_LISTBOX, self.on_choice, self.listbox)

        self.Centre()

    def on_choice(self, event):
        listbox = event.GetEventObject()
        print("选择{0}".format(listbox.GetSelections()))
        selectedIndex = listbox.GetSelections()[0]
        testChartModel = self.chartJSFuncOptionsConfigurationWithSelectedIndex(selectedIndex)
        # testChartModel2 = self.chartConfigurationWithSelectedIndex(listbox.GetSelections())

        self.web_view.aa_drawChartWithChartOptions(testChartModel)
        # self.aa_drawChartWithChartModel(testChartModel)


def main():

    app = wx.App()
    ex = Example(None, "测试标题")

    ex.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainTreeWidget()
    widget.resize(300, 1200)
    widget.show()

    sys.exit(app.exec())
