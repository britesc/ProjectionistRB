import os

from PySide6 import (
    QtGui,
    QtCore
)

from PySide6.QtCore import (
    QSize,
    QFileInfo
)
    
from PySide6.QtGui import (
    # QAction,
    # QIcon,
    QPixmap
)
    
from PySide6.QtWidgets import (
    QMainWindow,
    # QToolBar,
    # QPushButton,
    # QStatusBar,
    # QApplication,
    QHeaderView,
    # QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    # QVBoxLayout,
    # QHBoxLayout,
    # QTableView,
    QLabel,
)    

from PySide6.QtCore import (
    Qt
)

from sqlitedict import (
    SqliteDict
)

from main.mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self) # type: ignore
        self.app = app #declare an app member