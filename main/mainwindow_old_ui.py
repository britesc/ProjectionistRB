# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_old.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)
import buttonsGlassRound_rc
import png_rc
import readfiles_rc
import splash_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(979, 639)
        icon = QIcon()
        icon.addFile(u":/Images/png/projectionist.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_1_Ribbon_Bar = QVBoxLayout()
        self.verticalLayout_1_Ribbon_Bar.setSpacing(0)
        self.verticalLayout_1_Ribbon_Bar.setObjectName(u"verticalLayout_1_Ribbon_Bar")
        self.horizontalLayout_1_Ribbon_Bar = QHBoxLayout()
        self.horizontalLayout_1_Ribbon_Bar.setSpacing(0)
        self.horizontalLayout_1_Ribbon_Bar.setObjectName(u"horizontalLayout_1_Ribbon_Bar")
        self.horizontalLayout_1_Ribbon_Bar.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_1_Master = QGroupBox(self.centralwidget)
        self.groupBox_1_Master.setObjectName(u"groupBox_1_Master")
        self.groupBox_1_Master.setAlignment(Qt.AlignCenter)
        self.groupBox_1_Master.setFlat(True)
        self.gridLayoutWidget = QWidget(self.groupBox_1_Master)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 161, 171))
        self.gridLayout_1_Master = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1_Master.setSpacing(0)
        self.gridLayout_1_Master.setObjectName(u"gridLayout_1_Master")
        self.gridLayout_1_Master.setContentsMargins(0, 0, 0, 0)
        self.label_Master_R3C2 = QLabel(self.gridLayoutWidget)
        self.label_Master_R3C2.setObjectName(u"label_Master_R3C2")
        self.label_Master_R3C2.setMinimumSize(QSize(32, 32))
        self.label_Master_R3C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R3C2, 3, 2, 1, 1)

        self.label_Master_R1C3 = QLabel(self.gridLayoutWidget)
        self.label_Master_R1C3.setObjectName(u"label_Master_R1C3")
        self.label_Master_R1C3.setMinimumSize(QSize(32, 32))
        self.label_Master_R1C3.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R1C3, 1, 3, 1, 1)

        self.pushButton_Master_R3C3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_Master_R3C3.setObjectName(u"pushButton_Master_R3C3")
        self.pushButton_Master_R3C3.setMinimumSize(QSize(32, 32))
        self.pushButton_Master_R3C3.setMaximumSize(QSize(32, 32))
        self.pushButton_Master_R3C3.setSizeIncrement(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/Images/png/arrowup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Master_R3C3.setIcon(icon1)
        self.pushButton_Master_R3C3.setFlat(True)

        self.gridLayout_1_Master.addWidget(self.pushButton_Master_R3C3, 3, 3, 1, 1)

        self.label_Master_R0C2 = QLabel(self.gridLayoutWidget)
        self.label_Master_R0C2.setObjectName(u"label_Master_R0C2")
        self.label_Master_R0C2.setMinimumSize(QSize(32, 32))
        self.label_Master_R0C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R0C2, 0, 2, 1, 1)

        self.label_Master_R1C2 = QLabel(self.gridLayoutWidget)
        self.label_Master_R1C2.setObjectName(u"label_Master_R1C2")
        self.label_Master_R1C2.setMinimumSize(QSize(32, 32))
        self.label_Master_R1C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R1C2, 1, 2, 1, 1)

        self.pushButton_Master_R0C3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_Master_R0C3.setObjectName(u"pushButton_Master_R0C3")
        self.pushButton_Master_R0C3.setMinimumSize(QSize(32, 32))
        self.pushButton_Master_R0C3.setMaximumSize(QSize(32, 32))
        self.pushButton_Master_R0C3.setSizeIncrement(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/Images/png/arrowdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Master_R0C3.setIcon(icon2)
        self.pushButton_Master_R0C3.setFlat(True)

        self.gridLayout_1_Master.addWidget(self.pushButton_Master_R0C3, 0, 3, 1, 1)

        self.label_Master_R2C2 = QLabel(self.gridLayoutWidget)
        self.label_Master_R2C2.setObjectName(u"label_Master_R2C2")
        self.label_Master_R2C2.setMinimumSize(QSize(32, 32))
        self.label_Master_R2C2.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R2C2, 2, 2, 1, 1)

        self.label_Master_R2C1 = QLabel(self.gridLayoutWidget)
        self.label_Master_R2C1.setObjectName(u"label_Master_R2C1")
        self.label_Master_R2C1.setMinimumSize(QSize(32, 32))
        self.label_Master_R2C1.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R2C1, 2, 1, 1, 1)

        self.label_Master_R3C0 = QLabel(self.gridLayoutWidget)
        self.label_Master_R3C0.setObjectName(u"label_Master_R3C0")
        self.label_Master_R3C0.setMinimumSize(QSize(32, 32))
        self.label_Master_R3C0.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R3C0, 3, 0, 1, 1)

        self.label_Master_R2C3 = QLabel(self.gridLayoutWidget)
        self.label_Master_R2C3.setObjectName(u"label_Master_R2C3")
        self.label_Master_R2C3.setMinimumSize(QSize(32, 32))
        self.label_Master_R2C3.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R2C3, 2, 3, 1, 1)

        self.label_Master_R3C1 = QLabel(self.gridLayoutWidget)
        self.label_Master_R3C1.setObjectName(u"label_Master_R3C1")
        self.label_Master_R3C1.setMinimumSize(QSize(32, 32))
        self.label_Master_R3C1.setMaximumSize(QSize(32, 32))

        self.gridLayout_1_Master.addWidget(self.label_Master_R3C1, 3, 1, 1, 1)

        self.pushButton_Master_R0C0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_Master_R0C0.setObjectName(u"pushButton_Master_R0C0")
        self.pushButton_Master_R0C0.setMinimumSize(QSize(64, 64))
        self.pushButton_Master_R0C0.setMaximumSize(QSize(64, 64))
        self.pushButton_Master_R0C0.setAutoFillBackground(False)
        self.pushButton_Master_R0C0.setIcon(icon)
        self.pushButton_Master_R0C0.setIconSize(QSize(64, 64))
        self.pushButton_Master_R0C0.setFlat(True)

        self.gridLayout_1_Master.addWidget(self.pushButton_Master_R0C0, 0, 0, 2, 2)

        self.pushButton_Master_B2C0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_Master_B2C0.setObjectName(u"pushButton_Master_B2C0")
        self.pushButton_Master_B2C0.setMinimumSize(QSize(32, 32))
        self.pushButton_Master_B2C0.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/buttons/glassRound/glassButtonHelp2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Master_B2C0.setIcon(icon3)
        self.pushButton_Master_B2C0.setIconSize(QSize(24, 24))
        self.pushButton_Master_B2C0.setFlat(True)

        self.gridLayout_1_Master.addWidget(self.pushButton_Master_B2C0, 2, 0, 1, 1)


        self.horizontalLayout_1_Ribbon_Bar.addWidget(self.groupBox_1_Master)

        self.groupBox_2_Tabs = QGroupBox(self.centralwidget)
        self.groupBox_2_Tabs.setObjectName(u"groupBox_2_Tabs")
        self.tabWidget_Ribbon_Bar = QTabWidget(self.groupBox_2_Tabs)
        self.tabWidget_Ribbon_Bar.setObjectName(u"tabWidget_Ribbon_Bar")
        self.tabWidget_Ribbon_Bar.setGeometry(QRect(6, -1, 791, 171))
        self.tabWidget_Ribbon_Bar.setMinimumSize(QSize(0, 140))
        self.tab_1_Home = QWidget()
        self.tab_1_Home.setObjectName(u"tab_1_Home")
        self.tab_1_Home.setMinimumSize(QSize(0, 0))
        self.groupBox_T1B1 = QGroupBox(self.tab_1_Home)
        self.groupBox_T1B1.setObjectName(u"groupBox_T1B1")
        self.groupBox_T1B1.setGeometry(QRect(10, 0, 181, 133))
        self.groupBox_T1B1.setMinimumSize(QSize(0, 133))
        self.groupBox_T1B1.setMaximumSize(QSize(16777215, 133))
        self.groupBox_T1B1.setSizeIncrement(QSize(0, 0))
        self.groupBox_T1B1.setAlignment(Qt.AlignCenter)
        self.groupBox_T1B1.setFlat(False)
        self.groupBox_T1B1.setCheckable(False)
        self.pushButton_2 = QPushButton(self.groupBox_T1B1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 110, 181, 25))
        self.groupBox_T1B2 = QGroupBox(self.tab_1_Home)
        self.groupBox_T1B2.setObjectName(u"groupBox_T1B2")
        self.groupBox_T1B2.setGeometry(QRect(200, 0, 181, 133))
        self.groupBox_T1B2.setMinimumSize(QSize(0, 133))
        self.groupBox_T1B2.setMaximumSize(QSize(16777215, 133))
        self.groupBox_T1B2.setSizeIncrement(QSize(0, 0))
        self.groupBox_T1B2.setAlignment(Qt.AlignCenter)
        self.groupBox_T1B2.setFlat(False)
        self.groupBox_T1B2.setCheckable(False)
        self.pushButton = QPushButton(self.groupBox_T1B2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 110, 181, 25))
        self.tabWidget_Ribbon_Bar.addTab(self.tab_1_Home, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_Ribbon_Bar.addTab(self.tab_2, "")

        self.horizontalLayout_1_Ribbon_Bar.addWidget(self.groupBox_2_Tabs)

        self.horizontalLayout_1_Ribbon_Bar.setStretch(0, 3)
        self.horizontalLayout_1_Ribbon_Bar.setStretch(1, 15)

        self.verticalLayout_1_Ribbon_Bar.addLayout(self.horizontalLayout_1_Ribbon_Bar)


        self.verticalLayout.addLayout(self.verticalLayout_1_Ribbon_Bar)

        self.verticalLayout_2_Main = QVBoxLayout()
        self.verticalLayout_2_Main.setObjectName(u"verticalLayout_2_Main")
        self.horizontalLayout_1_Main = QHBoxLayout()
        self.horizontalLayout_1_Main.setObjectName(u"horizontalLayout_1_Main")
        self.stackedWidget_Main = QStackedWidget(self.centralwidget)
        self.stackedWidget_Main.setObjectName(u"stackedWidget_Main")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_Main.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_Main.addWidget(self.page_2)

        self.horizontalLayout_1_Main.addWidget(self.stackedWidget_Main)


        self.verticalLayout_2_Main.addLayout(self.horizontalLayout_1_Main)


        self.verticalLayout.addLayout(self.verticalLayout_2_Main)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Projectionist", None))
        self.groupBox_1_Master.setTitle("")
        self.label_Master_R3C2.setText(QCoreApplication.translate("MainWindow", u"R3C2", None))
        self.label_Master_R1C3.setText(QCoreApplication.translate("MainWindow", u"R1C3", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Master_R3C3.setToolTip(QCoreApplication.translate("MainWindow", u"Reduce Ribbon Bar  (Shift +Up Arrow)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_Master_R3C3.setStatusTip(QCoreApplication.translate("MainWindow", u"Reduce Ribbon Bar  (Shift +Up Arrow)", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Master_R3C3.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Master_R3C3.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Up", None))
#endif // QT_CONFIG(shortcut)
        self.label_Master_R0C2.setText(QCoreApplication.translate("MainWindow", u"R0C2", None))
        self.label_Master_R1C2.setText(QCoreApplication.translate("MainWindow", u"R1C2", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Master_R0C3.setToolTip(QCoreApplication.translate("MainWindow", u"Expand Ribbon Bar  (Shift +Down Arrow)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_Master_R0C3.setStatusTip(QCoreApplication.translate("MainWindow", u"Expand Ribbon Bar  (Shift +Down Arrow)", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Master_R0C3.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Master_R0C3.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Down", None))
#endif // QT_CONFIG(shortcut)
        self.label_Master_R2C2.setText(QCoreApplication.translate("MainWindow", u"R2C2", None))
        self.label_Master_R2C1.setText(QCoreApplication.translate("MainWindow", u"R2C1", None))
        self.label_Master_R3C0.setText(QCoreApplication.translate("MainWindow", u"R3C0", None))
        self.label_Master_R2C3.setText(QCoreApplication.translate("MainWindow", u"R2C3", None))
        self.label_Master_R3C1.setText(QCoreApplication.translate("MainWindow", u"R3C1", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Master_R0C0.setToolTip(QCoreApplication.translate("MainWindow", u"Logo Menu (Shift +L)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_Master_R0C0.setStatusTip(QCoreApplication.translate("MainWindow", u"Logo Menu (Shift +L)", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Master_R0C0.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Master_R0C0.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+L", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_Master_B2C0.setToolTip(QCoreApplication.translate("MainWindow", u"Help (F1)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_Master_B2C0.setStatusTip(QCoreApplication.translate("MainWindow", u"Help (F1)", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Master_B2C0.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Master_B2C0.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2_Tabs.setTitle("")
        self.groupBox_T1B1.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox_T1B2.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget_Ribbon_Bar.setTabText(self.tabWidget_Ribbon_Bar.indexOf(self.tab_1_Home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidget_Ribbon_Bar.setTabText(self.tabWidget_Ribbon_Bar.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

