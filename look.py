import os
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtGui


Form, Windows = uic.loadUiType(r'look.ui')
win = QApplication([])
windows = Windows()
windows.setFixedSize(1359, 866)
form = Form()
form.setupUi(windows)


def on1():
    form.labelT1.setText(str('Пирамида Хеопса'))
    form.labelT11.setText(str('Мастаба'))
    form.labelR1.setText(str('Первое чудо света - Пирамида Хеопса'))
def on2():
    form.labelT2.setText(str('Висячие сады Семирамиды'))
    form.labelT22.setText(str('Великая пирамида Чолулы'))
    form.labelR2.setText(str('Второе чудо света - Висячие сады Семирамиды'))
def on3():
    form.labelT3.setText(str('Статуя Зевса в Олимпии'))
    form.labelT33.setText(str('Моаи'))
    form.labelR3.setText(str('Третье чудо света - Статуя Зевса \nв Олимпии'))
def on4():
    form.labelT4.setText(str('Храм афайи'))
    form.labelT44.setText(str('Храм Артемиды в Эфесе'))
    form.labelR4.setText(str('Четвертое чудо света - Храм Артемиды в Эфесе'))
def on5():
    form.labelT5.setText(str('Аныткабир'))
    form.labelT55.setText(str('Мавзолей в Галикарнасе'))
    form.labelR5.setText(str('Пятое чудо света - Мавзолей в Галикарнасе'))
def on6():
    form.labelT6.setText(str('Колосс Родосский'))
    form.labelT66.setText(str('Статуя Афины в Акрополе'))
    form.labelR6.setText(str('Шестое чудо света - Колосс Родосский'))
def on7():
    form.labelT7.setText(str('Маяк Старт Пойнт'))
    form.labelT77.setText(str('Александрийский маяк'))
    form.labelR7.setText(str('Седьмое чудо света - Александрийский маяк'))
def playAudioFile1():
    full_file_path = os.path.join(os.getcwd(), 'win.wav')
    url = QUrl.fromLocalFile(full_file_path)
    content = QMediaContent(url)
    form.radioButton1_1.setMedia(content)
    form.radioButton1.setMedia(content)
    form.radioButton4.setMedia(content)
    form.radioButton6.setMedia(content)
    form.radioButton2_1.setMedia(content)
    form.radioButton7.setMedia(content)
    form.radioButton10.setMedia(content)
    form.radioButton12.setMedia(content)
    form.radioButton13.setMedia(content)
    form.radioButton3_1.setMedia(content)
    form.radioButton15.setMedia(content)
    form.radioButton18.setMedia(content)
    form.radioButton19.setMedia(content)
    form.radioButton22.setMedia(content)
    form.radioButton23.setMedia(content)

    form.radioButton4_3.setMedia(content)
    form.radioButton26.setMedia(content)
    form.radioButton27.setMedia(content)
    form.radioButton29.setMedia(content)

    form.radioButton5_3.setMedia(content)
    form.radioButton31.setMedia(content)
    form.radioButton34.setMedia(content)
    form.radioButton36.setMedia(content)

    form.radioButton6_1.setMedia(content)
    form.radioButton38.setMedia(content)
    form.radioButton40.setMedia(content)
    form.radioButton42.setMedia(content)

    form.radioButton7_3.setMedia(content)
    form.radioButton44.setMedia(content)
    form.radioButton46.setMedia(content)
    form.radioButton49.setMedia(content)

    form.radioButton51.setMedia(content)
    form.radioButton55.setMedia(content)
    form.radioButton58.setMedia(content)
    form.radioButton59.setMedia(content)
    form.radioButton62.setMedia(content)
    form.radioButton66.setMedia(content)
    form.radioButton68.setMedia(content)

