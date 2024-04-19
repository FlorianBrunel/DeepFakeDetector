# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledeZXUHa.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QToolBar, QWidget)

class Ui_DeepFakeDetector(object):
    def setupUi(self, DeepFakeDetector):
        if not DeepFakeDetector.objectName():
            DeepFakeDetector.setObjectName(u"DeepFakeDetector")
        DeepFakeDetector.resize(1181, 612)
        DeepFakeDetector.setMinimumSize(QSize(1181, 612))
        DeepFakeDetector.setMaximumSize(QSize(1181, 612))
        self.centralwidget = QWidget(DeepFakeDetector)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Title = QFrame(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 10, 1161, 101))
        self.Title.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(71, 71, 71);")
        self.Title.setFrameShape(QFrame.NoFrame)
        self.label = QLabel(self.Title)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 701, 21))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMidLineWidth(3)
        self.Legend = QLabel(self.Title)
        self.Legend.setObjectName(u"Legend")
        self.Legend.setEnabled(True)
        self.Legend.setGeometry(QRect(10, 30, 721, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.Legend.sizePolicy().hasHeightForWidth())
        self.Legend.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.Legend.setFont(font1)
        self.Legend.setAcceptDrops(False)
        self.Legend.setMidLineWidth(3)
        self.SelectMedia = QPushButton(self.Title)
        self.SelectMedia.setObjectName(u"SelectMedia")
        self.SelectMedia.setGeometry(QRect(950, 20, 201, 61))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.SelectMedia.setFont(font2)
        self.SelectMedia.setStyleSheet(u"color: rgb(125, 125, 125);")
        self.SelectMedia.setCheckable(False)
        self.SelectMedia.setAutoDefault(False)
        self.VideoImgAudio = QFrame(self.centralwidget)
        self.VideoImgAudio.setObjectName(u"VideoImgAudio")
        self.VideoImgAudio.setGeometry(QRect(10, 150, 1161, 371))
        self.VideoImgAudio.setStyleSheet(u"selection-background-color: rgb(167, 190, 255);")
        self.VideoImgAudio.setFrameShape(QFrame.NoFrame)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 120, 1151, 23))
        self.progressBar.setValue(24)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -170, 1251, 811))
        self.frame.setStyleSheet(u"background-color: rgb(159, 159, 159);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.SelectMedia_2 = QPushButton(self.frame)
        self.SelectMedia_2.setObjectName(u"SelectMedia_2")
        self.SelectMedia_2.setGeometry(QRect(20, 690, 1161, 51))
        self.SelectMedia_2.setFont(font2)
        self.SelectMedia_2.setCheckable(False)
        self.SelectMedia_2.setAutoDefault(False)
        DeepFakeDetector.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.Title.raise_()
        self.VideoImgAudio.raise_()
        self.progressBar.raise_()
        self.statusbar = QStatusBar(DeepFakeDetector)
        self.statusbar.setObjectName(u"statusbar")
        DeepFakeDetector.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(DeepFakeDetector)
        self.toolBar.setObjectName(u"toolBar")
        DeepFakeDetector.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(DeepFakeDetector)

        QMetaObject.connectSlotsByName(DeepFakeDetector)
    # setupUi

    def retranslateUi(self, DeepFakeDetector):
        DeepFakeDetector.setWindowTitle(QCoreApplication.translate("DeepFakeDetector", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("DeepFakeDetector", u"DeepFake Detector ", None))
        self.Legend.setText(QCoreApplication.translate("DeepFakeDetector", u"<html><head/><body><p>Vous pensez que vous \u00eates victime d'une tentative d'<span style=\" font-weight:700;\">escroquerie</span>, de <span style=\" font-weight:700;\">d\u00e9sinformation</span>, d<span style=\" font-weight:700;\">'</span><span style=\" font-weight:700;\">intimidation</span> ... ?<br/>Lancez une analyse afin d'en avoir le coeur net !</p></body></html>", None))
        self.SelectMedia.setText(QCoreApplication.translate("DeepFakeDetector", u"Selectionner un m\u00e9dia", None))
        self.SelectMedia_2.setText(QCoreApplication.translate("DeepFakeDetector", u"Lancez l'analyse", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("DeepFakeDetector", u"toolBar", None))
    # retranslateUi

from PyQt6.QtWidgets import QApplication

class DeepFakeDetector(QMainWindow, Ui_DeepFakeDetector):
    def __init__(self, parent=None):
        super(DeepFakeDetector, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = DeepFakeDetector()
    window.show()
    sys.exit(app.exec())