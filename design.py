import sys

from PyQt6.QtCore import pyqtSignal, QPropertyAnimation, QPoint
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem, QDialog, QMainWindow, QWidget
from PyQt6.QtWidgets import QMessageBox

import main_window
import dialog_window
from PyQt6 import QtWidgets

from classes import *

LIST_OF_CELL_CHANGES = []


class DialogDesign(QDialog, dialog_window.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_send.clicked.connect(self.send_data)

    def send_data(self):
        try:
            p_add = Printer()
            p_add.add_printer(self.lineEdit_model.text(), self.lineEdit_cartridge.text(),
                              self.lineEdit_drum.text(), self.lineEdit_ip.text(), self.lineEdit_mac.text(),
                              self.lineEdit_place.text(), self.lineEdit_place_building.text())
            self.close()
        except Exception as s:
            pass


class PrinterDesign(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setColumnHidden(0, True)
        self.import_data_to_table()
        self.pushButton_add.clicked.connect(self.dialog_window)
        self.tableWidget.cellChanged.connect(self.get_data_from_cell_to_change)
        self.pushButton_save.clicked.connect(self.send_cell_data_to_change)
        self.pushButton_refresh.clicked.connect(self.reload)
        self.pushButton_b1.clicked.connect(lambda: self.import_data_to_table_by_buldings('B1'))
        self.pushButton_b2.clicked.connect(lambda: self.import_data_to_table_by_buldings('B2'))
        self.pushButton_b3.clicked.connect(lambda: self.import_data_to_table_by_buldings('B3'))
        self.pushButton_search.clicked.connect(self.get_search_printer)

    def dialog_window(self):
        dlg = DialogDesign()
        dlg.finished.connect(self.reload)
        dlg.exec()

    def reload(self):
        # здесь вы можете выполнить любой код, который обновляет главное окно

        self.label_app_message.setText('updated')
        self.import_data_to_table()

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
        try:
            s = Printer()
            result = s.show_printers()
            self.tableWidget.setRowCount(0)
            for row, form in enumerate(result):
                self.tableWidget.insertRow(row)
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))

        except Exception as s:
            pass

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



        except Exception as s:
            pass

    def send_cell_data_to_change(self):
        try:
            p = Printer()
            p.edit_printers_column(LIST_OF_CELL_CHANGES)
            LIST_OF_CELL_CHANGES.clear()
            QMessageBox.about(self, 'Change item', 'Success')
            self.reload()

        except Exception as s:
            print(s)

    def import_data_to_table_by_buldings(self, building):
        try:
            s = Printer()
            result = s.show_printer_by_building(building)

            self.tableWidget.setRowCount(0)
            for row, form in enumerate(result):
                self.tableWidget.insertRow(row)
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))

        except Exception as s:
            print(s)

    def get_text_from_search(self):
        result = []

        def find_colon_index(txt):
            return txt.find(':')

        text = self.lineEdit.text()

        column = text[:find_colon_index(text)]
        result.append(column)
        string_ = text[find_colon_index(text) + 1:]
        result.append(string_)
        return result

    def get_search_printer(self):
        try:
            col = self.get_text_from_search()[0]
            string_ = self.get_text_from_search()[1]

            p = Printer()
            result = p.search_printer(col, string_)

            self.tableWidget.setRowCount(0)
            for row, form in enumerate(result):
                self.tableWidget.insertRow(row)
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))

        except Exception as s:
            pass
