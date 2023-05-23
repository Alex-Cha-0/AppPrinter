from classes import Printer

p = Printer('printers.db')
p.add_printer(input("Модель принтера: "), input("Модель картриджа: "),input("Модель барабана: "), input("IP-адрес: "),
            input("Местоположение: "))