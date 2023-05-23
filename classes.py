import sqlite3


#
# conn = sqlite3.connect('printers.db')
# cursor = conn.cursor()

class PrinterAbortAdd(Exception):
    def __str__(self):
        return f"Ошибка добавления принтера"


class Printer:
    def __init__(self, db_name):
        """
        Название базы данных
        :param db_name:
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def edit_printers_column(self, data):
        try:
            for i in range(len(data)):
                column_name = data[i][0]
                _data = (data[i][1])
                cell = data[i][2]
                print(column_name, _data, cell)
                sql_update_query = f"""UPDATE printers set {column_name} = '{_data}' where id = {cell}"""
                print(sql_update_query)
                self.cursor.execute(sql_update_query)
                self.connection.commit()
            self.connection.close()
        except Exception as e:
            print(e)

    def add_printer(self, model, cartridge_model, drum_cartridge, ip_address, mac, location):
        """
        Метод добавления принтера в базу данных
        :param mac:
        :param model:
        :param cartridge_model:
        :param drum_cartridge:
        :param ip_address:
        :param location:
        :return:
        """
        try:
            self.cursor.execute(
                "INSERT INTO printers (model, cartridge_model,drum_cartridge, ip_address, mac, location) VALUES (?, ?, ?, "
                "?, ?, ?)",
                (model, cartridge_model, drum_cartridge, ip_address, mac, location))
            self.connection.commit()
            self.connection.close()
            print("Принтер успешно добавлен")
        except PrinterAbortAdd as p:
            print(p)
        except Exception as e:
            print(e)

    def show_printers(self):
        self.cursor.execute("SELECT id, model, cartridge_model, drum_cartridge, ip_address, mac, location FROM printers")
        printers = self.cursor.fetchall()
        self.connection.close()
        return printers

    def search_printer(self, model):

        self.cursor.execute("SELECT * FROM printers WHERE model=?", (model,))
        printer = self.cursor.fetchone()
        try:
            if printer:
                return printer
            else:
                return "Принтер не найден"
        except Exception as s:
            print(s)
