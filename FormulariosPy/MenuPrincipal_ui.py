# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formularios/MenuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FormulariosPy import imgHelado


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(838, 448)
        Form.setStyleSheet("background-color: rgb(104, 104, 104);")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 841, 101))
        self.widget_4.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(100, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(610, 0, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(610, 50, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(-9, 101, 851, 31))
        self.widget_5.setStyleSheet("\n"
"background-color: rgb(49, 0, 74);")
        self.widget_5.setObjectName("widget_5")
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(280, 0, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"")
        self.label_17.setObjectName("label_17")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 190, 111, 101))
        self.pushButton_3.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 370, 271, 31))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(49, 0, 74);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 190, 111, 101))
        self.pushButton_4.setStyleSheet("background-color: rgb(194, 194, 194);\n"
"\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 300, 111, 101))
        self.pushButton_7.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 300, 111, 101))
        self.pushButton_8.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 130, 441, 41))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(52, 52, 52);")
        self.widget.setObjectName("widget")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 0, 131, 41))
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 0, 127, 64), stop:0.482955 rgba(0, 0, 0, 255), stop:1 rgba(85, 0, 127, 108));")
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(143, 2, 161, 41))
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 0, 127, 64), stop:0.482955 rgba(0, 0, 0, 255), stop:1 rgba(85, 0, 127, 108));")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(-2, 2, 151, 41))
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 0, 127, 64), stop:0.482955 rgba(0, 0, 0, 255), stop:1 rgba(85, 0, 127, 108));")
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 230, 271, 141))
        self.label.setMinimumSize(QtCore.QSize(271, 141))
        self.label.setMaximumSize(QtCore.QSize(271, 141))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Helado/helado_extravagante.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.widget.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PRINCIPAL"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Ice Cream &quot;Faván”</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Manta - Manabí - Ecuador</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PERONAL O ADMIN</span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NOMBRE</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Menú Principal</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "REALIZAR PEDIDO"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Ice Cream &quot;Faván”</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "REPORTES"))
        self.pushButton_7.setText(_translate("Form", "SALIR"))
        self.pushButton_8.setText(_translate("Form", "CONSULTAS"))
        self.pushButton_10.setText(_translate("Form", "SUCURSAL"))
        self.pushButton_9.setText(_translate("Form", "PERSONAL"))
        self.pushButton_11.setText(_translate("Form", "CLIENTE"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><img src=\":/Helado/helado_extravagante.jpg\"/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
