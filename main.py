#!/usr/bin/env python3
# coding: utf-8

import sys
# import qdarktheme
import traceback

from PySide6.QtWidgets import QApplication

from main.mainwindow import MainWindow


def main() -> None:
    try:
        app = QApplication(sys.argv)

        window = MainWindow(app)
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
