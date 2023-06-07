# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 761, 461))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(120, 20, 111, 31))
        self.pushButton_add.setMinimumSize(QtCore.QSize(50, 31))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_refresh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.pushButton_refresh.setMinimumSize(QtCore.QSize(41, 31))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_b1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_b1.setGeometry(QtCore.QRect(590, 60, 31, 21))
        self.pushButton_b1.setMinimumSize(QtCore.QSize(20, 10))
        self.pushButton_b1.setObjectName("pushButton_b1")
        self.pushButton_search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(380, 20, 51, 31))
        self.pushButton_search.setMinimumSize(QtCore.QSize(40, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 20, 221, 31))
        self.lineEdit.setMinimumSize(QtCore.QSize(221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(670, 20, 111, 31))
        self.pushButton_save.setMinimumSize(QtCore.QSize(111, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_b2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_b2.setGeometry(QtCore.QRect(630, 60, 31, 21))
        self.pushButton_b2.setMinimumSize(QtCore.QSize(20, 10))
        self.pushButton_b2.setObjectName("pushButton_b2")
        self.pushButton_b3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_b3.setGeometry(QtCore.QRect(670, 60, 31, 21))
        self.pushButton_b3.setMinimumSize(QtCore.QSize(20, 10))
        self.pushButton_b3.setObjectName("pushButton_b3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 60, 141, 20))
        self.label.setObjectName("label")
        self.label_app_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_app_message.setGeometry(QtCore.QRect(30, 0, 761, 16))
        self.label_app_message.setText("")
        self.label_app_message.setObjectName("label_app_message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "model"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "cartridge_model"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "drum_cartridge"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ip_address"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "mac"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "location"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButton_refresh.setText(_translate("MainWindow", "обновить"))
        self.pushButton_b1.setText(_translate("MainWindow", "B1"))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "column:text"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_b2.setText(_translate("MainWindow", "B2"))
        self.pushButton_b3.setText(_translate("MainWindow", "B3"))
        self.label.setText(_translate("MainWindow", "Фильтровать по зданию :"))
