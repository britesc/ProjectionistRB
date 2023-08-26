#!/usr/bin/env python3
# coding: utf-8

import sys
# import qdarktheme
import traceback

from PySide6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu,
)    

from PySide6.QtGui import (
    QAction,
    QIcon,
    QWindow,
)

from main.mainwindow import MainWindow

# trunk-ignore(ruff/F401)
import resources.buttonsGlassRound_rc

def main() -> None:  # sourcery skip: extract-method, remove-pass-body, remove-redundant-pass, swap-if-else-branches  # noqa: E501
    try:
        app = QApplication(sys.argv)
        window = MainWindow(app)
 
        if not QSystemTrayIcon.isSystemTrayAvailable():
            pass
        else:
    
            app.setQuitOnLastWindowClosed(False)        

            tray_icon = QIcon(u":/buttons/glassRound/glassButtonProjectionist.png")  # noqa: E501

            tray = QSystemTrayIcon()
            tray.setIcon(tray_icon)
            tray.setVisible(True)


            tray_menu = QMenu()
            action1 = QAction("Show")
            action1.triggered.connect(window.showNormal)
            action1.triggered.connect(window.activateWindow)
            action1.triggered.connect(window.raise_)
            action1.setIcon(QIcon(u":/buttons/glassRound/glassButtonProjectionist.png"))
            tray_menu.addAction(action1)

            action2 = QAction("Quit")
            action2.triggered.connect(app.quit)
            action2.setIcon(QIcon(u":/buttons/glassRound/glassButtonQuit.png"))
            tray_menu.addAction(action2)

            tray.setContextMenu(tray_menu)        
        
        window.show()

    except Exception as err:
        print("Unfortunately the Application has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        sys.exit(app.exec()) # type: ignore



if __name__ == '__main__':
    main()
    
