import os
import sys

from PyQt6.QtWidgets import QApplication

from user_application import UserApplication


def main():
    app = QApplication(sys.argv)

    file_dir = os.path.dirname(os.path.realpath('__file__'))

    with open(os.path.join(file_dir, 'styles/style.qss'), 'r') as file:
        app.setStyleSheet(file.read())

    window = UserApplication()
    window.show()

    # Запускаем цикл событий.
    app.exec()


if __name__ == '__main__':
    main()

