# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet("background-color: rgb(209, 209, 209);")

        MainWindow.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Use a horizontal layout to manage the navigation and pages
        self.mainLayout = QHBoxLayout(self.centralwidget)

        # Expanded Navigation Section
        self.ExpandedNav = QWidget(self.centralwidget)
        self.ExpandedNav.setObjectName("ExpandedNav")
        self.ExpandedNav.setStyleSheet("QWidget{background-color: rgb(255, 255, 255);border-radius: 10px;width: 200;text-align: left;}")

        button_style = """
        QPushButton {
            text-align: left;
            height: 30px;
            border: none;
            padding-left: 10px;
            background-color: rgb(255, 255, 255);
            color: rgb(0, 0, 0);  
        }

        QPushButton:hover {
            background-color: rgb(255, 255, 255);  
            color: #c8c8c8;
            font-size: 25px;  
        }
        """

        self.verticalLayout = QVBoxLayout(self.ExpandedNav)

        font = QFont("Arial Rounded MT", 12)

        self.Xpand = QPushButton(self.ExpandedNav)
        menu_icon = QIcon("Assets/menu.png")
        self.Xpand.setIcon(menu_icon)
        icon_size = QSize(30, 30)
        self.Xpand.setIconSize(icon_size)
        self.Xpand.setFont(font)
        self.verticalLayout.addWidget(self.Xpand)

        # Monitor Button with Icon
        self.MonitorExpand = QPushButton(" Monitor ", self.ExpandedNav)
        icon1 = QIcon("Assets/Monitor.png")  # Update this path to your icon's location
        self.MonitorExpand.setFont(font)
        self.MonitorExpand.setIcon(icon1)
        self.MonitorExpand.setCheckable(True)
        self.MonitorExpand.setAutoExclusive(True)
        self.verticalLayout.addWidget(self.MonitorExpand)

        # Defend Button with Icon
        self.DefendExpand = QPushButton(" System Analysis", self.ExpandedNav)
        icon2 = QIcon("Assets/Analysis.png")  # Update this path to your icon's location
        self.DefendExpand.setFont(font)
        self.DefendExpand.setIcon(icon2)
        self.DefendExpand.setCheckable(True)
        self.DefendExpand.setAutoExclusive(True)
        self.verticalLayout.addWidget(self.DefendExpand)

        # Analysis Button with Icon
        self.AnalysisExpand = QPushButton(" Defend", self.ExpandedNav)
        icon3 = QIcon("Assets/Defend.png")  # Update this path to your icon's location
        self.AnalysisExpand.setFont(font)
        self.AnalysisExpand.setIcon(icon3)
        self.AnalysisExpand.setCheckable(True)
        self.AnalysisExpand.setAutoExclusive(True)
        self.verticalLayout.addWidget(self.AnalysisExpand)

        self.MonitorExpand.setStyleSheet(button_style)
        self.DefendExpand.setStyleSheet(button_style)
        self.AnalysisExpand.setStyleSheet(button_style)

        self.verticalLayout.setSpacing(5)  # Decreased space between buttons
        self.verticalLayout.setAlignment(Qt.AlignTop)
        self.mainLayout.addWidget(self.ExpandedNav)

        # Pages Section
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName("Pages")
        self.Pages.setStyleSheet(
            "background-color: rgb(255, 255, 255); border-radius: 10px;"
        )

        self.MonitroPage = QWidget()
        self.MonitroPage.setObjectName("MonitroPage")
        self.Pages.addWidget(self.MonitroPage)

        self.AnalysisPage = QWidget()
        self.AnalysisPage.setObjectName("AnalysisPage")
        self.Pages.addWidget(self.AnalysisPage)

        self.mainLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
