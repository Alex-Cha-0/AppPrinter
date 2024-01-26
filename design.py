import asyncio
import threading
from datetime import datetime

from PyQt6.QtCore import QSettings, QThread, pyqtSignal, QObject
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTableWidgetItem, QDialog
from PyQt6.QtWidgets import QMessageBox

import dialog_send_repair
import main_window
import dialog_window
from PyQt6 import QtWidgets

from classes import *
import v1_count_of_pages

LIST_OF_CELL_CHANGES = []


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    max_value = 0

    def run(self):
        p = Printer()
        printers = p.show_printers()
        current_value = 0
        self.max_value = len(printers) - 1
        for printer in printers:
            printer_id = printer[0]
            ip = printer[6]

            if ip:

                p.add_pages_printed(printer_id, asyncio.run(v1_count_of_pages.run(ip, oids=v1_count_of_pages.oid_s)))
                self.progress.emit(current_value)
                current_value += 1
            else:
                self.progress.emit(current_value)
                current_value += 1
        self.finished.emit()


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


class DialogSendRepair(QDialog, dialog_send_repair.Ui_Dialog_Add_Repair):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_sendrepair.clicked.connect(self.send_data_repair)
        self.label_printer_id.setVisible(False)
        self.lineEdit_printer_id.setVisible(False)

    def send_data_repair(self):
        try:
            p = Printer()
            p.add_info(datetime.now(), int(self.lineEdit_count_pages.text()), self.textEdit_comment.toPlainText(),
                       int(self.lineEdit_printer_id.text()))

            self.close()
        except Exception as s:
            print(s)


