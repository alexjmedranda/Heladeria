# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formularios/Clientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import FormulariosPy.xz_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 627)
        Form.setStyleSheet("background-color: rgb(206, 196, 255);")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 721, 91))
        self.widget_4.setStyleSheet("background-color: rgb(85, 0, 127);")
        self.widget_4.setObjectName("widget_4")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(230, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 100, 721, 41))
        self.textBrowser.setStyleSheet("background-color: rgb(49, 0, 74);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 110, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(49, 0, 74);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 160, 841, 521))
        self.frame.setStyleSheet("background-color: rgb(206, 196, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 0, 701, 241))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 160, 121, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 130, 121, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(510, 100, 121, 31))
        self.pushButton.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 180, 231, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 156, 231, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(150, 131, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 130, 231, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(170, 161, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 106, 231, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(160, 181, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(170, 81, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 81, 151, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(160, 111, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 10, 121, 21))
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 0, 31, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"image: url(:/prefijoNuevo/buscar.ico);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(50, 10, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox.setFont(font)
        self.checkBox.setWhatsThis("")
        self.checkBox.setStyleSheet("font: 75 10pt \"Georgia\";")
        self.checkBox.setObjectName("checkBox")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 701, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(731, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 240, 101, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 240, 101, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(49, 0, 74);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(110, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(49, 0, 74);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.frame.raise_()
        self.widget_4.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_10.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CLIENTES"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Ice Cream &quot;Faván”</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Manta - Manabí - Ecuador</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Datos Personales</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "Eliminar"))
        self.pushButton_3.setText(_translate("Form", "Editar"))
        self.pushButton.setText(_translate("Form", "Guardar"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Apellidos:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Correo:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Teléfono:</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Cédula:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Nombres:</span></p></body></html>"))
        self.checkBox.setText(_translate("Form", "Id"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "CÉDULA"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "NOMBRE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "APELLIDO"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "CORREO"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "TELÉFONO"))
        self.pushButton_2.setText(_translate("Form", "Reporte"))
        self.pushButton_5.setText(_translate("Form", "Actualizar"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Cliente:</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">00000</span></p></body></html>"))
#import rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
