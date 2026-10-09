
import sys

#импорт эл для созд ui
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QCheckBox,
    QGridLayout
)
from PyQt6.QtCore import Qt


#создание класса главного окна
class WidgetsDSV(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()  #вызов созд ui

    #метод создания интерфейса
    def InitUI(self):

        #название окна
        self.setWindowTitle("Управление виджетами DSV")

        self.resize(600, 350)  #размер окна

        #созд 2 текстовых поля
        self.value_1 = QLineEdit(self)
        self.value_2 = QLineEdit(self)

        #созд 2 кнопки
        self.button_1 = QPushButton("Кнопка 1", self)
        self.button_2 = QPushButton("Кнопка 2", self)

        #созд 2 надписи
        self.label_1 = QLabel("Надпись 1", self)
        self.label_2 = QLabel("Надпись 2", self)

        #созд 6 галочек для управления эл
        self.check_1 = QCheckBox("Поле 1", self)
        self.check_2 = QCheckBox("Поле 2", self)
        self.check_3 = QCheckBox("Кнопка 1", self)
        self.check_4 = QCheckBox("Кнопка 2", self)
        self.check_5 = QCheckBox("Надпись 1", self)
        self.check_6 = QCheckBox("Надпись 2", self)

        #список всех галочек
        self.checkboxes = [
            self.check_1,
            self.check_2,
            self.check_3,
            self.check_4,
            self.check_5,
            self.check_6
        ]

        #изначально все галочки включены
        for check in self.checkboxes:
            check.setChecked(True)

        #для первой галочки разрешаем 3 состояния
        #Checked, Unchecked, Indeterminate
        self.check_1.setTristate(True)

        #связываем галочки с эл
        self.widgets = {
            self.check_1: self.value_1,
            self.check_2: self.value_2,
            self.check_3: self.button_1,
            self.check_4: self.button_2,
            self.check_5: self.label_1,
            self.check_6: self.label_2
        }

        #созд сетку для расположения эл
        layout = QGridLayout()

        #добав 2 текстовых поля и галочки
        layout.addWidget(self.check_1, 0, 0)
        layout.addWidget(self.value_1, 0, 1)

        layout.addWidget(self.check_2, 1, 0)
        layout.addWidget(self.value_2, 1, 1)

        #добав 2 кнопки и галочки
        layout.addWidget(self.check_3, 2, 0)
        layout.addWidget(self.button_1, 2, 1)

        layout.addWidget(self.check_4, 3, 0)
        layout.addWidget(self.button_2, 3, 1)

        #добав 2 надписи и галочки
        layout.addWidget(self.check_5, 4, 0)
        layout.addWidget(self.label_1, 4, 1)

        layout.addWidget(self.check_6, 5, 0)
        layout.addWidget(self.label_2, 5, 1)

        #устр расположение в окне
        self.setLayout(layout)

        #подключ все галочки к одной функции
        for check in self.checkboxes:
            check.stateChanged.connect(self.status_DSV)

    #общая функция для скрытия и показа эл
    def status_DSV(self, state):

        #определяем какая галочка вызвала функцию
        check = self.sender()

        #находим эл связанный с этой галочкой
        widget = self.widgets[check]

        #проверяем состояние галочки
        if check.checkState() == Qt.CheckState.Checked:

            #если галочка стоит показываем эл
            widget.show()

        else:
            #если галочки нет скрываем эл
            #при Indeterminate тоже скрываем
            widget.hide()


#запуск программы
if __name__ == "__main__":

    #созд приложение PyQt6
    app = QApplication(sys.argv)

    #созд объект нашего окна
    window = WidgetsDSV()

    #показываем окно
    window.show()

    #запускаем обработчик событий
    sys.exit(app.exec())
