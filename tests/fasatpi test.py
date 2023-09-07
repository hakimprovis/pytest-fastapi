# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Date, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///C:\\Users\\User\\Desktop\\MarksandModels (2).db',echo = True)
Base = declarative_base()
class MArksandModel(Base):

    __tablename__ = "ID"

    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __init__(self, name):

        self.name = name


Base.metadata.create_all(engine)
