# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from MES.pythonProject import db_to_interface


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1305, 746)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1331, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.Orders = QtWidgets.QWidget()
        self.Orders.setObjectName("Orders")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Orders)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 360, 1121, 291))
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
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
        self.label_2 = QtWidgets.QLabel(self.Orders)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 161, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.Orders)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 1121, 291))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
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
        self.label = QtWidgets.QLabel(self.Orders)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.Orders, "")
        self.Facilities = QtWidgets.QWidget()
        self.Facilities.setObjectName("Facilities")
        self.label_3 = QtWidgets.QLabel(self.Facilities)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.label_3.setObjectName("label_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.Facilities)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 40, 941, 291))
        self.tableWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(12)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        self.label_4 = QtWidgets.QLabel(self.Facilities)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 151, 31))
        self.label_4.setObjectName("label_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.Facilities)
        self.tableWidget_4.setGeometry(QtCore.QRect(20, 360, 941, 321))
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(10)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        self.tabWidget.addTab(self.Facilities, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 120)
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 120)

        self.tableWidget_2.setColumnWidth(0, 70)
        self.tableWidget_2.setColumnWidth(1, 400)
        self.tableWidget_2.setColumnWidth(2, 400)
        self.tableWidget_2.setColumnWidth(3, 100)
        self.tableWidget_2.setColumnWidth(4, 100)

        self.tableWidget_3.setColumnWidth(0, 70)
        self.tableWidget_3.setColumnWidth(1, 70)
        self.tableWidget_3.setColumnWidth(2, 70)
        self.tableWidget_3.setColumnWidth(3, 70)
        self.tableWidget_3.setColumnWidth(4, 70)
        self.tableWidget_3.setColumnWidth(5, 70)
        self.tableWidget_3.setColumnWidth(6, 70)
        self.tableWidget_3.setColumnWidth(7, 70)
        self.tableWidget_3.setColumnWidth(8, 70)
        self.tableWidget_3.setColumnWidth(9, 70)
        self.tableWidget_3.setColumnWidth(10, 120)
        self.tableWidget_3.setColumnWidth(11, 90)

        self.tableWidget_4.setColumnWidth(0, 60)
        self.tableWidget_4.setColumnWidth(1, 70)
        self.tableWidget_4.setColumnWidth(2, 70)
        self.tableWidget_4.setColumnWidth(3, 70)
        self.tableWidget_4.setColumnWidth(4, 70)
        self.tableWidget_4.setColumnWidth(5, 70)
        self.tableWidget_4.setColumnWidth(6, 70)
        self.tableWidget_4.setColumnWidth(7, 70)
        self.tableWidget_4.setColumnWidth(8, 70)
        self.tableWidget_4.setColumnWidth(9, 70)
        self.tableWidget_3.setColumnWidth(10, 90)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Table: Daily Plan</span></p></body></html>"))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Table: Orders</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Orders), _translate("MainWindow", "Orders and Daily Plan Tables"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Table: Facilities</span></p></body></html>"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "num"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "P1"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P2"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P3"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "P4"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "P5"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "P6"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "P7"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "P8"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "P9"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "WorkTime"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Total"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Table: Docks</span></p><p><br/></p></body></html>"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "num"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "P2"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P3"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P4"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "P5"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "P6"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "P7"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "P8"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "P9"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Total"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Facilities), _translate("MainWindow", "Facilities and Docks Tables"))


        self.loaddata()


