import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime, timedelta
import faker
from random import randint, choice
from tabulate import tabulate
# from main import Group, Lector, Subject, Student, Mark
from models import Group, Lector, Subject, Student, Mark
from sqlalchemy import create_engine



NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_LECTORS = randint(3, 5)
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_MARKS = 100
NUMBER_MARKS_PER_STUDENT = 20

def create_fake_data(session):
    fake_data = faker.Faker()

    groups = [Group(name=fake_data.name()) for _ in range(NUMBER_GROUPS)]
    session.add_all(groups)
    session.commit()

    lectors = [Lector(name=fake_data.name()) for _ in range(NUMBER_LECTORS)]
    session.add_all(lectors)
    session.commit()

    subjects = [Subject(name=fake_data.name(), lector=choice(lectors)) for _ in range(NUMBER_SUBJECTS)]
    session.add_all(subjects)
    session.commit()

    students = [Student(name=fake_data.name(), group=choice(groups)) for _ in range(NUMBER_STUDENTS)]
    session.add_all(students)
    session.commit()

    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    for _ in range(NUMBER_MARKS):
        mark = Mark(
            grade=randint(0, 100),
            timestamp=fake_data.date_time_between(start_date=start_date, end_date=end_date),
            subject_id=choice(subjects).id,  
            student_id=choice(students).id    
        )
        session.add(mark)
    session.commit()