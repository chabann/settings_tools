import subprocess

from PyQt6.QtWidgets import QMainWindow, QGridLayout, QPushButton, QFrame
from PyQt6 import uic

from connection import Connection
from builders.list_builder import ListBuilder


class UserApplication(QFrame):        
    def __init__(self):
        super().__init__()

        uic.loadUi('design-profile.ui', self)
        layout = QGridLayout()
        self.setLayout(layout)

    def update(self):        
        cmd = f'python {self.execPath.text()} {self.Param1.text()}'

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, encoding='utf-8')
        out, err = p.communicate()
        console_text = '<p>'
        result = out.split('\n')
        for lin in result:
            if lin:
                console_text += lin + '</br>'
        console_text += '</p>'
        
        self.Console.setText(out)
