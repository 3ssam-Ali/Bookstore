import sys
import datetime
from peewee import *
from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from Ui_Bookstore import Ui_BookStore
from Ui_Login import Ui_LoginWindow
from Ui_AddClient import Ui_Form
from databaseModels import *


# qtCreatorFile = "Bookstore.ui" # Enter file here.

# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_BookStore):

    def __init__(self,admin='False'):
        QtWidgets.QMainWindow.__init__(self)
        Ui_BookStore.__init__(self)

        self.setupUi(self)
        self.tabWidget.tabBar().setVisible(False)
        #-----button configeration-----#
        self.OperationsBtn.clicked.connect(self.switchToOP)
        self.StockBtn.clicked.connect(self.switchToStock)
        self.ClientsBtn.clicked.connect(self.switchToClient)
        self.ReportBtn.clicked.connect(self.switchToReport)
        self.SettingsBtn.clicked.connect(self.switchToSettings)
        self.Logoutbtn.clicked.connect(self.log_out)
        #---Main window---#
        self.addClientbtn.clicked.connect(self.addclient)
        self.addOPbtn_2.clicked.connect(self.addSale)
        self.addOPbtn.clicked.connect(self.addRequest)
        # ---Stock---#+
        self.pushButton_2.clicked.connect(self.FilterStock)
        self.pushButton_10.clicked.connect(self.Addbook)
        self.pushButton_13.clicked.connect(self.Deletebook)
        self.pushButton_11.clicked.connect(self.Savebook)
        self.pushButton_12.clicked.connect(self.search_Book_database)
        #---clients and suppliers---#
        self.pushButton_14.clicked.connect(self.fill_Client_table)
        self.pushButton_17.clicked.connect(self.search_Client_database)
        self.pushButton_16.clicked.connect(self.Save_client_data)
        self.pushButton_18.clicked.connect(self.Delete_client_data)
        #####
        self.pushButton_26.clicked.connect(self.search_Supplier_database)
        self.pushButton_19.clicked.connect(self.Save_Supplier_data)
        self.pushButton_25.clicked.connect(self.Delete_Supplier_data)
        #---report---#
        self.pushButton_24.clicked.connect(self.FilterReport)
        self.pushButton_41.clicked.connect(self.MakeReport)
        #---Requests---#
        self.pushButton.clicked.connect(self.SendRequest)
        self.pushButton_3.clicked.connect(self.RemoveRequest)
        #---settings---#
        # data
        self.pushButton_23.clicked.connect(self.Add_supplier)
        self.pushButton_20.clicked.connect(self.Add_publisher)
        self.pushButton_22.clicked.connect(self.Add_category)
        self.pushButton_27.clicked.connect(self.delete_category)
        # Employee
        self.pushButton_30.clicked.connect(self.Add_employee)
        self.pushButton_31.clicked.connect(self.save_employee_data)
        self.pushButton_32.clicked.connect(self.Check_data)
        self.pushButton_33.clicked.connect(self.delete_employee)

        if admin=='False':
            self.tab.setEnabled(False)
            self.tab_15.setEnabled(False)

        self.refresh()
        self.show_Book_view()
        self.show_Old_operation()
        
        self.fill_requests()
        
        self.refreshClients.clicked.connect(self.refresh)

    #-----------------Functions--------------------#

    def show_Old_operation(self):
        for sale in Sale.select().where(Sale.op_time.day == datetime.date.today().day):
            self.tableWidget.insertRow(0)
            try:
                self.tableWidget.setItem(
                    0, 0, QTableWidgetItem(str(sale.book.id)))
            except:
                pass
            self.tableWidget.setItem(
                0, 1, QTableWidgetItem(str(sale.book_name)))
            try:
                self.tableWidget.setItem(
                    0, 2, QTableWidgetItem(str(sale.book.category.name)))
            except:
                pass
            self.tableWidget.setItem(0, 3, QTableWidgetItem('sale'))
            self.tableWidget.setItem(0, 4, QTableWidgetItem(str(sale.id)))
            self.tableWidget.setItem(0, 5, QTableWidgetItem(str(sale.client)))
            self.tableWidget.setItem(0, 6, QTableWidgetItem(str(sale.price)))
            self.tableWidget.setItem(
                0, 7, QTableWidgetItem(str(sale.quantity)))
            self.tableWidget.setItem(0, 8, QTableWidgetItem(str(sale.op_time)))

    def show_Book_view(self):
        self.BookstableWidget.clearContents()
        query = Book.select().where(Book.name.contains(self.BookNameField.text()))
        for book, Id in zip(query, range(0, 1000)):

            self.BookstableWidget.insertRow(Id)
            self.BookstableWidget.setItem(
                Id, 0, QTableWidgetItem(str(book.id)))
            self.BookstableWidget.setItem(
                Id, 1, QTableWidgetItem(str(book.name)))
            self.BookstableWidget.setItem(
                Id, 2, QTableWidgetItem(str(book.category.name)))
            self.BookstableWidget.setItem(
                Id, 3, QTableWidgetItem(str(book.author)))
            self.BookstableWidget.setItem(
                Id, 4, QTableWidgetItem(book.publisher))
            self.BookstableWidget.setItem(
                Id, 5, QTableWidgetItem(str(book.price)))
            self.BookstableWidget.setItem(
                Id, 6, QTableWidgetItem(str(book.amount_instock)))

    def fill_supplier(self):
        self.comboBox.clear()
        for supplier in Supplier.select():
            self.comboBox.addItem(supplier.name)

    def fill_Client_table(self):

        self.tableWidget_3.setRowCount(0)
        query = Client.select().where(Client.name.contains(self.lineEdit_11.text()))
        for Id, client in enumerate(query):
            self.tableWidget_3.insertRow(Id)
            self.tableWidget_3.setItem(
                Id, 0, QTableWidgetItem(str(client.name)))
            self.tableWidget_3.setItem(
                Id, 1, QTableWidgetItem(str(client.phone)))
            self.tableWidget_3.setItem(
                Id, 2, QTableWidgetItem(str(client.date_joined)))

    def fill_requests(self):
        self.tableWidget_6.setRowCount(0)
        query = Request.select()
        for Id, request in enumerate(query):
            self.tableWidget_6.insertRow(Id)
            self.tableWidget_6.setItem(Id, 0, QTableWidgetItem(str(request.id)))
            self.tableWidget_6.setItem(Id, 1, QTableWidgetItem(str(request.book)))
            self.tableWidget_6.setItem(Id, 2, QTableWidgetItem(str(request.quantity)))
            self.tableWidget_6.setItem(Id, 3, QTableWidgetItem(str(request.op_time.strftime('%d %b, %Y %H:%M:%S'))))

    def refresh(self):
        self.comboBox_2.clear()
        self.comboBox_2.addItem('Unknown')
        for client in Client.select():
            self.comboBox_2.addItem(client.name)
        for category in Category.select():
            self.comboBox_3.addItem(category.name)
            self.comboBox_8.addItem(category.name)
        for book in Book.select():
            self.BooknameLEdit.addItem(book.name)
        self.fill_Client_table()
        self.fill_supplier()
    #---transitions---#

    def switchToOP(self):
        self.tabWidget.setCurrentIndex(0)

    def switchToStock(self):
        self.tabWidget.setCurrentIndex(1)

    def switchToClient(self):
        self.tabWidget.setCurrentIndex(2)

    def switchToReport(self):
        self.tabWidget.setCurrentIndex(3)

    def switchToSettings(self):
        self.tabWidget.setCurrentIndex(4)

    def addclient(self):
        self.addClient_form = AddClient()
        self.addClient_form.show()

    def log_out(self):
        self.Login_Window = LoginWindow()
        self.Login_Window.show()
        self.close()
    #----❗☢⚠⚠ buttons ⚠⚠☢❗ ---#
    #----if it works don't touch it ☠ ----#

    def addSale(self):
        book_Name = self.BooknameLEdit.currentText()
        client_name = self.comboBox_2.currentText()
        quantity_sold = self.spinBox_2.value()

        if book_Name == "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Fields cannot be empty.')
        else:
            try:
                book_ref = Book.get(Book.name == book_Name)
                sale = Sale.create(book=book_ref, quantity=quantity_sold,
                                   client=client_name, book_name=book_Name, price=book_ref.price)
                book_ref.amount_instock -= quantity_sold
                book_ref.save()
                self.BookstableWidget.setItem(
                    book_ref.id-1, 6, QTableWidgetItem(str(book_ref.amount_instock)))
                if book_ref.amount_instock == 0:
                    QMessageBox.warning(
                        QMessageBox(), 'Error', f'{book_Name} ran out of stock.')
                self.tableWidget.insertRow(0)
                self.tableWidget.setItem(
                    0, 0, QTableWidgetItem(str(book_ref.id)))
                self.tableWidget.setItem(
                    0, 1, QTableWidgetItem(str(book_Name)))
                self.tableWidget.setItem(
                    0, 2, QTableWidgetItem(str(book_ref.category.name)))
                self.tableWidget.setItem(0, 3, QTableWidgetItem('sale'))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(str(sale.id)))
                self.tableWidget.setItem(
                    0, 5, QTableWidgetItem(str(client_name)))
                self.tableWidget.setItem(
                    0, 6, QTableWidgetItem(str(sale.price)))
                self.tableWidget.setItem(
                    0, 7, QTableWidgetItem(str(quantity_sold)))
                self.tableWidget.setItem(0, 8, QTableWidgetItem(
                    str(datetime.datetime.now().strftime('%d %b, %Y %H:%M:%S'))))
            except:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    f'{book_Name} is not in the database.')

    def addRequest(self):
        book_Name = self.BooknameLEdit.currentText()
        client_name = self.comboBox_2.currentText()
        quantity = self.spinBox_2.value()

        if book_Name == "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Fields cannot be empty.')
        else:
            try:
                request = Request.create(
                    book=book_Name, quantity=quantity, client=client_name, op_type='request')
                self.tableWidget.insertRow(0)
                # self.tableWidget.setItem(0,0,QTableWidgetItem(str(book_ref.id)))
                self.tableWidget.setItem(
                    0, 1, QTableWidgetItem(str(book_Name)))
                # self.tableWidget.setItem(0,2,QTableWidgetItem(str(book_ref.category.name)))
                self.tableWidget.setItem(0, 3, QTableWidgetItem('request'))
                self.tableWidget.setItem(
                    0, 4, QTableWidgetItem(str(request.id)))
                self.tableWidget.setItem(
                    0, 5, QTableWidgetItem(str(client_name)))
                # self.tableWidget.setItem(0,6,QTableWidgetItem(str(request.price)))
                self.tableWidget.setItem(0, 7, QTableWidgetItem(str(quantity)))
                self.tableWidget.setItem(0, 8, QTableWidgetItem(
                    str(datetime.datetime.now().strftime('%d %b, %Y %H:%M:%S'))))
                ########Requests table#########
                self.tableWidget_6.insertRow(0)
                self.tableWidget_6.setItem(
                    0, 0, QTableWidgetItem(str(request.id)))
                self.tableWidget_6.setItem(
                    0, 1, QTableWidgetItem(str(request.book)))
                self.tableWidget_6.setItem(
                    0, 2, QTableWidgetItem(str(request.quantity)))
                self.tableWidget_6.setItem(0, 3, QTableWidgetItem(
                    str(request.op_time.strftime('%d %b, %Y %H:%M:%S'))))

                self.comboBox_2.setCurrentText("")
                self.BooknameLEdit.setCurrentText("")
            except:
                pass

    def FilterStock(self):
        self.BookstableWidget.setRowCount(0)
        query = Book.select().where(Book.name.contains(self.BookNameField.text()))
        for book, Id in zip(query, range(0, 1000)):

            self.BookstableWidget.insertRow(Id)
            self.BookstableWidget.setItem(
                Id, 0, QTableWidgetItem(str(book.id)))
            self.BookstableWidget.setItem(
                Id, 1, QTableWidgetItem(str(book.name)))
            self.BookstableWidget.setItem(
                Id, 2, QTableWidgetItem(str(book.category.name)))
            self.BookstableWidget.setItem(
                Id, 3, QTableWidgetItem(str(book.author)))
            self.BookstableWidget.setItem(
                Id, 4, QTableWidgetItem(book.publisher))
            self.BookstableWidget.setItem(
                Id, 5, QTableWidgetItem(str(book.price)))
            self.BookstableWidget.setItem(
                Id, 6, QTableWidgetItem(str(book.amount_instock)))

    def Addbook(self):
        book_name = self.lineEdit_3.text()
        category = self.comboBox_3.currentText()
        try:
            price = int(self.lineEdit_4.text())
            Amount = int(self.lineEdit_5.text())
        except:
            QMessageBox.warning(
                QMessageBox(), 'Error', 'you tried to enter string?..really!🙄...fix it now.')
        publisher = self.lineEdit_6.text()
        author = self.lineEdit_31.text()
        description = self.textEdit.toPlainText()
        try:
            Book.get(Book.phone == book_name)
            QMessageBox.information(
                QMessageBox(), 'Error', "book is already in the database.")
        except:
            try:
                category_ref = Category.get(Category.name == category)
            except:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    "wrong category name or it doesn't exist.")
            book = Book.create(name=book_name, author=author, amount_instock=Amount, price=price,
                               description=description, category=category_ref, publisher=publisher)
            # add to stock table
            Id = book.id-1
            self.BookstableWidget.insertRow(Id)
            self.BookstableWidget.setItem(
                Id, 0, QTableWidgetItem(str(book.id)))
            self.BookstableWidget.setItem(
                Id, 1, QTableWidgetItem(str(book.name)))
            self.BookstableWidget.setItem(
                Id, 2, QTableWidgetItem(str(book.category.name)))
            self.BookstableWidget.setItem(
                Id, 3, QTableWidgetItem(str(book.author)))
            self.BookstableWidget.setItem(
                Id, 4, QTableWidgetItem(book.publisher))
            self.BookstableWidget.setItem(
                Id, 5, QTableWidgetItem(str(book.price)))
            self.BookstableWidget.setItem(
                Id, 6, QTableWidgetItem(str(book.amount_instock)))
            # add to combo boxes
            self.BooknameLEdit.addItem(book_name)
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Book is added.')

    def Deletebook(self):
        bookId = int(self.lineEdit_7.text())
        book = Book.delete_by_id(bookId)
        QMessageBox.information(
            QMessageBox(), 'Successful', 'Book is deleted.')
        self.BookstableWidget.removeRow(bookId-1)

    def Savebook(self):
        try:
            bookId = int(self.lineEdit_7.text())
            book = Book.get_by_id(bookId)
            book.name = self.lineEdit_9.text()
            book.description = self.textEdit_2.toPlainText()
            category = self.comboBox_8.currentText()
            category_ref = Category.get(Category.name == category)
            book.category = category_ref
            book.price = self.lineEdit_10.text()
            book.publisher = self.lineEdit_12.text()
            book.author = self.lineEdit_13.text()
            book.save()
            Id = bookId-1
            self.BookstableWidget.setItem(
                Id, 0, QTableWidgetItem(str(book.id)))
            self.BookstableWidget.setItem(
                Id, 1, QTableWidgetItem(str(book.name)))
            self.BookstableWidget.setItem(
                Id, 2, QTableWidgetItem(str(book.category.name)))
            self.BookstableWidget.setItem(
                Id, 3, QTableWidgetItem(str(book.author)))
            self.BookstableWidget.setItem(
                Id, 4, QTableWidgetItem(book.publisher))
            self.BookstableWidget.setItem(
                Id, 5, QTableWidgetItem(str(book.price)))
            self.BookstableWidget.setItem(
                Id, 6, QTableWidgetItem(str(book.amount_instock)))
        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "Id is unacceptable or doesn't exist.")

    def search_Book_database(self):
        try:
            bookId = int(self.lineEdit_7.text())
            book = Book.get_by_id(bookId)
            self.lineEdit_9.setText(book.name)
            self.textEdit_2.setText(book.description)
            self.comboBox_8.setCurrentText(book.category.name)
            self.lineEdit_10.setText(str(book.price))
            self.lineEdit_12.setText(str(book.publisher))
            self.lineEdit_13.setText(str(book.author))

        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "Id is unacceptable or doesn't exist.")

    def search_Client_database(self):
        if self.comboBox_11.currentIndex() == 0:
            client_name = self.lineEdit_20.text()
            try:
                client = Client.get(Client.name == client_name)
                self.client = client
                self.lineEdit_19.setText(client.name)
                self.lineEdit_16.setText(client.phone)
            except:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    "Wrong name or doesn't exist.")
        else:
            client_phone = self.lineEdit_20.text()
            try:
                client = Client.get(Client.phone == client_phone)
                self.client = client
                self.lineEdit_19.setText(client.name)
                self.lineEdit_16.setText(client.phone)
            except:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    "Wrong Phone number or doesn't exist.")

    def Save_client_data(self):
        try:
            self.client.name = self.lineEdit_19.text()
            self.client.phone = self.lineEdit_16.text()
            self.client.save()
            self.refresh()
        except:
            QMessageBox.information(
                QMessageBox(), 'Note', 'choose client first.')

    def Delete_client_data(self):
        try:
            self.client.delete_instance()
            self.refresh()
        except:
            QMessageBox.information(
                QMessageBox(), 'Note', 'choose client first.')

    def search_Supplier_database(self):
        if self.comboBox_14.currentIndex() == 0:
            supplier_name = self.lineEdit_25.text()
            try:
                supplier = Supplier.get(Supplier.name == supplier_name)
                self.supplier = supplier
                self.lineEdit_23.setText(supplier.name)
                self.lineEdit_22.setText(supplier.mail)
                self.lineEdit_21.setText(supplier.phone)
            except:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    "Wrong name or doesn't exist.")
        elif self.comboBox_14.currentIndex() == 1:
            supplier_mail = self.lineEdit_25.text()
            try:
                supplier = Supplier.get(Supplier.mail == supplier_mail)
                self.supplier = supplier
                self.lineEdit_23.setText(supplier.name)
                self.lineEdit_22.setText(supplier.mail)
                self.lineEdit_21.setText(supplier.phone)
            except:
                QMessageBox.information(
                    QMessageBox(), 'Note', "Wrong Mail or doesn't exist.")

        else:
            supplier_phone = self.lineEdit_25.text()
            try:
                supplier = Supplier.get(Supplier.phone == supplier_phone)
                self.supplier = supplier
                self.lineEdit_23.setText(supplier.name)
                self.lineEdit_22.setText(supplier.mail)
                self.lineEdit_21.setText(supplier.phone)
            except:
                QMessageBox.information(
                    QMessageBox(), 'Note', "Wrong Phone or doesn't exist.")

    def Save_Supplier_data(self):
        # try:
            self.supplier.name = self.lineEdit_23.text()
            self.supplier.mail = self.lineEdit_22.text()
            self.supplier.phone = self.lineEdit_21.text()
            self.supplier.save()
            self.refresh()
        # except:
            # QMessageBox.information(
                # QMessageBox(), 'Note', 'choose Supplier first.')

    def Delete_Supplier_data(self):
        try:
            self.supplier.delete_instance()
            QMessageBox.information(QMessageBox(), 'Done', "Supplier deleted.")
        except:
            QMessageBox.information(
                QMessageBox(), 'Note', 'choose Supplier first.')

    def FilterReport(self):
        date1 = self.dateEdit.date().toPyDate()
        date2 = self.dateEdit_2.date().toPyDate()
        query = Sale.select().where(date1 <= Sale.op_time <= date2)
        for Id, sale in enumerate(query):
            self.tableWidget_5.insertRow(Id)
            self.tableWidget_5.setItem(Id, 0, QTableWidgetItem(str(sale.id)))
            self.tableWidget_5.setItem(
                Id, 1, QTableWidgetItem(str(sale.book_name)))
            try:
                self.tableWidget_5.setItem(
                    Id, 2, QTableWidgetItem(str(sale.book.category)))
                self.tableWidget_5.setItem(
                    Id, 3, QTableWidgetItem(str(sale.book.author)))
            except:
                pass
            self.tableWidget_5.setItem(
                Id, 4, QTableWidgetItem(str(sale.price)))
            self.tableWidget_5.setItem(
                Id, 5, QTableWidgetItem(str(sale.quantity)))

    def MakeReport(self):
        pass

    def SendRequest(self):
        try:
            Id = int(self.lineEdit.text())
            request = Request.get_by_id(Id)
            supplier = self.comboBox.currentText()
            QMessageBox.information(
                QMessageBox(), 'Note', 'Request sent to Supplier.')
            request.delete_instance()
            self.fill_requests()
        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "Problem during process.\nCheck the Id")

    def RemoveRequest(self):
        Id = int(self.lineEdit_2.text())
        try:
            Request.delete_by_id(Id)
            self.fill_requests()
        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "Wrong ID or it doesn't exist")

    def Add_supplier(self):
        name = self.lineEdit_32.text()
        email = self.lineEdit_33.text()
        phone = self.lineEdit_48.text()
        if name == '' or email == '' or phone == '':
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Fields cannot be empty.')
        else:
            try:
                Supplier.get(Supplier.name == name)
                QMessageBox.information(
                    QMessageBox(), 'Error', "supllier is already in the database.")
            except:
                Supplier.create(name=name, mail=email, phone=phone)
                QMessageBox.information(
                    QMessageBox(), 'Successful', 'Supplier is added.')
                self.fill_supplier()
                self.lineEdit_32.clear()
                self.lineEdit_33.clear()
                self.lineEdit_48.clear()

    def Add_publisher(self):
        name = self.lineEdit_24.text()
        email = self.lineEdit_26.text()
        address = self.lineEdit_51.text()
        if name == '' or email == '' or address == '':
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Fields cannot be empty.')
        else:
            try:
                Publisher.get(Supplier.name == name)
                QMessageBox.information(
                    QMessageBox(), 'Error', "Publisher is already in the database.")
            except:
                Supplier.create(name=name, email=email, address=address)
                QMessageBox.information(
                    QMessageBox(), 'Successful', 'publisher is added.')
                self.lineEdit_24.clear()
                self.lineEdit_26.clear()
                self.lineEdit_51.clear()

    def Add_category(self):
        name = self.lineEdit_28.text()

        if name == '':
            QMessageBox.warning(QMessageBox(), 'Error',
                                'category name cannot be empty.')
        else:
            try:
                Category.get(Category.name == name)
                QMessageBox.information(
                    QMessageBox(), 'Error', "category is already in the database.")
            except:
                Category.create(name=name)
                QMessageBox.information(
                    QMessageBox(), 'Successful', 'category is added.')
                self.refresh()
                self.lineEdit_28.clear()

    def delete_category(self):
        category_name = self.lineEdit_28.text()
        try:
            category = Category.get(Category.name == category_name)
            category.delete_instance()
            QMessageBox.information(
                    QMessageBox(), 'Successful', 'category is deleted.')
            self.refresh()
            self.lineEdit_28.clear()
        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "wrong category name or it doesn't exist.")

    def Add_employee(self):
        name = self.lineEdit_34.text()
        email = self.lineEdit_35.text()
        phone = self.lineEdit_36.text()
        national_id = self.lineEdit_37.text()
        password1 = self.lineEdit_38.text()
        password2 = self.lineEdit_39.text()
        is_admin = self.checkBox.isChecked()
        if name == '' or email == '' or phone == ''or national_id == '':
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Fields cannot be empty.')
        else:
            if password1 == password2 != '':
                try:
                    Employee.get(Employee.national_Id == national_id)
                    QMessageBox.information(
                        QMessageBox(), 'Error', "Publisher is already in the database.")
                except:
                    Employee.create(name=name, mail=email, phone=phone,
                                    national_Id=national_id, password=password1, isAdmin=is_admin)
                    QMessageBox.information(
                        QMessageBox(), 'Successful', 'Employee is added.')
                    self.lineEdit_34.clear()
                    self.lineEdit_35.clear()
                    self.lineEdit_36.clear()
                    self.lineEdit_37.clear()
                    self.lineEdit_38.clear()
                    self.lineEdit_39.clear()
            else:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    "passwords aren't identical.")

    def save_employee_data(self):
        try:
            new_password = self.lineEdit_44.text()
            self.employee.mail = self.lineEdit_41.text()
            self.employee.phone = self.lineEdit_42.text()
            self.employee.national_Id = self.lineEdit_43.text()
            if new_password!=self.employee.password and new_password !="":
                self.employee.password=new_password
                
            self.employee.save()
            self.lineEdit_41.clear()
            self.lineEdit_42.clear()
            self.lineEdit_43.clear()
        except:
            QMessageBox.warning(QMessageBox(), 'Error',"choose employee first.")

        


    def Check_data(self):
        name = self.lineEdit_40.text()
        password = self.lineEdit_46.text()

        try:
            employee = Employee.get(
                Employee.name == name and Employee.password == password)
            self.employee=employee
            self.lineEdit_41.setText(employee.mail)
            self.lineEdit_42.setText(employee.phone)
            self.lineEdit_43.setText(employee.national_Id)

        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "name or password isn't correct.")
            self.lineEdit_46.clear()

    def delete_employee(self):
        name = self.lineEdit_40.text()
        password = self.lineEdit_46.text()
        try:
            employee = Employee.get(
                Employee.name == name and Employee.password == password)
            employee.delete_instance()
            QMessageBox.information(
                QMessageBox(), 'Successful', f'{name} is removed.')
        except:
            QMessageBox.warning(QMessageBox(), 'Error',
                                "name or password isn't correct.")
            self.lineEdit_46.clear()
