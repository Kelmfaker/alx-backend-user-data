#!/usr/bin/env python3
"""
This module defines the User model and sets up the database.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    User model for the users table.
    Attributes:
        id (int):The primary key.
        email (str): The user's email address, non-nullable.
        hashed_password (str): The user's hashed password,non-nullable.
        session_id (str): The user's session ID, nullable.
        reset_token (str): The user's reset token, nullable.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


# Create an SQLite database
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
# Create a session
Session = sessionmaker(bind=engine)
session = Session()
