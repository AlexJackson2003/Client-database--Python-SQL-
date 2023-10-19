import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from LoginUIcode1 import *
import Main_Program

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class loginForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.SubmitButton.clicked.connect(self.submit)
        self.ui.AddButton.clicked.connect(self.add)
    
        c.execute("CREATE TABLE IF NOT EXISTS tbl_users(fld_Username TEXT,fld_Password TEXT)")
            
    def submit(self):
        username = self.ui.USERNAME_LineEdit.text()
        password = self.ui.PASSWORD_LineEdit.text()
        count = 0
        var_select = []
        var_select.append(username)
        var_select.append(password)
        with sqlite3.connect('Database.db') as db:
            cursor = db.cursor()
            sql = 'SELECT * FROM tbl_users WHERE fld_Username =? AND fld_Password = ?';
            cursor.execute(sql, var_select)
            result = cursor.fetchall()
            for row in result:
                global var_UID
                var_UID = (row[0])
                count = count +1
                        
    
        if count > 0:
            QMessageBox.information(self, 'Welcome', "You are now logged in", QMessageBox.Ok)
            self.w = Main_Program.MainWindow()
            self.w.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Error', "Login Details Incorrect", QMessageBox.Ok)
            
    def add(self):
        adminpass = "jackson123"
        NewUser = self.ui.NewUser_LineEdit.text()
        NewPassword = self.ui.NewPassword_LineEdit.text()
        ConfirmPassword = self.ui.ConfirmPassword_LineEdit.text()
        AdminPassword = self.ui.AdminPassword_LineEdit.text()
        if NewPassword == ConfirmPassword and AdminPassword == adminpass:
            var_insert = []
            var_insert.append(NewUser)
            var_insert.append(NewPassword)
            with sqlite3.connect('Database.db') as db:
                cursor = db.cursor()
                cursor.execute('insert INTO tbl_users (fld_Username, fld_Password)VALUES(?,?);', var_insert)
                db.commit()
                QMessageBox.information(self, 'Welcome', "You are now a user, Please log in.", QMessageBox.Ok)
        
            with sqlite3.connect('Database.db') as db:
                sql = 'SELECT * FROM tbl_users WHERE fld_Username =? AND fld_Password = ?';
                cursor.execute(sql, var_insert)
                result = cursor.fetchall()
                for row in result:
                    global var_UID
                    var_UID = (row[0])
        elif NewPassword != ConfirmPassword:
            QMessageBox.warning(self, 'Error', "Passwords do not match.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Error', "Admin Password wrong. You are not authorised to enter.", QMessageBox.Ok)
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = loginForm()
    w.show()
    sys.exit(app.exec_())
