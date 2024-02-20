from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Lector(Base):
    __tablename__ = 'lectors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lector_id = Column(Integer, ForeignKey('lectors.id'))
    lector = relationship("Lector")

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group")

class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
