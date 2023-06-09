import pymssql as mc
from cfg import *


class PrinterAbortAdd(Exception):
    def __str__(self):
        return f"Ошибка добавления принтера"


class PrinterAbortSearch(PrinterAbortAdd):
    def __str__(self):
        return f"Ошибка поиска принтера"


class Printer:
    def __init__(self):
        """
        Название базы данных
        :param db_name:
        """
        self.connection = mc.connect(server=SERVERMSSQL, user=USERMSSQL, password=PASSWORDMSSQL,
                                     database=DATABASEMSSQL)
        self.cursor = self.connection.cursor()

    def edit_printers_column(self, data):
        try:
            for i in range(len(data)):
                column_name = data[i][0]
                _data = data[i][1]
                cell = data[i][2]
                sql_update_query = f"""UPDATE ap_printers set {column_name} = '{_data}' where id = {cell}"""
                self.cursor.execute(sql_update_query)

                self.connection.commit()
            self.connection.close()
        except Exception as e:
            print(e)

    def add_printer(self, model, cartridge_model, drum_cartridge, ip_address, mac, location, building):
        """
        Метод добавления принтера в базу данных
        :param mac:
        :param model:
        :param cartridge_model:
        :param drum_cartridge:
        :param ip_address:
        :param location:
        :param building:
        :return:
        """
        try:
            self.cursor.execute(
                "INSERT INTO ap_printers (model, cartridge_model,drum_cartridge, ip_address, mac, location, building) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (model, cartridge_model, drum_cartridge, ip_address, mac, location, building))
            self.connection.commit()
            self.connection.close()
        except PrinterAbortAdd as p:
            print(p)
        except Exception as e:
            print(e)

    def show_printers(self):
        self.cursor.execute(
            "SELECT id, model, cartridge_model, drum_cartridge, ip_address, mac, location, building FROM ap_printers")
        printers = self.cursor.fetchall()
        self.connection.close()
        return printers

    def search_printer(self, column, string):
        try:

            self.cursor.execute(f"SELECT * FROM ap_printers WHERE {column} LIKE '%{string}%'")
            printer = self.cursor.fetchall()
            self.connection.close()
            return printer
        except Exception as s:
            pass

    def show_printer_by_building(self, building):
        self.cursor.execute(f"SELECT id, model, cartridge_model, drum_cartridge, ip_address, mac, location, building "
                            f"FROM ap_printers where building = '{building}'")
        printers = self.cursor.fetchall()
        self.connection.close()
        return printers

    # def load_html_content(self, id):
    #     self.cursor.execute(f"SELECT html_content "
    #                         f"FROM ap_printers where id = '{id}'")
    #     html_content = self.cursor.fetchall()
    #     self.connection.close()
    #     return html_content
