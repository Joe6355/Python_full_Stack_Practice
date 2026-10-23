
import io
import sys

#импорт эл для созд ui
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


#созд переменную для хранения дизайна из Qt Designer
tempDSV = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="Name">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>90</y>
      <width>113</width>
      <height>26</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="LastName">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>140</y>
      <width>113</width>
      <height>26</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>70</y>
      <width>49</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>120</y>
      <width>49</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Фамилия</string>
    </property>
   </widget>
   <widget class="QPushButton" name="addStudentBtn">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>190</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="sizePolicy">
     <sizepolicy hsizetype="Minimum" vsizetype="Preferred">
      <horstretch>0</horstretch>
      <verstretch>0</verstretch>
     </sizepolicy>
    </property>
    <property name="text">
     <string>Добавить в список</string>
    </property>
   </widget>
   <widget class="QListWidget" name="presenceList">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>70</y>
      <width>256</width>
      <height>192</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>50</y>
      <width>241</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>                  Cписок присутствующих </string>
    </property>
    <property name="scaledContents">
     <bool>false</bool>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>33</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


#создание класса главного окна
class GroupList_DSV(QMainWindow):

    def __init__(self):
        super().__init__()

        #созд поток для чтения дизайна
        f = io.StringIO(tempDSV)

        #загружаем ui из переменной
        uic.loadUi(f, self)

        #название окна
        self.setWindowTitle("Список присутствующих DSV")

        #подгон размера кнопки под текст
        self.addStudentBtn.adjustSize()

        #подключ нажатие кнопки к функции
        self.addStudentBtn.clicked.connect(self.status_DSV)

    #функция добавления студента в список
    def status_DSV(self):

        #получ имя из первого поля
        name = self.Name.text().strip()

        #получ фамилию из второго поля
        lastname = self.LastName.text().strip()

        #проверяем что оба поля заполнены
        if name and lastname:

            #объединяем фамилию и имя
            student = lastname + " " + name

            #добав студента в список
            self.presenceList.addItem(student)

            #очищаем поля после добавления
            self.Name.clear()
            self.LastName.clear()

            #возвращаем курсор в поле имени
            self.Name.setFocus()


#запуск программы
if __name__ == "__main__":

    #созд приложение PyQt6
    app = QApplication(sys.argv)

    #создаем объект нашего окна
    window = GroupList_DSV()

    #показываем окно
    window.show()

    #запускаем обработчик событий
    sys.exit(app.exec())
