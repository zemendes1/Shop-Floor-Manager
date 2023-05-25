# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignInterfaceErp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from ERP import MPS
import sys
from MES import db

from MES import db_to_interface as db_to_interface



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 1301, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 161, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 390, 881, 291))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(920, 390, 131, 31))
        self.label_6.setObjectName("label_6")
        self.CurrentDate = QtWidgets.QLabel(self.centralwidget)
        self.CurrentDate.setGeometry(QtCore.QRect(920, 430, 55, 16))
        self.CurrentDate.setObjectName("CurrentDate")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(920, 460, 131, 31))
        self.label_7.setObjectName("label_7")
        self.TotalCost = QtWidgets.QLabel(self.centralwidget)
        self.TotalCost.setGeometry(QtCore.QRect(920, 500, 55, 16))
        self.TotalCost.setObjectName("TotalCost")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1359, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 125)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 125)
        self.tableWidget.setColumnWidth(4, 110)
        self.tableWidget.setColumnWidth(5, 110)
        self.tableWidget.setColumnWidth(6, 110)
        self.tableWidget.setColumnWidth(7, 110)
        self.tableWidget.setColumnWidth(8, 120)
        self.tableWidget.setColumnWidth(9, 125)
        self.tableWidget.setColumnWidth(10, 125)

        self.tableWidget_2.setColumnWidth(0, 70)
        self.tableWidget_2.setColumnWidth(1, 185)
        self.tableWidget_2.setColumnWidth(2, 245)
        self.tableWidget_2.setColumnWidth(3, 80)
        self.tableWidget_2.setColumnWidth(4, 80)
        self.tableWidget_2.setColumnWidth(5, 100)
        self.tableWidget_2.setColumnWidth(6, 100)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Erp Interface"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Table: Orders</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Client"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "OrderNumber"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "WorkPiece"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DueDate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Late_Penalty"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Early_Penalty"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Path"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Custo"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Table: Daily Plan</span></p></body></html>"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Purchase_orders"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delivery_orders"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P1_toBuy"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "P2_toBuy"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "P1_Arriving"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "P2_Arriving"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Current Date:</span></p></body></html>"))
        self.CurrentDate.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Custo Total:</span></p></body></html>"))
        self.TotalCost.setText(_translate("MainWindow", "TextLabel"))

        self.loaddata()
        self.SetDATA()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateMode)
        self.timer.start(5000)

    def updateMode(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.loaddata()
        self.SetDATA()

    def loaddata(self):
        testeOrder = db_to_interface.orders(None)
        testeDailyPlan = db_to_interface.daily_plan(None)
        rowOrder = 0
        rowDailyPlan = 0
        CustoAux=0

        self.tableWidget.setRowCount(len(testeOrder))
        self.tableWidget_2.setRowCount(len(testeDailyPlan))

        for order in testeOrder:
            self.tableWidget.setItem(rowOrder, 0, QtWidgets.QTableWidgetItem(order["id"]))
            self.tableWidget.setItem(rowOrder, 1, QtWidgets.QTableWidgetItem(order["Client"]))
            self.tableWidget.setItem(rowOrder, 2, QtWidgets.QTableWidgetItem(order["OrderNumber"]))
            self.tableWidget.setItem(rowOrder, 3, QtWidgets.QTableWidgetItem(order["WorkPiece"]))
            self.tableWidget.setItem(rowOrder, 4, QtWidgets.QTableWidgetItem(order["Quantity"]))
            self.tableWidget.setItem(rowOrder, 5, QtWidgets.QTableWidgetItem(order["DueDate"]))
            self.tableWidget.setItem(rowOrder, 6, QtWidgets.QTableWidgetItem(order["Late_Penalty"]))
            self.tableWidget.setItem(rowOrder, 7, QtWidgets.QTableWidgetItem(order["Early_Penalty"]))
            self.tableWidget.setItem(rowOrder, 8, QtWidgets.QTableWidgetItem(order["path"]))
            self.tableWidget.setItem(rowOrder, 9, QtWidgets.QTableWidgetItem(order["status"]))
            self.tableWidget.setItem(rowOrder, 10, QtWidgets.QTableWidgetItem(order["custo"]))
            cust = int(order["custo"])
            CustoAux = CustoAux + cust
            rowOrder = rowOrder + 1
        CustoStr = str(CustoAux)
        self.TotalCost.setText(CustoStr)

        for DailyPlan in testeDailyPlan:
            self.tableWidget_2.setItem(rowDailyPlan, 0, QtWidgets.QTableWidgetItem(DailyPlan["date"]))
            self.tableWidget_2.setItem(rowDailyPlan, 1, QtWidgets.QTableWidgetItem(DailyPlan["Working_orders"]))
            self.tableWidget_2.setItem(rowDailyPlan, 2, QtWidgets.QTableWidgetItem(DailyPlan["Delivery_orders"]))
            self.tableWidget_2.setItem(rowDailyPlan, 3, QtWidgets.QTableWidgetItem(DailyPlan["P1_toBuy"]))
            self.tableWidget_2.setItem(rowDailyPlan, 4, QtWidgets.QTableWidgetItem(DailyPlan["P2_toBuy"]))
            self.tableWidget_2.setItem(rowDailyPlan, 5, QtWidgets.QTableWidgetItem(DailyPlan["P1_Arriving "]))
            self.tableWidget_2.setItem(rowDailyPlan, 6, QtWidgets.QTableWidgetItem(DailyPlan["P2_Arriving "]))
            rowDailyPlan = rowDailyPlan + 1

    def SetDATA(self):
        day = db.get_day()
        DayString = str(day)
        self.CurrentDate.setText(DayString)



def setup_interface():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
