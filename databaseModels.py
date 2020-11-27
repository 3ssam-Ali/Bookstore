from peewee import *
import datetime
db = SqliteDatabase('database.db' ,pragmas={
    'journal_mode': 'wal',
    'foreign_keys': 1,
    'ignore_check_constraints': 0})

class BaseModel(Model):
    class Meta:
        database = db   

class Category(BaseModel):
    name=CharField()

class Client(BaseModel):
    name=CharField()
    phone=CharField()   
    date_joined=DateField(default=datetime.date.today())

class Supplier(BaseModel):
    name=CharField()
    mail=CharField()
    phone=CharField()


class Publisher(BaseModel):
    name=CharField()
    email=CharField()
    address=TextField()

class Employee(BaseModel):
    name=CharField()
    mail=CharField()
    phone=CharField()
    national_Id=CharField()
    password=CharField()
    isAdmin=CharField(default='False')


class Book(BaseModel):
    name = CharField(null=False,unique=True)
    author=CharField(null=False)
    amount_instock=IntegerField(null=False)
    price= IntegerField(null=False)
    description=TextField()
    publisher=CharField()
    category=ForeignKeyField(Category, backref='books', on_delete='CASCADE')
    

class Sale(BaseModel):
    
    op_time=DateTimeField(default=datetime.datetime.now)
    quantity=IntegerField(null=False)
    client=CharField()
    book_name=CharField()
    price=CharField()   
    book=ForeignKeyField(Book, backref='operations',on_delete='SET NULL')

    # client=ForeignKeyField(Client,backref='operetions')
    # employee=ForeignKeyField(Employee,backref='operetions')

class Request(BaseModel):
    
    op_time=DateTimeField(default=datetime.datetime.now)
    quantity=IntegerField(null=False)
    client=CharField()
    book=CharField()
db.connect()
db.create_tables([Category,Client,Supplier,Publisher,Employee,Book,Sale,Request])


# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
# uncle_bob.save()
# grandma.save()
# herb.save()


# bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
# herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
# herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
# herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

# herb_mittens.delete_instance()  