class PrinterDesign(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.t1 = threading.Thread(target=self.get_count_pages)
        self.btn_dell = None
        self.setupUi(self)
        self.settings = QSettings('ap_printer', 'Ui_MainWindow')
        # Кол-во колонок в таблице
        self.count_column = self.tableWidget.horizontalHeader().count()

        self.load_setting()
        #  Visible objects
        self.tableWidget.setColumnHidden(0, True)
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)

        self.import_data_to_table()
        # self.column_to_contex()
        self.get_column_name()

        self.pushButton_add.clicked.connect(self.dialog_window)
        self.pushButton_addrepair.setEnabled(False)
        self.pushButton_history.setVisible(False)
        self.pushButton_addrepair.clicked.connect(self.dialog_send_repair)
        self.tableWidget.cellChanged.connect(self.get_data_from_cell_to_change)
        self.tableWidget.clicked.connect(self.true_history_repair)

        self.pushButton_save.clicked.connect(self.send_cell_data_to_change)
        self.pushButton_refresh.clicked.connect(self.reload)
        self.pushButton_b1.clicked.connect(lambda: self.import_data_to_table_by_buldings('B1'))
        self.pushButton_b2.clicked.connect(lambda: self.import_data_to_table_by_buldings('B2'))
        self.pushButton_b3.clicked.connect(lambda: self.import_data_to_table_by_buldings('B3'))
        self.pushButton_search.clicked.connect(self.get_search_printer)
        self.pushButton_history.clicked.connect(self.show_info)
        self.lineEdit.returnPressed.connect(self.get_search_printer)

        self.comboBox.activated.connect(self.lineEdit_focus)



        self.pushButton_count.clicked.connect(self.task_get_num_of_printed_page)


    def lineEdit_focus(self):
        self.lineEdit.clear()
        self.lineEdit.setFocus()
    def task_get_num_of_printed_page(self):
        #  QThread()
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.progressBar.setVisible(True)
        # self.max_value = self.worker.max_value
        # self.progressBar.setMaximum(self.max_value)
        self.worker.progress.connect(self.update_progress)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Step 6: Start the thread
        self.thread.start()
        self.pushButton_count.setEnabled(False)
        # Final resets
        self.thread.finished.connect(lambda: self.pushButton_count.setEnabled(True))

    def update_progress(self, current_value):
        self.max_value = self.worker.max_value
        self.progressBar.setMaximum(self.max_value)
        self.progressBar.setValue(current_value)
        self.tableWidget.selectRow(current_value)
        self.reload()
        if self.progressBar.value() == self.max_value:
            self.progressBar.setVisible(False)
            self.progressBar.reset()

    # def get_count_pages(self):
    #     p = Printer()
    #     printers = p.show_printers()
    #     current_value = 0
    #     max_value = len(printers) - 1
    #     self.progressBar.setVisible(True)
    #     self.progressBar.setRange(current_value, max_value)
    #     for printer in printers:
    #         ip = printer[4]
    #         model = printer[1].split()[0]
    #         if ip:
    #             asyncio.run(v1_count_of_pages.run(ip, model))
    #             self.progressBar.setValue(current_value)
    #             current_value += 1
    #         else:
    #             self.progressBar.setValue(current_value)
    #             current_value += 1
    #             pass
    #         if self.progressBar.value() == max_value:
    #             self.progressBar.setVisible(False)
    #             self.progressBar.reset()

    """Сохранение настроек"""

    def closeEvent(self, event):
        self.save_setting()
        event.accept()

    def save_setting(self):
        # self.settings.setValue('window size', self.size())
        # self.settings.setValue('window position', self.pos())
        self.settings.setValue('Geometry', self.saveGeometry())
        self.settings.setValue('WindowState', self.saveState())

        for i in range(self.count_column):
            self.settings.setValue(f'column {i}', self.tableWidget.columnWidth(i))

    def load_setting(self):
        geometry = self.settings.value('Geometry')
        if geometry:
            self.restoreGeometry(geometry)

        state = self.settings.value('WindowState')
        if state:
            self.restoreState(state)

        for i in range(self.count_column):
            self.tableWidget.setColumnWidth(i, self.settings.value(f'column {i}', 100))

    def column_to_contex(self):
        """
        Размер колонок по содержимому
        :return:
        """
        for i in range(4, 7):
            self.tableWidget.resizeColumnToContents(i)

    def dialog_window(self):
        """
        Показать диалог
        :return:
        """
        dlg = DialogDesign()
        dlg.finished.connect(self.reload)
        dlg.exec()

    def dialog_send_repair(self):
        """
        Показать диалог
        :return:
        """
        dlg = DialogSendRepair()
        dlg.lineEdit_printer_id.setText(self.cell_was_clicked())
        dlg.finished.connect(self.reload)
        dlg.exec()

    def reload(self):
        """
        Перезагрузка главного окна
        :return:
        """
        self.label_app_message.setText('Обновлено')
        self.import_data_to_table()

    def import_data(self, result):
        """
        Загрузка данных из базы
        :param result:
        :return:
        """

        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(len(result))
        # for row, form in enumerate(result):
        #     self.tableWidget.insertRow(row)
        #     # Button delete
        #     self.btn_dell = QtWidgets.QPushButton(f"❌")
        #     self.btn_dell.setStyleSheet(
        #         "QPushButton:hover {\n"
        #         "    background-color: rgba(42, 127, 127, 40);\n"
        #         "    color: white;\n"
        #         "    border-radius:7px;\n"
        #         "}\n"
        #         "")
        #     self.btn_dell.setObjectName(f"pushButton_{form[0]}")
        #     self.btn_dell.clicked.connect(self.show_popup)
        #     self.tableWidget.setCellWidget(row, 9, self.btn_dell)
        #     # End Button delete
        #     for column, item in enumerate(form):
        #         # Items in colum 6 to upper
        #         if column == 6:
        #             item = str(item).upper()
        #         self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
        for i, (id, model, printed, repairs, cartridge_model, drum_cartridge, ip_address, network_id, mac, location,
                building) in enumerate(result):
            item_id = QTableWidgetItem(str(id))
            item_model = QTableWidgetItem(model)
            item_printed = QTableWidgetItem(str(printed))
            item_repairs = QTableWidgetItem(str(repairs))
            item_cartridge_model = QTableWidgetItem(cartridge_model)
            item_drum_cartridge = QTableWidgetItem(drum_cartridge)
            item_ip_address = QTableWidgetItem(ip_address)
            item_network_id = QTableWidgetItem(network_id)
            item_mac = QTableWidgetItem(str(mac).upper())
            item_location = QTableWidgetItem(location)
            item_building = QTableWidgetItem(building)
            # Button delete
            self.btn_dell = QtWidgets.QPushButton(f"❌")
            self.btn_dell.setStyleSheet(
                "QPushButton:hover {\n"
                "    background-color: rgba(42, 127, 127, 40);\n"
                "    color: white;\n"
                "    border-radius:7px;\n"
                "}\n"
                "")
            self.btn_dell.setObjectName(f"pushButton_{item_id}")
            self.btn_dell.clicked.connect(self.show_popup)
            self.tableWidget.setCellWidget(i, 11, self.btn_dell)
            # End Button delete
            self.tableWidget.setItem(i, 0, item_id)
            self.tableWidget.setItem(i, 1, item_model)
            self.tableWidget.setItem(i, 2, item_printed)
            self.tableWidget.setItem(i, 3, item_repairs)
            self.tableWidget.setItem(i, 4, item_cartridge_model)
            self.tableWidget.setItem(i, 5, item_drum_cartridge)
            self.tableWidget.setItem(i, 6, item_ip_address)
            self.tableWidget.setItem(i, 7, item_network_id)
            self.tableWidget.setItem(i, 8, item_mac)
            self.tableWidget.setItem(i, 9, item_location)
            self.tableWidget.setItem(i, 10, item_building)
            # self.tableWidget.setItem(i, 11, item_actions)
        self.tableWidget.setSortingEnabled(True)

    def cell_was_clicked(self):
        """
        Возвращает id стобца ID
        :return:
        """
        try:
            current_row = self.tableWidget.currentRow()
            cell_id = self.tableWidget.item(current_row, 0).text()
            self.pushButton_addrepair.setEnabled(True)
            self.label_app_message.setText(f'entry_id - {cell_id}')
            return cell_id
        except Exception as s:
            pass

    def cur_row_and_cur_col(self):
        """
        Возвращает int выбранной строки и
        колонки
        :return:
        """
        return self.tableWidget.currentRow(), self.tableWidget.currentColumn()

    def import_data_to_table(self):
        """
        Заполняет таблицу данными из базы
        :return:
        """
        try:
            s = Printer()
            result = s.show_printers()
            self.import_data(result)
        except Exception as s:
            print(s)

    def get_data_from_cell_to_change(self):
        """
        Получает ячейки для изменения и
        добаляет их в глобальную переменную
        LIST_OF_CELL_CHANGES
        :return:
        """
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
        """
        Получет ячейки из LIST_OF_CELL_CHANGES
        и отправляет в базу данных
        :return:
        """
        try:
            p = Printer()
            p.edit_printers_column(LIST_OF_CELL_CHANGES)
            self.label_app_message.setText(f"Обновлена ячейка")
            LIST_OF_CELL_CHANGES.clear()
            QMessageBox.about(self, 'Change item', 'Success')
            self.reload()

        except Exception as s:
            pass

    def import_data_to_table_by_buldings(self, building):
        """
        Фильтрует ячейки по зданиям
        :param building:
        :return:
        """
        try:
            s = Printer()
            result = s.show_printer_by_building(building)

            self.import_data(result)
            self.label_app_message.setText(f'Выбрано здание {building}')

        except Exception as s:
            pass

    # def get_text_from_search(self):
    #     """
    #     Получает текст поиска из
    #     lineEdit. Возвращает нужную колонку и
    #     текст для поиска
    #     :return:
    #     """
    #     result = []
    #
    #     def find_colon_index(txt):
    #         return txt.find(':')
    #
    #     text = self.lineEdit.text()
    #
    #     column = text[:find_colon_index(text)]
    #     result.append(column)
    #     string_ = text[find_colon_index(text) + 1:]
    #     result.append(string_)
    #     return result

    def get_search_printer(self):
        """
        Получет нужную колонку и текст из
        get_text_from_search и показывает результат
        поиска
        :return:
        """
        try:
            # col = self.get_text_from_search()[0]
            # string_ = self.get_text_from_search()[1]
            col = self.comboBox.currentText()
            string_ = self.lineEdit.text()

            p = Printer()
            result = p.search_printer(col, string_)

            self.import_data(result)
            self.label_app_message.setText('Результат поиска')

        except Exception as s:
            pass

    # def get_html_content(self):
    #     p = Printer()
    #     result = p.load_html_content(self.cell_was_clicked())
    #     self.textBrowser.setHtml(result[0][0])

    def get_column_name(self):
        for x in range(1, self.tableWidget.columnCount()):
            self.comboBox.addItem(self.tableWidget.horizontalHeaderItem(x).text())

    # def set_line_edit_column_to_search(self):
    #     self.lineEdit.setText(self.comboBox.currentText() + ':')

    def show_info(self):
        id = self.cell_was_clicked()
        p = Printer()
        current_row = self.tableWidget.currentRow()
        model = self.tableWidget.item(current_row, 1).text()
        location = self.tableWidget.item(current_row, 9).text()
        try:
            result = p.show_info(id)
            if result:
                self.tabWidget.setCurrentIndex(1)
                self.label_infotab.setText(model + ' ' + location)

                self.tableWidget_info.setSortingEnabled(False)
                self.tableWidget_info.setRowCount(0)
                for row, form in enumerate(result):
                    self.tableWidget_info.insertRow(row)
                    for column, item in enumerate(form):
                        self.tableWidget_info.setItem(row, column, QTableWidgetItem(str(item)))
                self.tableWidget_info.setSortingEnabled(True)

        except Exception as e:
            print(e)

    def true_history_repair(self):
        self.tableWidget_info.clearContents()
        id = self.cell_was_clicked()
        p = Printer()
        result = p.show_info(id)
        if result:
            self.pushButton_history.setVisible(True)
            self.pushButton_history.setStyleSheet("\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgba(42, 127, 127, 40);\n"
                                                  "    color: black;\n"
                                                  "    border-radius:7px;\n"
                                                  "}\n"
                                                  "")
        else:
            self.pushButton_history.setVisible(False)

    def show_popup(self):
        try:
            id = self.cell_was_clicked()
            current_row = self.tableWidget.currentRow()
            model = self.tableWidget.item(current_row, 1).text()
            # result = p.delete_row(id)
            msg = QMessageBox(text="Удалить запись?", parent=self)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok |
                                   QMessageBox.StandardButton.Cancel)
            msg.setInformativeText(f'id({id}) {model}')
            msg.buttonClicked.connect(self.output)
            ret = msg.exec()
        except Exception as s:
            print(s)

    def output(self, button):
        try:
            id = self.cell_was_clicked()
            p = Printer()
            if button.text() == 'OK':
                self.label_app_message.setText(f"Удалена запись с id = {id}")
                p.delete_row(id)
                self.reload()
        except Exception as s:
            print(s)
