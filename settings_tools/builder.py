from abc import ABC, abstractmethod

from connection import Connection

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, QRectF, QRect


class Builder(ABC):
    def __init__(self, app, connection: Connection) -> None:
        super().__init__()

        self._connection = connection
        self._app = app

    def build(self):
        pass

    def build_menu(self):
        self._app.setWindowTitle("Feedback Tools")
        self._app.setMinimumSize(QSize(1500, 1000))

        # main_CF = QtWidgets.QFrame(self._app)
        # main_CF.setObjectName('mainFrame')
        # self._app.setCentralWidget(main_CF)

        # main_CL = QtWidgets.QVBoxLayout(main_CF)
        # # main_CL.setContentsMargins(0, 0, 0, 0)
        # # main_CL.setFixedSize(10, 10)
        # # main_CL.move(20, 20)
        # # main_CL.setGeometry(QRect(10, 10, 10, 10))


        # # creating the first subcontainer + layout, parenting it
        # asset_CGF = QtWidgets.QFrame(main_CF)
        # # asset_CGF.setGeometry(QRect(0, 0, 0, 0))
        # asset_CGF.setObjectName('frame2')
        # asset_CGF.setFrameRect(QRect(10, 10, 20, 20))
        # # asset_CGF.setFixedSize(10, 10)
        # # asset_CGF.move(10, 10)
        # # main_CL.addWidget(asset_CGF)
        # main_CL.addWidget(asset_CGF)

        # asset_CGF.setStyleSheet('background-color: rgba(0, 150, 0, 1);')
        # asset_CGL = QtWidgets.QHBoxLayout(asset_CGF)

        # creating label and lineEdit, both are supposed to be on top of asset_CGF    
        # asset_label = QtWidgets.QLabel("Assetname: ", asset_CGF)
        # asset_CGL.addWidget(asset_label)
        # asset_name = QtWidgets.QLineEdit("MyNewAsset", asset_CGF)
        # asset_CGL.addWidget(asset_name)

        # scene = QGraphicsScene(self._app)
        # view = QGraphicsView(scene)

        # rect = QRectF(0, 0, 100, 100)

        # rect_item = QGraphicsRectItem(rect)
        # rect_item.setObjectName('frame2')

        # # graphicsView = QGraphicsView(self.centralwidget)
        # # view.setGeometry(QRect(40, 60, 811, 561))
        # view.setObjectName("mainFrame")

        # rect = QRect(0, 60, 811, 561)
        # # rect.setObjectName("frame2")
        # scene.addItem(rect_item)

        # # scene.addItem(rect_item)

        # self._app.setCentralWidget(view)

        # button = QPushButton("Press Me!")
        # self._app.setCentralWidget(button)