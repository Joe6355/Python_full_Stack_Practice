
import sys

#импорт эл созд ui
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox
)
#cозд искл если user переносит пустой текст
class EmptyTextError(Exception):
    pass

#Создание класса главного window
class WordsDSV(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()  #вызов созд ui

    #вызов метода созд интерфейса
    def InitUI(self):
        #название окна
        self.setWindowTitle("Перемещение текста DSV")

        self.resize(500, 150)  #размер окна

        self.value_1 = QLineEdit(self)  #текстовое поле 1
        self.value_2 = QLineEdit(self)  #текстовое поле 2

        #созд кнопку со стрелкой вправо
        self.arrow_button = QPushButton("->", self)

        #уст W button
        self.arrow_button.setFixedWidth(50)

        #горизонт эллементов
        layout = QHBoxLayout()

        #добав поля и кнопку между ними
        layout.addWidget(self.value_1)
        layout.addWidget(self.arrow_button)
        layout.addWidget(self.value_2)

        #устр расположене в окне
        self.setLayout(layout)

        #подключ нажатие кнопки к функции
        self.arrow_button.clicked.connect(self.transfer_DSV)

    #функция для перемещения текста

    #функция для перемещения текста
    def transfer_DSV(self):

        try:
            #проверяем куда направлена стрелка
            if self.arrow_button.text() == "->":

                #получ текст из поля 1
                text = self.value_1.text()

                #проверяем что поле не пустое
                if not text.strip():
                    raise EmptyTextError(
                        "Поле 1 пустое! Введите текст для перемещения вправо."
                    )

                #перенос текста в поле 2
                self.value_2.setText(text)

                #очищаем поле 1
                self.value_1.clear()

                #меняем направление стрелки
                self.arrow_button.setText("<-")

            else:
                #получ текст из поля 2
                text = self.value_2.text()

                #проверяем что поле не пустое
                if not text.strip():
                    raise EmptyTextError(
                        "Поле 2 пустое! Введите текст для перемещения влево."
                    )

                #перенос текста в поле 1
                self.value_1.setText(text)

                #очищаем поле 2
                self.value_2.clear()

                #меняем направление стрелки
                self.arrow_button.setText("->")

        #обработка ошибки пустого поля
        except EmptyTextError as error:

            #вывод сообщения пользователю
            QMessageBox.warning(
                self,
                "Ошибка перемещения",
                str(error)
            )


#запуск
if __name__ == "__main__":

    #созд приложение PyQt6
    app = QApplication(sys.argv)

    #создаем обьект нашего окна
    window = WordsDSV()

    #показываем окно
    window.show()

    #запускаем обработчик событий
    sys.exit(app.exec())
