# import uuid
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"
#     id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
#     name = Column(String)
#     age = Column(Integer)
