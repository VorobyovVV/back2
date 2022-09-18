from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class car(Base):
    __tablename__='cars'
    id=Column(Integer,primary_key=True)
    producer = Column(String(255), nullable=False, unique=True)
    model = Column(String(255), nullable=False, unique=True)
    owner = Column(String(255), nullable=False, unique=True)
    releaseYear= Column(Integer,primary_key=True)
    color = Column(String(255), nullable=False, unique=True)
    maxSpeed = Column(Integer,primary_key=True)
    image = Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)


    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"