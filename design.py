import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem, QDialog
from PyQt6.QtWidgets import QMessageBox

import main_window
import dialog_window
from PyQt6 import QtWidgets

from classes import Printer

LIST_OF_CELL_CHANGES = []


class DialogDesign(QDialog, dialog_window.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_send.clicked.connect(self.send_data)

    def send_data(self):
        p_add = Printer('printers.db')
        p_add.add_printer(self.lineEdit_model.text(), self.lineEdit_cartridge.text(),
                          self.lineEdit_drum.text(), self.lineEdit_ip.text(), self.lineEdit_mac.text(),
                          self.lineEdit_place.text())
        self.close()


class PrinterDesign(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setColumnWidth(0, 10)

        self.import_data_to_table()
        self.pushButton_add.clicked.connect(self.dialog_window)
        self.tableWidget.cellChanged.connect(self.get_data_from_cell_to_change)
        self.pushButton_save.clicked.connect(self.send_cell_data_to_change)

    def dialog_window(self):
        dlg = DialogDesign()
        dlg.exec()

    def cell_was_clicked(self):
        # Функция - получить ID
        try:
            current_row = self.tableWidget.currentRow()
            cell_id = self.tableWidget.item(current_row, 0).text()
            return cell_id
        except Exception as s:
            pass

    def cur_row_and_cur_col(self):
        return self.tableWidget.currentRow(), self.tableWidget.currentColumn()

    def import_data_to_table(self):
        s = Printer('printers.db')
        result = s.show_printers()

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def get_data_from_cell_to_change(self):
        try:
            global LIST_OF_CELL_CHANGES
            cell_id = self.cell_was_clicked()
            current_row = self.cur_row_and_cur_col()[0]
            current_column = self.cur_row_and_cur_col()[1]
            column_name = self.tableWidget.horizontalHeaderItem(current_column).text()

            cell_value = self.tableWidget.item(current_row, current_column).text()

            font = QFont()
            font.setItalic(True)
            self.tableWidget.item(current_row, current_column).setFont(font)
            LIST_OF_CELL_CHANGES.append((column_name, cell_value, cell_id))

            # print(DICT_OF_CELL_CHANGES)
            # print(len(DICT_OF_CELL_CHANGES))

        except Exception as s:
            print(s)

    def send_cell_data_to_change(self):
        try:
            p = Printer('printers.db')
            p.edit_printers_column(LIST_OF_CELL_CHANGES)
            LIST_OF_CELL_CHANGES.clear()
            QMessageBox.about(self, 'Change item', 'Success')

        except Exception as s:
            print(s)
