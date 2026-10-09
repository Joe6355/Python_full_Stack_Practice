import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWidget (QMainWindow):
    def __init__(self):
        super().__init__()

        #загружаем ui из qt дизайнера
        uic.loadUi("lr2_DudinSergey.ui", self)

#проверка что фалй запущен напрямую
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWidget()#создаем обьект окна
    window.show()#Отрисовываем окно на экране
    sys.exit(app.exec_())#обработчик событий