def playAudioFile2():
    full_file_path = os.path.join(os.getcwd(), 'no.wav')
    url = QUrl.fromLocalFile(full_file_path)
    content = QMediaContent(url)
    form.radioButton1_2.setMedia(content)
    form.radioButton2.setMedia(content)
    form.radioButton3.setMedia(content)
    form.radioButton5.setMedia(content)
    form.radioButton2_3.setMedia(content)
    form.radioButton8.setMedia(content)
    form.radioButton9.setMedia(content)
    form.radioButton11.setMedia(content)
    form.radioButton14.setMedia(content)
    form.radioButton3_3.setMedia(content)
    form.radioButton16.setMedia(content)
    form.radioButton17.setMedia(content)
    form.radioButton20.setMedia(content)
    form.radioButton21.setMedia(content)
    form.radioButton24.setMedia(content)

    form.radioButton4_1.setMedia(content)
    form.radioButton25.setMedia(content)
    form.radioButton28.setMedia(content)
    form.radioButton30.setMedia(content)

    form.radioButton5_1.setMedia(content)
    form.radioButton32.setMedia(content)
    form.radioButton33.setMedia(content)
    form.radioButton35.setMedia(content)

    form.radioButton6_3.setMedia(content)
    form.radioButton37.setMedia(content)
    form.radioButton41.setMedia(content)
    form.radioButton43.setMedia(content)

    form.radioButton7_1.setMedia(content)
    form.radioButton45.setMedia(content)
    form.radioButton47.setMedia(content)
    form.radioButton48.setMedia(content)

    form.radioButton50.setMedia(content)
    form.radioButton52.setMedia(content)
    form.radioButton53.setMedia(content)
    form.radioButton54.setMedia(content)
    form.radioButton56.setMedia(content)
    form.radioButton57.setMedia(content)
    form.radioButton60.setMedia(content)
    form.radioButton61.setMedia(content)
    form.radioButton63.setMedia(content)
    form.radioButton64.setMedia(content)
    form.radioButton65.setMedia(content)
    form.radioButton67.setMedia(content)
    form.radioButton69.setMedia(content)
    form.radioButton70.setMedia(content)

def clear1():
    form.labelT1.clear()
    form.labelT11.clear()
    form.labelR1.clear()
def clear2():
    form.labelT2.clear()
    form.labelT22.clear()
    form.labelR2.clear()
def clear3():
    form.labelT3.clear()
    form.labelT33.clear()
    form.labelR3.clear()
def clear4():
    form.labelT4.clear()
    form.labelT44.clear()
    form.labelR4.clear()
def clear5():
    form.labelT5.clear()
    form.labelT55.clear()
    form.labelR5.clear()
def clear6():
    form.labelT6.clear()
    form.labelT66.clear()
    form.labelR6.clear()
def clear7():
    form.labelT7.clear()
    form.labelT77.clear()
    form.labelR7.clear()

defaultfont = QtGui.QFont('Bookman Old Style', 14) #указываем нужный шрифт
msg = QMessageBox()
msg.setFont(defaultfont)
msg.setWindowTitle("Подсказка")  #заголовок
#цвет фона
msg.setStyleSheet(
    """
                    QMessageBox {
                        background-color: rgb(87, 121, 172);               
                    }         
                    """
    )

msg.setIcon(QMessageBox.NoIcon) #нет значка
msg.setStandardButtons(QMessageBox.Ok) #кнопки

