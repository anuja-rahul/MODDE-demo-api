from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
# from sqlalchemy.orm import relationship
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    stock = Column(Integer, nullable=False, server_default="0")
    price = Column(Integer, nullable=False, server_default="0")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    # owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    # name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

