# Form implementation generated from reading ui file 'MainWindow1.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_app_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_app_message.setText("")
        self.label_app_message.setObjectName("label_app_message")
        self.gridLayout.addWidget(self.label_app_message, 0, 0, 1, 7)
        self.pushButton_refresh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_refresh.setMinimumSize(QtCore.QSize(41, 31))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout.addWidget(self.pushButton_refresh, 1, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add.setMinimumSize(QtCore.QSize(50, 31))
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 1, 1, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_search.setMinimumSize(QtCore.QSize(40, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 3)
        self.pushButton_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(111, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        self.pushButton_b1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_b1.setMinimumSize(QtCore.QSize(20, 10))
        self.pushButton_b1.setObjectName("pushButton_b1")
        self.gridLayout.addWidget(self.pushButton_b1, 2, 4, 1, 1)
        self.pushButton_b2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_b2.setMinimumSize(QtCore.QSize(20, 10))
        self.pushButton_b2.setObjectName("pushButton_b2")
        self.gridLayout.addWidget(self.pushButton_b2, 2, 5, 1, 1)
        self.pushButton_b3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_b3.setMinimumSize(QtCore.QSize(20, 10))
        self.pushButton_b3.setObjectName("pushButton_b3")
        self.gridLayout.addWidget(self.pushButton_b3, 2, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgb(254, 255, 245);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_refresh.setText(_translate("MainWindow", "обновить"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "column:text"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Фильтровать по зданию :"))
        self.pushButton_b1.setText(_translate("MainWindow", "B1"))
        self.pushButton_b2.setText(_translate("MainWindow", "B2"))
        self.pushButton_b3.setText(_translate("MainWindow", "B3"))
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
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "bldg"))
