# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 506)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setBackground(1, QtGui.QColor(255, 255, 255))
        self.treeWidget.headerItem().setBackground(2, QtGui.QColor(255, 255, 255))
        self.verticalLayout.addWidget(self.treeWidget)
        self.label_16 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Surname_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Surname_LineEdit.sizePolicy().hasHeightForWidth())
        self.Surname_LineEdit.setSizePolicy(sizePolicy)
        self.Surname_LineEdit.setObjectName("Surname_LineEdit")
        self.gridLayout_3.addWidget(self.Surname_LineEdit, 2, 2, 1, 1)
        self.DoB_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DoB_LineEdit.sizePolicy().hasHeightForWidth())
        self.DoB_LineEdit.setSizePolicy(sizePolicy)
        self.DoB_LineEdit.setObjectName("DoB_LineEdit")
        self.gridLayout_3.addWidget(self.DoB_LineEdit, 3, 2, 1, 1)
        self.FirstName_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FirstName_LineEdit.sizePolicy().hasHeightForWidth())
        self.FirstName_LineEdit.setSizePolicy(sizePolicy)
        self.FirstName_LineEdit.setObjectName("FirstName_LineEdit")
        self.gridLayout_3.addWidget(self.FirstName_LineEdit, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.Address_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Address_LineEdit.sizePolicy().hasHeightForWidth())
        self.Address_LineEdit.setSizePolicy(sizePolicy)
        self.Address_LineEdit.setObjectName("Address_LineEdit")
        self.gridLayout_3.addWidget(self.Address_LineEdit, 4, 2, 1, 1)
        self.PhoneNumber_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhoneNumber_LineEdit.sizePolicy().hasHeightForWidth())
        self.PhoneNumber_LineEdit.setSizePolicy(sizePolicy)
        self.PhoneNumber_LineEdit.setObjectName("PhoneNumber_LineEdit")
        self.gridLayout_3.addWidget(self.PhoneNumber_LineEdit, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 7, 0, 1, 1)
        self.Email_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Email_LineEdit.sizePolicy().hasHeightForWidth())
        self.Email_LineEdit.setSizePolicy(sizePolicy)
        self.Email_LineEdit.setObjectName("Email_LineEdit")
        self.gridLayout_3.addWidget(self.Email_LineEdit, 7, 2, 1, 1)
        self.Postcode_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Postcode_LineEdit.sizePolicy().hasHeightForWidth())
        self.Postcode_LineEdit.setSizePolicy(sizePolicy)
        self.Postcode_LineEdit.setObjectName("Postcode_LineEdit")
        self.gridLayout_3.addWidget(self.Postcode_LineEdit, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.Add_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add_button.sizePolicy().hasHeightForWidth())
        self.Add_button.setSizePolicy(sizePolicy)
        self.Add_button.setObjectName("Add_button")
        self.gridLayout_3.addWidget(self.Add_button, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ClientID_LineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClientID_LineEdit.sizePolicy().hasHeightForWidth())
        self.ClientID_LineEdit.setSizePolicy(sizePolicy)
        self.ClientID_LineEdit.setObjectName("ClientID_LineEdit")
        self.gridLayout_2.addWidget(self.ClientID_LineEdit, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.Delete_Button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete_Button.sizePolicy().hasHeightForWidth())
        self.Delete_Button.setSizePolicy(sizePolicy)
        self.Delete_Button.setObjectName("Delete_Button")
        self.gridLayout_2.addWidget(self.Delete_Button, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.verticalLayout_2.addWidget(self.treeWidget_2)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Location_AppointmentLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.Location_AppointmentLineEdit.setObjectName("Location_AppointmentLineEdit")
        self.gridLayout_4.addWidget(self.Location_AppointmentLineEdit, 4, 3, 1, 1)
        self.Book_Button = QtWidgets.QPushButton(self.tab_4)
        self.Book_Button.setObjectName("Book_Button")
        self.gridLayout_4.addWidget(self.Book_Button, 6, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 4, 1, 1, 1)
        self.ClientID_AppointmentLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.ClientID_AppointmentLineEdit.setObjectName("ClientID_AppointmentLineEdit")
        self.gridLayout_4.addWidget(self.ClientID_AppointmentLineEdit, 0, 3, 1, 1)
        self.Surname_AppointmentLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.Surname_AppointmentLineEdit.setObjectName("Surname_AppointmentLineEdit")
        self.gridLayout_4.addWidget(self.Surname_AppointmentLineEdit, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 1, 1, 1)
        self.Date_AppointmentLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.Date_AppointmentLineEdit.setObjectName("Date_AppointmentLineEdit")
        self.gridLayout_4.addWidget(self.Date_AppointmentLineEdit, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)
        self.Time_AppointmentLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.Time_AppointmentLineEdit.setObjectName("Time_AppointmentLineEdit")
        self.gridLayout_4.addWidget(self.Time_AppointmentLineEdit, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Date_LineEdit2 = QtWidgets.QLineEdit(self.tab_4)
        self.Date_LineEdit2.setObjectName("Date_LineEdit2")
        self.gridLayout_6.addWidget(self.Date_LineEdit2, 1, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.Delete_Button2 = QtWidgets.QPushButton(self.tab_4)
        self.Delete_Button2.setObjectName("Delete_Button2")
        self.gridLayout_6.addWidget(self.Delete_Button2, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)
        self.Time_LineEdit2 = QtWidgets.QLineEdit(self.tab_4)
        self.Time_LineEdit2.setObjectName("Time_LineEdit2")
        self.gridLayout_6.addWidget(self.Time_LineEdit2, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Window"))
        self.label_17.setText(_translate("Dialog", "Client Data"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "Client ID"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Surname"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "First Name"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "Date of Birth"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "Address Line 1"))
        self.treeWidget.headerItem().setText(5, _translate("Dialog", "Address Line 2"))
        self.treeWidget.headerItem().setText(6, _translate("Dialog", "Postcode"))
        self.treeWidget.headerItem().setText(7, _translate("Dialog", "Phone Number"))
        self.treeWidget.headerItem().setText(8, _translate("Dialog", "Email"))
        self.label_16.setText(_translate("Dialog", "Add new client: (Enter all data in the format shown below)"))
        self.Surname_LineEdit.setPlaceholderText(_translate("Dialog", "Jackson"))
        self.DoB_LineEdit.setPlaceholderText(_translate("Dialog", "03/03/1998"))
        self.FirstName_LineEdit.setPlaceholderText(_translate("Dialog", "Alex"))
        self.label_14.setText(_translate("Dialog", "First Name:"))
        self.Address_LineEdit.setPlaceholderText(_translate("Dialog", "13 elm street"))
        self.PhoneNumber_LineEdit.setPlaceholderText(_translate("Dialog", "07346 346236"))
        self.label_15.setText(_translate("Dialog", "Email:"))
        self.Email_LineEdit.setPlaceholderText(_translate("Dialog", "alex@email.com"))
        self.Postcode_LineEdit.setPlaceholderText(_translate("Dialog", "B85 3Y9"))
        self.label_2.setText(_translate("Dialog", "Client ID:"))
        self.label_13.setText(_translate("Dialog", "Phone Number:"))
        self.label_9.setText(_translate("Dialog", "Postcode:"))
        self.label_12.setText(_translate("Dialog", "Address line 1:"))
        self.label_10.setText(_translate("Dialog", "Date of Birth:"))
        self.label_11.setText(_translate("Dialog", "Surname:"))
        self.Add_button.setText(_translate("Dialog", "Add"))
        self.label_5.setText(_translate("Dialog", "(This will be created for you and automatically stored in the above database.)"))
        self.label_7.setText(_translate("Dialog", "Delete a client:"))
        self.label_8.setText(_translate("Dialog", "Client ID:"))
        self.Delete_Button.setText(_translate("Dialog", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Client Data"))
        self.label.setText(_translate("Dialog", "Appointments"))
        self.treeWidget_2.headerItem().setText(0, _translate("Dialog", "Client ID"))
        self.treeWidget_2.headerItem().setText(1, _translate("Dialog", "Surname"))
        self.treeWidget_2.headerItem().setText(2, _translate("Dialog", "Date"))
        self.treeWidget_2.headerItem().setText(3, _translate("Dialog", "Time"))
        self.treeWidget_2.headerItem().setText(4, _translate("Dialog", "Location"))
        self.label_3.setText(_translate("Dialog", "Book an Appointment (Enter all data in the formats shown below.)"))
        self.Location_AppointmentLineEdit.setPlaceholderText(_translate("Dialog", "B5G WY2"))
        self.Book_Button.setText(_translate("Dialog", "Book"))
        self.label_24.setText(_translate("Dialog", "Surname:"))
        self.label_23.setText(_translate("Dialog", "Date:"))
        self.label_22.setText(_translate("Dialog", "Location:"))
        self.ClientID_AppointmentLineEdit.setPlaceholderText(_translate("Dialog", "Ajack96493"))
        self.Surname_AppointmentLineEdit.setPlaceholderText(_translate("Dialog", "Jackson"))
        self.label_6.setText(_translate("Dialog", "Time:"))
        self.Date_AppointmentLineEdit.setPlaceholderText(_translate("Dialog", "29/09/2020"))
        self.label_4.setText(_translate("Dialog", "Client ID:"))
        self.Time_AppointmentLineEdit.setPlaceholderText(_translate("Dialog", "13:00"))
        self.label_19.setText(_translate("Dialog", "Delete an appointment:"))
        self.label_18.setText(_translate("Dialog", "Date:"))
        self.Delete_Button2.setText(_translate("Dialog", "Delete"))
        self.label_20.setText(_translate("Dialog", "Time:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Book Appointment"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