def smm1():
    msg.setText("1.Это чудо имеет правильную геометрическую форму. \n2.Оно сложено из обтесанных каменных блоков. \n3.Как оно построено, ученым до сих пор неизвестно.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()
def smm2():
    msg.setText("1.Его украшали 127 мраморных колонн. \n2.Оно было и музеем и хранилищем богатых людей того времени. \n3.Оно находилось в городе Эфесе.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()
def smm3():
    msg.setText("1.Его изображение есть на древних монетах. \n2.С ним связаны знаменитые состязания. \n3.Оно изображало греческого бога.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()
def smm4():
    msg.setText("1.От названия этого острова появилось слово «фара». \n2.Сейчас на том месте, где оно было – крепость Каит-бей. \n3.Днем оно было красивей – ночью нужнее.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()
def smm5():
    msg.setText("1.Высота его около 60 м. \n2.На его возведение потребовалось 500 талантов (13т.) бронзы и 300 талантов (8т.) железа. \n3.Обломки его пролежали в земле более 1000 лет.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()
def smm6():
    msg.setText("1.Ни крепостные стены, ни семиступенчатая башня этого города не могли сравниться с ними по красоте. \n2.С ним связаны последние дни великого полководца Древнего Мира.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()
def smm7():
    msg.setText("1.Оно было построено по приказу царя и его жены. \n2.На его развалинах построили крепость Святого Петра.")  #текст, который мы хотим видеть в сообщении
    msg.exec_()

defaultfontt = QtGui.QFont('Bookman Old Style', 18) #указываем нужный шрифт
def smmEnd():
    msgg = QMessageBox()
    msgg.setFont(defaultfontt)
    msgg.setWindowTitle("Финиш")  #заголовок
    msgg.setText("ПОЗДРАВЛЯЕМ! \nВы завершили игровой крест \n«Я ищу»") #текст, который мы хотим видеть в сообщении
    msgg.setIcon(QMessageBox.NoIcon)   #нет значка
    msgg.setStandardButtons(QMessageBox.Ok) #кнопки
    # цвет фона
    msgg.setStyleSheet(
    """
                    QMessageBox {
                        background-color: rgb(239, 255, 165);
                    }         
                    """
    )

    msgg.exec_()

#first
form.radioButton1_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton1_2.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
#
form.radioButton2_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton2_3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
#
form.radioButton3_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton3_3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
#
form.radioButton4_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
form.radioButton4_3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
#
form.radioButton5_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
form.radioButton5_3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
#
form.radioButton6_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton6_3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
#
form.radioButton7_1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                            "}")
form.radioButton7_3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
#second
form.radioButton1.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton2.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton3.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton4.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton5.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton6.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"

                                "}")
#
form.radioButton7.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton8.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton9.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton10.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton11.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton12.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"

                                "}")
form.radioButton13.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton14.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
#
form.radioButton15.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton16.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton17.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton18.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton19.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton20.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"

                                "}")
form.radioButton21.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton22.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton23.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton24.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
#
form.radioButton25.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton26.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton27.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton28.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton29.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton30.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
#
form.radioButton31.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton32.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton33.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton34.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton35.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton36.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
#
form.radioButton37.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton38.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton40.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton41.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton42.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton43.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton44.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton45.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton46.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton47.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton48.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton49.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")





form.radioButton50.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton51.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
#
form.radioButton52.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton53.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton54.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton55.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton56.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton57.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton58.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton59.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton60.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton61.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton62.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton63.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton64.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton65.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton66.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton67.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton68.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : green;"
                                "}")
form.radioButton69.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")
form.radioButton70.setStyleSheet("QRadioButton::checked"
                                "{"
                                "background-color : red;"
                                "}")

sound = QSound('win.wav')
soundd=QSound('no.wav')
form.radioButton1_1.clicked.connect(sound.play)
form.radioButton1.clicked.connect(sound.play)
form.radioButton4.clicked.connect(sound.play)
form.radioButton6.clicked.connect(sound.play)
form.radioButton2_1.clicked.connect(sound.play)
form.radioButton7.clicked.connect(sound.play)
form.radioButton10.clicked.connect(sound.play)
form.radioButton12.clicked.connect(sound.play)
form.radioButton13.clicked.connect(sound.play)
form.radioButton3_1.clicked.connect(sound.play)
form.radioButton15.clicked.connect(sound.play)
form.radioButton18.clicked.connect(sound.play)
form.radioButton19.clicked.connect(sound.play)
form.radioButton22.clicked.connect(sound.play)
form.radioButton23.clicked.connect(sound.play)
form.radioButton4_3.clicked.connect(sound.play)
form.radioButton26.clicked.connect(sound.play)
form.radioButton27.clicked.connect(sound.play)
form.radioButton29.clicked.connect(sound.play)
form.radioButton5_3.clicked.connect(sound.play)
form.radioButton31.clicked.connect(sound.play)
form.radioButton34.clicked.connect(sound.play)
form.radioButton36.clicked.connect(sound.play)
form.radioButton6_1.clicked.connect(sound.play)
form.radioButton38.clicked.connect(sound.play)
form.radioButton40.clicked.connect(sound.play)
form.radioButton42.clicked.connect(sound.play)
form.radioButton7_3.clicked.connect(sound.play)
form.radioButton44.clicked.connect(sound.play)
form.radioButton46.clicked.connect(sound.play)
form.radioButton49.clicked.connect(sound.play)
form.radioButton51.clicked.connect(sound.play)
form.radioButton55.clicked.connect(sound.play)
form.radioButton58.clicked.connect(sound.play)
form.radioButton59.clicked.connect(sound.play)
form.radioButton62.clicked.connect(sound.play)
form.radioButton66.clicked.connect(sound.play)
form.radioButton68.clicked.connect(sound.play)




form.radioButton1_2.clicked.connect(soundd.play)
form.radioButton2.clicked.connect(soundd.play)
form.radioButton3.clicked.connect(soundd.play)
form.radioButton5.clicked.connect(soundd.play)
form.radioButton2_3.clicked.connect(soundd.play)
form.radioButton8.clicked.connect(soundd.play)
form.radioButton9.clicked.connect(soundd.play)
form.radioButton11.clicked.connect(soundd.play)
form.radioButton14.clicked.connect(soundd.play)
form.radioButton3_3.clicked.connect(soundd.play)
form.radioButton16.clicked.connect(soundd.play)
form.radioButton17.clicked.connect(soundd.play)
form.radioButton20.clicked.connect(soundd.play)
form.radioButton21.clicked.connect(soundd.play)
form.radioButton24.clicked.connect(soundd.play)
form.radioButton4_1.clicked.connect(soundd.play)
form.radioButton25.clicked.connect(soundd.play)
form.radioButton28.clicked.connect(soundd.play)
form.radioButton30.clicked.connect(soundd.play)
form.radioButton5_1.clicked.connect(soundd.play)
form.radioButton32.clicked.connect(soundd.play)
form.radioButton33.clicked.connect(soundd.play)
form.radioButton35.clicked.connect(soundd.play)
form.radioButton6_3.clicked.connect(soundd.play)
form.radioButton37.clicked.connect(soundd.play)
form.radioButton41.clicked.connect(soundd.play)
form.radioButton43.clicked.connect(soundd.play)
form.radioButton7_1.clicked.connect(soundd.play)
form.radioButton45.clicked.connect(soundd.play)
form.radioButton47.clicked.connect(soundd.play)
form.radioButton48.clicked.connect(soundd.play)

form.radioButton50.clicked.connect(soundd.play)
form.radioButton52.clicked.connect(soundd.play)
form.radioButton53.clicked.connect(soundd.play)
form.radioButton54.clicked.connect(soundd.play)
form.radioButton56.clicked.connect(soundd.play)
form.radioButton57.clicked.connect(soundd.play)
form.radioButton60.clicked.connect(soundd.play)
form.radioButton61.clicked.connect(soundd.play)
form.radioButton63.clicked.connect(soundd.play)
form.radioButton64.clicked.connect(soundd.play)
form.radioButton65.clicked.connect(soundd.play)
form.radioButton67.clicked.connect(soundd.play)
form.radioButton69.clicked.connect(soundd.play)
form.radioButton70.clicked.connect(soundd.play)

form.pushButtonR1.clicked.connect(smm1)
form.pushButtonR2.clicked.connect(smm2)
form.pushButtonR3.clicked.connect(smm3)
form.pushButtonR4.clicked.connect(smm4)
form.pushButtonR5.clicked.connect(smm5)
form.pushButtonR6.clicked.connect(smm6)
form.pushButtonR7.clicked.connect(smm7)


form.pushButtonP1.clicked.connect(on1)
form.pushButtonP2.clicked.connect(on2)
form.pushButtonP3.clicked.connect(on3)
form.pushButtonP4.clicked.connect(on4)
form.pushButtonP5.clicked.connect(on5)
form.pushButtonP6.clicked.connect(on6)
form.pushButtonP7.clicked.connect(on7)
form.pushButtonC1.clicked.connect(clear1)
form.pushButtonC2.clicked.connect(clear2)
form.pushButtonC3.clicked.connect(clear3)
form.pushButtonC4.clicked.connect(clear4)
form.pushButtonC5.clicked.connect(clear5)
form.pushButtonC6.clicked.connect(clear6)
form.pushButtonC7.clicked.connect(clear7)
form.pushButtonEnd.clicked.connect(smmEnd)


windows.show()
win.exec()