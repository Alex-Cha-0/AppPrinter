import pymssql as mc

from dotenv import load_dotenv
import os

# загрузка настроек
load_dotenv()

SERVERMSSQL = os.getenv("SERVERMSSQL")
USERMSSQL = os.getenv("USERMSSQL")
PASSWORDMSSQL = os.getenv("PASSWORDMSSQL")
DATABASEMSSQL = os.getenv("DATABASEMSSQL")


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
                (model, cartridge_model, drum_cartridge, ip_address, mac.upper(), location, building))
            self.connection.commit()
            self.connection.close()
        except PrinterAbortAdd as p:
            print(p)
        except Exception as e:
            print(e)

    def show_printers(self):
        self.cursor.execute(
            "SELECT id, model, cartridge_model, drum_cartridge, ip_address, network_id, mac, location, building FROM ap_printers")
        printers = self.cursor.fetchall()
        self.connection.close()
        return printers

    def search_printer(self, column, string):
        try:

            self.cursor.execute(
                f"SELECT id, model, cartridge_model, drum_cartridge, ip_address, network_id, mac, location, building FROM ap_printers WHERE {column} LIKE '%{string}%'")
            printer = self.cursor.fetchall()
            self.connection.close()
            return printer
        except Exception as s:
            pass

    def show_printer_by_building(self, building):
        self.cursor.execute(
            f"SELECT id, model, cartridge_model, drum_cartridge, ip_address, network_id, mac, location, building "
            f"FROM ap_printers where building = '{building}'")
        printers = self.cursor.fetchall()
        self.connection.close()
        return printers

    def show_info(self, id):
        self.cursor.execute(
            f"SELECT date_repair, pages_printed, comment  FROM ap_printers_info where printer_id = {id}")
        printer_info = self.cursor.fetchall()
        self.connection.close()
        return printer_info

    def add_info(self, date_repair, pages_printed, comment, printer_id):
        self.cursor.execute(
            "INSERT INTO ap_printers_info (date_repair, pages_printed,comment, printer_id) VALUES (%s,%s,%s,%s)",
            (date_repair, pages_printed, comment, printer_id))
        self.connection.commit()
        self.connection.close()