# funcao que faz refresh periodicamente
# verifica se a base de dados tem algum id novo em cada uma das tabelas
# fazer um loaddata para cada uma das tabelas para poder controlar caso so houver atualizações
# ou apagar as tabelas todas e dar refresh sempre periodicamente
    def loaddata(self):
        testeOrder = db_to_interface.orders(None)
        testeDailyPlan = db_to_interface.daily_plan(None)
        testeFacilities = db_to_interface.facilities(None)
        testeDocks = db_to_interface.dock(None)

        rowOrder = 0
        rowDailyPlan = 0
        rowFacilities = 0
        rowDocks = 0
        self.tableWidget_3.setRowCount((len(testeFacilities)))
        self.tableWidget_4.setRowCount((len(testeDocks)))
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
            rowOrder = rowOrder + 1

        for DailyPlan in testeDailyPlan:
            self.tableWidget_2.setItem(rowDailyPlan, 0, QtWidgets.QTableWidgetItem(DailyPlan["date"]))
            self.tableWidget_2.setItem(rowDailyPlan, 1, QtWidgets.QTableWidgetItem(DailyPlan["Purchase_orders"]))
            self.tableWidget_2.setItem(rowDailyPlan, 2, QtWidgets.QTableWidgetItem(DailyPlan["Delivery_orders"]))
            self.tableWidget_2.setItem(rowDailyPlan, 3, QtWidgets.QTableWidgetItem(DailyPlan["P1_toBuy"]))
            self.tableWidget_2.setItem(rowDailyPlan, 4, QtWidgets.QTableWidgetItem(DailyPlan["P2_toBuy"]))
            rowDailyPlan = rowDailyPlan + 1

        for Facilities in testeFacilities:
            self.tableWidget_3.setItem(rowFacilities, 0, QtWidgets.QTableWidgetItem(Facilities["num"]))
            self.tableWidget_3.setItem(rowFacilities, 1, QtWidgets.QTableWidgetItem(Facilities["P1"]))
            self.tableWidget_3.setItem(rowFacilities, 2, QtWidgets.QTableWidgetItem(Facilities["P2"]))
            self.tableWidget_3.setItem(rowFacilities, 3, QtWidgets.QTableWidgetItem(Facilities["P3"]))
            self.tableWidget_3.setItem(rowFacilities, 4, QtWidgets.QTableWidgetItem(Facilities["P4"]))
            self.tableWidget_3.setItem(rowFacilities, 5, QtWidgets.QTableWidgetItem(Facilities["P5"]))
            self.tableWidget_3.setItem(rowFacilities, 6, QtWidgets.QTableWidgetItem(Facilities["P6"]))
            self.tableWidget_3.setItem(rowFacilities, 7, QtWidgets.QTableWidgetItem(Facilities["P7"]))
            self.tableWidget_3.setItem(rowFacilities, 8, QtWidgets.QTableWidgetItem(Facilities["P8"]))
            self.tableWidget_3.setItem(rowFacilities, 9, QtWidgets.QTableWidgetItem(Facilities["P9"]))
            self.tableWidget_3.setItem(rowFacilities, 10, QtWidgets.QTableWidgetItem(Facilities["workTime"]))
            rowFacilities = rowFacilities + 1

        for Docks in testeDocks:
            self.tableWidget_4.setItem(rowDocks, 0, QtWidgets.QTableWidgetItem(Docks["num"]))
            self.tableWidget_4.setItem(rowDocks, 1, QtWidgets.QTableWidgetItem(Docks["P1"]))
            self.tableWidget_4.setItem(rowDocks, 2, QtWidgets.QTableWidgetItem(Docks["P2"]))
            self.tableWidget_4.setItem(rowDocks, 3, QtWidgets.QTableWidgetItem(Docks["P3"]))
            self.tableWidget_4.setItem(rowDocks, 4, QtWidgets.QTableWidgetItem(Docks["P4"]))
            self.tableWidget_4.setItem(rowDocks, 5, QtWidgets.QTableWidgetItem(Docks["P5"]))
            self.tableWidget_4.setItem(rowDocks, 6, QtWidgets.QTableWidgetItem(Docks["P6"]))
            self.tableWidget_4.setItem(rowDocks, 7, QtWidgets.QTableWidgetItem(Docks["P7"]))
            self.tableWidget_4.setItem(rowDocks, 8, QtWidgets.QTableWidgetItem(Docks["P8"]))
            self.tableWidget_4.setItem(rowDocks, 9, QtWidgets.QTableWidgetItem(Docks["P9"]))
            self.tableWidget_4.setItem(rowDocks, 10, QtWidgets.QTableWidgetItem(Docks["Total"]))
            rowDocks = rowDocks + 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
