from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Person (Base):
    __tablename__='person'
    id=Column("id",Integer,primary_key=True)
    name=Column("Name",String(50))
    age=Column("Age",Integer)
    address=Column("Address",String(100))

    def init(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        
    def __repr__(self):
        return "<User(name='%s', age='%s', address='%s')>" % (self.name, self.age, self.address)
    
    

engine=create_engine('sqlite:///mydb.db',echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session=Session()

p1=Person(name='Raj',age=21,address='Chennai')
p2=Person(name='Anne',age=27,address='Dubai')
p3=Person(name='Jhone',age=21,address='Colombo')
p4=Person(name='Tharushi',age=27,address='Dubai')

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)


session.commit()

result=session.query(Person).all()
print(result)

filter_result=session.query(Person).filter_by(name='Raj')
print(filter_result)

session.delete(p1)
session.close()