import sqlite3



conn = sqlite3.connect('printers.db')
cursor = conn.cursor()


def add_printer(model, cartridge_model,drum_cartridge, ip_address, location,):
    cursor.execute("INSERT INTO printers (model, cartridge_model,drum_cartridge, ip_address, location) VALUES (?, ?, ?, ?, ?)",
                   (model, cartridge_model, drum_cartridge, ip_address, location))
    conn.commit()
    print("Принтер успешно добавлен в базу данных")


# Функция для вывода списка всех принтеров
def show_printers():
    cursor.execute("SELECT * FROM printers")
    printers = cursor.fetchall()
    # for printer in printers:
    #     print(f"ID: {printer[0]}, Модель: {printer[1]}, Модель картриджа: {printer[2]},Модель барабана: {printer[5]}, IP-адрес: {printer[3]}, "
    #           f"Местоположение {printer[4]}")
    return printers


# Функция для поиска принтера по модели
def search_printer(model):

    cursor.execute("SELECT * FROM printers WHERE model=?", (model,))
    printer = cursor.fetchone()
    if printer:
        print(f"ID: {printer[0]}, Модель: {printer[1]}, Модель картриджа: {printer[2]},Модель барабана: {printer[5]}, IP-адрес: {printer[3]}"
              f"Местоположение {printer[4]}")
    else:
        print("Принтер не найден")

