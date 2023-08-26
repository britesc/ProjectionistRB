#!/usr/bin/env python3
# coding: utf-8

import sys

from PySide6.QtGui import (
    QIcon, 
    QAction
)
    
from PySide6.QtWidgets import (
    # trunk-ignore(ruff/F401)
    QApplication,  # noqa: F401
    QSystemTrayIcon,
    QMenu,
    QMessageBox,
    QWidget
)    

from PySide6.QtCore import (
    QSize
)

# trunk-ignore(ruff/F401)
import resources.buttonsGlassRound_rc


class P2_Tray:
    """ A Class for the Tray Icon. """
    
    def __init__(self, app, mainwindow) -> None:
        # trunk-ignore(ruff/D401)
        """The __init__ Function."""
        super().__init__()
        self.ClassVersion = "0.0.0"
        self.app = app
        self.maiwindow = mainwindow
        
    def __str__(self) -> str:
        # trunk-ignore(ruff/D401)
        """The __str__ Function."""
        return "P2_Tray"

    def __repr__(self) -> str:
        # trunk-ignore(ruff/D401)
        """The __repr__ Function."""
        return "P2_Tray"

    def getClassVersion(self) -> str:
        # trunk-ignore(ruff/D401)
        """The Version String of this Class."""
        return self.ClassVersion 
    
    def setupTray(self) -> None:
        # trunk-ignore(ruff/D401)
        """Setup the Tray Icon."""
        

                
        if not QSystemTrayIcon.isSystemTrayAvailable():
            message = QMessageBox()
            message.setMinimumSize(400,200)
            message.setWindowTitle("SetupTray")
            message.setText("Warning")
            message.setInformativeText("The System Tray is Not Available")
            message.setIcon(QMessageBox.Warning) # type: ignore
            message.setStandardButtons(QMessageBox.Ok) # type: ignore
            message.setDefaultButton(QMessageBox.Ok) # type: ignore
            message.exec()
            return
        else:
            # message.setInformativeText("The System Tray is Available")
            self.app.setQuitOnLastWindowClosed(False)
            
        

        # Create the icon
        
        tray = QSystemTrayIcon(QIcon(u":/buttons/glassRound/glassButtonProjectionist.png"), self.app)  # noqa: E501
        
        menu = QMenu()
        
        action_hide_icon = QIcon("u:/buttons/glassRound/glassButtonProjectionist.png")
        action_hide = QAction(action_hide_icon, "Hide Window", self.maiwindow)
        action_hide.setStatusTip("Hide the Application")
        action_hide.triggered.connect(self.func_action_hide)
        menu.addAction(action_hide)

        action_show = QAction()
        menu.addAction("Show Window")

        action_exit = QAction("Exit Application")
        action_exit.triggered.connect(self.app.quit) # type: ignore  # noqa: F821
        menu.addAction(action_exit)

        
        tray.setContextMenu(menu)
        
        tray.show()
        
    def func_action_exit(self) -> None:
        self.app.setQuitOnLastWindowClosed(True) 
        self.app.exit   
 
    def func_action_hide(self) -> None: 
        self.app.hide   
        
    