#---------------------  ------------------LOGIN WINDOW---------------------------------------#


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.Login)

    #----------Functions----------#
    def Login(self):
        username = self.usrNameField.text()
        password = self.passwordField.text()
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Login")
        msg.setText("Wrong username or password")
        # username=='essam' and password=='essam123'
        try:
            employee = Employee.get(Employee.name == username)
            if employee.password == password:
                if employee.isAdmin=='True':
                    self.window = MyApp('True')
                else:
                    self.window = MyApp('False')
                self.window.show()
                self.hide()
            else:
                msg.exec_()
                self.passwordField.clear()
        except:
            if username == 'admin' and password == 'admin':
                self.window = MyApp(True)
                self.window.show()
                self.hide()
            else:
                msg.exec_()
                self.passwordField.clear()


#----------------------adding client form--------------------------#


class AddClient(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)

        self.AddBtn.clicked.connect(self.AddClient)
        self.CancelBtn.clicked.connect(self.Cancel)

    def AddClient(self):
        name = self.ClientName.text()
        phone = self.Phone.text().strip()
        if name == "" or phone == "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Fields cannot be empty.')
        else:
            try:
                Client.get(Client.phone == phone)
                QMessageBox.information(QMessageBox(
                ), 'Error', "Client is already in the database.\n\nYou can edit it's data in clients tap")
            except:

                Client.create(name=name, phone=phone)

                QMessageBox.information(
                    QMessageBox(), 'Successful', 'Client is added successfully to the database.')
                self.hide()

    def Cancel(self):
        self.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
