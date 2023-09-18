# Form implementation generated from reading ui file '.\MainWindow3.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 600)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 10px solid grey;\n"
"     background: #32CC99;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {\n"
"    background-color: rgb(165, 165, 165);\n"
"     min-height: 20px;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {   \n"
"     height: 20px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::sub-line:vertical {  \n"
"     height: 20px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     \n"
"     width: 3px;\n"
"     height: 3px;\n"
"    \n"
" }\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    height: 15px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(165, 165, 165);\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"    \n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"   \n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QFrame(parent=self.centralwidget)
        self.menu.setStyleSheet("")
        self.menu.setObjectName("menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_refresh = QtWidgets.QPushButton(parent=self.menu)
        self.pushButton_refresh.setMinimumSize(QtCore.QSize(70, 31))
        self.pushButton_refresh.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    border-radius:7px;\n"
"    color: white;\n"
"}")
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.pushButton_add = QtWidgets.QPushButton(parent=self.menu)
        self.pushButton_add.setMinimumSize(QtCore.QSize(70, 31))
        self.pushButton_add.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    color: white;\n"
"    border-radius:7px;\n"
"}\n"
"\n"
"")
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.frame = QtWidgets.QFrame(parent=self.menu)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setStyleSheet("border-radius:7px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(193, 0, 108, 31))
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 31))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_search = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_search.setGeometry(QtCore.QRect(0, 0, 70, 31))
        self.pushButton_search.setMinimumSize(QtCore.QSize(70, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    color: white\n"
"}")
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(76, 0, 55, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setGeometry(QtCore.QRect(137, 0, 50, 31))
        self.comboBox.setMinimumSize(QtCore.QSize(50, 31))
        self.comboBox.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.comboBox.setStyleSheet("")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(parent=self.menu)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_b1 = QtWidgets.QPushButton(parent=self.menu)
        self.pushButton_b1.setMinimumSize(QtCore.QSize(35, 30))
        self.pushButton_b1.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    color: white\n"
"}")
        self.pushButton_b1.setObjectName("pushButton_b1")
        self.horizontalLayout.addWidget(self.pushButton_b1)
        self.pushButton_b2 = QtWidgets.QPushButton(parent=self.menu)
        self.pushButton_b2.setMinimumSize(QtCore.QSize(35, 30))
        self.pushButton_b2.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    color: white\n"
"}")
        self.pushButton_b2.setObjectName("pushButton_b2")
        self.horizontalLayout.addWidget(self.pushButton_b2)
        self.pushButton_b3 = QtWidgets.QPushButton(parent=self.menu)
        self.pushButton_b3.setMinimumSize(QtCore.QSize(35, 30))
        self.pushButton_b3.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    color: white\n"
"}")
        self.pushButton_b3.setObjectName("pushButton_b3")
        self.horizontalLayout.addWidget(self.pushButton_b3)
        self.pushButton_save = QtWidgets.QPushButton(parent=self.menu)
        self.pushButton_save.setMinimumSize(QtCore.QSize(111, 31))
        self.pushButton_save.setStyleSheet("QPushButton:hover {\n"
"   \n"
"    background-color: rgba(42, 127, 127, 40);\n"
"    color: white\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.verticalLayout.addWidget(self.menu)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgba(220, 210, 235, 20);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border:1px solid rgba(138, 138, 138, 40);\n"
"border-radius: 3px;")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked)
        self.tableWidget.setDragEnabled(True)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.label_app_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_app_message.setText("")
        self.label_app_message.setObjectName("label_app_message")
        self.gridLayout.addWidget(self.label_app_message, 0, 0, 1, 1)
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
        self.pushButton_add.setText(_translate("MainWindow", "добавить"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "column:text"))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))
        self.label_2.setText(_translate("MainWindow", "Столбец:"))
        self.label.setText(_translate("MainWindow", "Фильтровать по зданию :"))
        self.pushButton_b1.setText(_translate("MainWindow", "B1"))
        self.pushButton_b2.setText(_translate("MainWindow", "B2"))
        self.pushButton_b3.setText(_translate("MainWindow", "B3"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
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
        item.setText(_translate("MainWindow", "building"))
