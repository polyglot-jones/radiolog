# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nonRadioClueDialog.ui'
#
# Created: Sat Aug  1 20:56:36 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nonRadioClueDialog(object):
    def setupUi(self, nonRadioClueDialog):
        nonRadioClueDialog.setObjectName("nonRadioClueDialog")
        nonRadioClueDialog.resize(721, 572)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        nonRadioClueDialog.setFont(font)
        self.label_4 = QtWidgets.QLabel(nonRadioClueDialog)
        self.label_4.setGeometry(QtCore.QRect(40, 450, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.buttonBox = QtWidgets.QDialogButtonBox(nonRadioClueDialog)
        self.buttonBox.setGeometry(QtCore.QRect(540, 510, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(nonRadioClueDialog)
        self.label_3.setGeometry(QtCore.QRect(50, 400, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(nonRadioClueDialog)
        self.label.setGeometry(QtCore.QRect(0, 170, 151, 37))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(nonRadioClueDialog)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.clueNumberField = QtWidgets.QLineEdit(nonRadioClueDialog)
        self.clueNumberField.setGeometry(QtCore.QRect(640, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clueNumberField.setFont(font)
        self.clueNumberField.setObjectName("clueNumberField")
        self.label_6 = QtWidgets.QLabel(nonRadioClueDialog)
        self.label_6.setGeometry(QtCore.QRect(560, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(nonRadioClueDialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 601, 81))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.callsignField = QtWidgets.QLineEdit(self.groupBox)
        self.callsignField.setEnabled(True)
        self.callsignField.setGeometry(QtCore.QRect(330, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.callsignField.setFont(font)
        self.callsignField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.callsignField.setAutoFillBackground(False)
        self.callsignField.setText("")
        self.callsignField.setClearButtonEnabled(False)
        self.callsignField.setObjectName("callsignField")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(370, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(190, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.timeField = QtWidgets.QLineEdit(self.groupBox)
        self.timeField.setEnabled(True)
        self.timeField.setGeometry(QtCore.QRect(180, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.timeField.setFont(font)
        self.timeField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.timeField.setText("")
        self.timeField.setObjectName("timeField")
        self.dateField = QtWidgets.QLineEdit(self.groupBox)
        self.dateField.setEnabled(True)
        self.dateField.setGeometry(QtCore.QRect(30, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dateField.setFont(font)
        self.dateField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateField.setText("")
        self.dateField.setObjectName("dateField")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(40, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.clueReportPrintCheckBox = QtWidgets.QCheckBox(nonRadioClueDialog)
        self.clueReportPrintCheckBox.setGeometry(QtCore.QRect(150, 520, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clueReportPrintCheckBox.setFont(font)
        self.clueReportPrintCheckBox.setChecked(True)
        self.clueReportPrintCheckBox.setObjectName("clueReportPrintCheckBox")
        self.label_8 = QtWidgets.QLabel(nonRadioClueDialog)
        self.label_8.setGeometry(QtCore.QRect(30, 300, 661, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(nonRadioClueDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 300, 661, 201))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.instructionsField = QtWidgets.QLineEdit(self.groupBox_2)
        self.instructionsField.setGeometry(QtCore.QRect(160, 160, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.instructionsField.setFont(font)
        self.instructionsField.setText("")
        self.instructionsField.setObjectName("instructionsField")
        self.locationField = QtWidgets.QLineEdit(self.groupBox_2)
        self.locationField.setGeometry(QtCore.QRect(160, 110, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.locationField.setFont(font)
        self.locationField.setObjectName("locationField")
        self.descriptionField = QtWidgets.QPlainTextEdit(nonRadioClueDialog)
        self.descriptionField.setGeometry(QtCore.QRect(163, 166, 531, 121))
        self.descriptionField.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.descriptionField.setObjectName("descriptionField")

        self.retranslateUi(nonRadioClueDialog)
        self.buttonBox.accepted.connect(nonRadioClueDialog.accept)
        self.buttonBox.rejected.connect(nonRadioClueDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(nonRadioClueDialog)
        nonRadioClueDialog.setTabOrder(self.clueNumberField, self.dateField)
        nonRadioClueDialog.setTabOrder(self.dateField, self.timeField)
        nonRadioClueDialog.setTabOrder(self.timeField, self.callsignField)
        nonRadioClueDialog.setTabOrder(self.callsignField, self.descriptionField)
        nonRadioClueDialog.setTabOrder(self.descriptionField, self.locationField)
        nonRadioClueDialog.setTabOrder(self.locationField, self.instructionsField)
        nonRadioClueDialog.setTabOrder(self.instructionsField, self.clueReportPrintCheckBox)

    def retranslateUi(self, nonRadioClueDialog):
        _translate = QtCore.QCoreApplication.translate
        nonRadioClueDialog.setWindowTitle(_translate("nonRadioClueDialog", "Clue Report"))
        self.label_4.setText(_translate("nonRadioClueDialog", "Instructions"))
        self.label_3.setText(_translate("nonRadioClueDialog", "Location"))
        self.label.setText(_translate("nonRadioClueDialog", "Description"))
        self.label_2.setText(_translate("nonRadioClueDialog", "Non-Radio Clue Report"))
        self.label_6.setText(_translate("nonRadioClueDialog", "Clue #"))
        self.label_5.setText(_translate("nonRadioClueDialog", "REPORTED BY"))
        self.label_7.setText(_translate("nonRadioClueDialog", "TIME"))
        self.label_9.setText(_translate("nonRadioClueDialog", "DATE"))
        self.clueReportPrintCheckBox.setText(_translate("nonRadioClueDialog", "Print a Clue Report Form as soon as this clue is saved"))
        self.label_8.setText(_translate("nonRadioClueDialog", "Typically, \'Location\' and \'Instructions\' should be left blank.\n"
"All relevant data should be hand-written on this form after printing,\n"
"or on a separate paper or attachment."))

