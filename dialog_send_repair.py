
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Add_Repair(object):
    def setupUi(self, Dialog_Add_Repair):
        Dialog_Add_Repair.setObjectName("Dialog_Add_Repair")
        Dialog_Add_Repair.resize(543, 435)
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog_Add_Repair)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 501, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_sendrepair = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_sendrepair.setObjectName("pushButton_sendrepair")
        self.gridLayout.addWidget(self.pushButton_sendrepair, 3, 0, 1, 2)
        self.label_comment = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_comment.setObjectName("label_comment")
        self.gridLayout.addWidget(self.label_comment, 1, 0, 1, 1)
        self.lineEdit_count_pages = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_count_pages.setObjectName("lineEdit_count_pages")
        self.gridLayout.addWidget(self.lineEdit_count_pages, 0, 1, 1, 1)
        self.label_count_pages = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_count_pages.setObjectName("label_count_pages")
        self.gridLayout.addWidget(self.label_count_pages, 0, 0, 1, 1)
        self.textEdit_comment = QtWidgets.QTextEdit(parent=self.layoutWidget)
        self.textEdit_comment.setObjectName("textEdit_comment")
        self.gridLayout.addWidget(self.textEdit_comment, 1, 1, 1, 1)
        self.lineEdit_printer_id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_printer_id.setObjectName("lineEdit_printer_id")
        self.gridLayout.addWidget(self.lineEdit_printer_id, 2, 1, 1, 1)
        self.label_printer_id = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_printer_id.setObjectName("label_printer_id")
        self.gridLayout.addWidget(self.label_printer_id, 2, 0, 1, 1)

        self.retranslateUi(Dialog_Add_Repair)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Add_Repair)

    def retranslateUi(self, Dialog_Add_Repair):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Add_Repair.setWindowTitle(_translate("Dialog_Add_Repair", "Dialog"))
        self.pushButton_sendrepair.setText(_translate("Dialog_Add_Repair", "Записать"))
        self.label_comment.setText(_translate("Dialog_Add_Repair", "Коммент:"))
        self.label_count_pages.setText(_translate("Dialog_Add_Repair", "Напечатанные страницы:"))
        self.label_printer_id.setText(_translate("Dialog_Add_Repair", "принтер"))
