import sys
import sqlite3
import random
from sqlite3 import Error
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from Run_From_Here import *
from MainUI import *

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.Add_button.clicked.connect(self.inputData)
        self.ui.Book_Button.clicked.connect(self.inputDataAppointments)
        self.ui.Delete_Button.clicked.connect(self.deleteDataClients)
        self.ui.Delete_Button2.clicked.connect(self.deleteAppointments)

        c.execute("CREATE TABLE IF NOT EXISTS tbl_clients(fld_ClientID TEXT,fld_FirstName TEXT, fld_Surname TEXT, fld_DoB TEXT, fld_Address TEXT, fld_Postcode TEXT, fld_PhoneNumber TEXT, fld_Email TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS tbl_appointments(fld_ClientID TEXT,fld_Surname TEXT,fld_Date TEXT,fld_Time TEXT,fld_Location TEXT)")

        with sqlite3.connect('Database.db') as db:
            cursor = db.cursor()
            self.ui.treeWidget_2.clear()
            cursor.execute('SELECT * FROM tbl_appointments')

            appointments = []
            [appointments.append(list(row)) for row in cursor.fetchall()]

            for appointment in appointments:
                item = QtWidgets.QTreeWidgetItem(appointment)
                self.ui.treeWidget_2.addTopLevelItem(item)

        with sqlite3.connect('Database.db') as db:
            cursor = db.cursor()
            self.ui.treeWidget.clear()
            cursor.execute('SELECT * FROM tbl_clients')

            clients = []
            [clients.append(list(row)) for row in cursor.fetchall()]

            for client in clients:
                item = QtWidgets.QTreeWidgetItem(client)
                self.ui.treeWidget.addTopLevelItem(item)

        for i in range(self.ui.treeWidget.columnCount()):
            self.ui.treeWidget.resizeColumnToContents(i)

        for i in range(self.ui.treeWidget_2.columnCount()):
            self.ui.treeWidget_2.resizeColumnToContents(i)


    def inputData(self):
        FirstName = self.ui.FirstName_LineEdit.text()
        Surname = self.ui.Surname_LineEdit.text()
        DoB = self.ui.DoB_LineEdit.text()
        Address = self.ui.Address_LineEdit.text()
        Postcode = self.ui.Postcode_LineEdit.text()
        PhoneNumber = self.ui.PhoneNumber_LineEdit.text()
        Email = self.ui.Email_LineEdit.text()
        
        if len(FirstName)>0 and len(Surname)>0 and len(DoB)>0 and len(Address)>0 and len(Postcode)>0 and len(PhoneNumber)>0 and len(Email)>0:
            Client_ID = FirstName.lower()[0] + Surname.lower()[0:4] + str(random.randint(10000,99999))
            var_insert = []
            var_insert.append(Client_ID)
            var_insert.append(FirstName)
            var_insert.append(Surname)
            var_insert.append(DoB)
            var_insert.append(Address)
            var_insert.append(Postcode)
            var_insert.append(PhoneNumber)
            var_insert.append(Email)

            
            with sqlite3.connect('Database.db') as db:
                cursor = db.cursor()
                cursor.execute('insert INTO tbl_clients(fld_ClientID, fld_FirstName, fld_Surname, fld_DoB, fld_Address, fld_Postcode, fld_PhoneNumber, fld_Email)VALUES(?,?,?,?,?,?,?,?);', var_insert)
                db.commit()
                self.ui.treeWidget.clear()
                cursor.execute('SELECT * FROM tbl_clients')

                clients = []
                [clients.append(list(row)) for row in cursor.fetchall()]

                for client in clients:
                    item = QtWidgets.QTreeWidgetItem(client)
                    self.ui.treeWidget.addTopLevelItem(item)
       
            with sqlite3.connect('Database.db') as db:
                cursor = db.cursor()
                sql = 'SELECT * FROM tbl_clients WHERE fld_ClientID =? AND fld_FirstName =? AND fld_Surname =? AND fld_DoB =? AND fld_Address =? AND fld_Postcode =? AND fld_PhoneNumber =? and fld_Email =?'
                cursor.execute(sql,var_insert)
                result = cursor.fetchall()
                for row in result:
                    global var_UID
                    var_UID = (row[0])
        else:
            QMessageBox.warning(self, 'Error', "Please enter all the required data.", QMessageBox.Ok)
        

        for i in range(self.ui.treeWidget.columnCount()):
            self.ui.treeWidget.resizeColumnToContents(i)

    def inputDataAppointments(self):
        ClientID = self.ui.ClientID_AppointmentLineEdit.text()
        Surname = self.ui.Surname_AppointmentLineEdit.text()
        Date = self.ui.Date_AppointmentLineEdit.text()
        Time = self.ui.Time_AppointmentLineEdit.text()
        Location = self.ui.Location_AppointmentLineEdit.text()
        var_insert = []
        var_insert.append(ClientID)
        var_insert.append(Surname)
        var_insert.append(Date)
        var_insert.append(Time)
        var_insert.append(Location)

        if len(ClientID)>0 and len(Surname)>0 and len(Date)>0 and len(Time)>0 and len(Location)>0:
            with sqlite3.connect('Database.db') as db:
                cursor = db.cursor()
                cursor.execute('insert INTO tbl_appointments(fld_ClientID, fld_Surname, fld_Date, fld_Time, fld_Location)VALUES(?,?,?,?,?);', var_insert)
                db.commit()
                self.ui.treeWidget_2.clear()
                cursor.execute('SELECT * FROM tbl_appointments')

                appointments = []
                [appointments.append(list(row)) for row in cursor.fetchall()]

                for appointment in appointments:
                    item = QtWidgets.QTreeWidgetItem(appointment)
                    self.ui.treeWidget_2.addTopLevelItem(item)

                for i in range(self.ui.treeWidget_2.columnCount()):
                    self.ui.treeWidget_2.resizeColumnToContents(i)
            
            with sqlite3.connect('Database.db') as db:
                cursor = db.cursor()
                sql = 'SELECT * FROM tbl_appointments WHERE fld_ClientID =? AND fld_Surname =? AND fld_Date =? AND fld_Time =? AND fld_Location =?'
                cursor.execute(sql,var_insert)
                result = cursor.fetchall()
                for row in result:
                    global var_UID
                    var_UID = (row[0])

        else:
            QMessageBox.warning(self, 'Error', "Please enter all the required data.", QMessageBox.Ok)

    def deleteDataClients(self):
        ClientID2 = self.ui.ClientID_LineEdit.text()
        var_insert=[]
        var_insert.append(ClientID2)
        with sqlite3.connect('Database.db') as db:
            cursor = db.cursor()
            sql = 'DELETE FROM tbl_clients WHERE fld_ClientID = ?'
            cursor.execute(sql, var_insert)
            result = cursor.fetchall()
            for row in result:
                global var_UID
                var_UID = (row[0])

            self.ui.treeWidget.clear()
            cursor.execute('SELECT * FROM tbl_clients')

            clients = []
            [clients.append(list(row)) for row in cursor.fetchall()]

            for client in clients:
                item = QtWidgets.QTreeWidgetItem(client)
                self.ui.treeWidget.addTopLevelItem(item)
                
       
    def deleteAppointments(self):
        Date2 = self.ui.Date_LineEdit2.text()
        Time2 = self.ui.Time_LineEdit2.text()
        var_insert=[]
        var_insert.append(Date2)
        var_insert.append(Time2)
        with sqlite3.connect('Database.db') as db:
            cursor = db.cursor()
            sql = 'DELETE FROM tbl_appointments WHERE fld_Date = ? AND fld_Time = ?'
            cursor.execute(sql, var_insert)
            result = cursor.fetchall()
            for row in result:
                global var_UID
                var_UID = (row[0])

            self.ui.treeWidget_2.clear()
            cursor.execute('SELECT * FROM tbl_appointments')

            appointments = []
            [appointments.append(list(row)) for row in cursor.fetchall()]

            for appointment in appointments:
                item = QtWidgets.QTreeWidgetItem(appointment)
                self.ui.treeWidget_2.addTopLevelItem(item)
            


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
                



        
    
