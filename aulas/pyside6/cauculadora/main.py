# import sys

# from main_window import MainWindow
# from PySide6.QtWidgets import QApplication, QLabel

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()

#     label1 = QLabel('O meu texto')
#     label1.setStyleSheet('font-size: 150px;')
#     window.v_layout.addWidget(label1)
#     window.adjustFixedSize()

#     window.show()
#     app.exec()

import sys

from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

from buttons import Button


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    button = Button('Texto do botão')
    window.addToVLayout(button)

    button2 = Button('Texto do botão')
    window.addToVLayout(button2)
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()