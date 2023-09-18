import sys

from PyQt6 import QtWidgets

from design import PrinterDesign

app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = PrinterDesign()  # Создаём объект класса PrinterDesign
window.load_setting()
window.get_column_name()
window.show()  # Показываем окно
app.exec()  # и запускаем приложение
