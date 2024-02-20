import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from random import randint
from tabulate import tabulate
import seed
import my_select
from models import Base
from models import Student, Mark, Group, Lector, Subject


def main():
    engine = sqlalchemy.create_engine('sqlite:///tables.db', echo=True)
    Base.metadata.drop_all(engine) 
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    seed.create_fake_data(session)

    
    count = 1
    print(f"Query {count}:")
    
    students = session.query(Student).all()
    print(tabulate([(student.id, student.name, student.group.name) for student in students], headers=["ID", "Name", "Group"], tablefmt="grid"))
    count = 1
    
    print(f"Знайти 5 студентів із найбільшим середнім балом з усіх предметів. Query {count}")
    task_1_query = my_select.select_1(session)
    my_select.execute_query(task_1_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти студента із найвищим середнім балом з певного предмета. Query {count}:")
    task_2_query = my_select.select_2(session)
    my_select.execute_query(task_2_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти середній бал у групах з певного предмета. Query {count}:")
    task_3_query = my_select.select_3(session)
    my_select.execute_query(task_3_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти середній бал на потоці (по всій таблиці оцінок). Query {count}:")
    task_4_query = my_select.select_4(session)
    my_select.execute_query(task_4_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти які курси читає певний викладач. Query {count}:")
    task_5_query = my_select.select_5(session)
    my_select.execute_query(task_5_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти список студентів у певній групі. Query {count}:")
    task_6_query = my_select.select_6(session)
    my_select.execute_query(task_6_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти оцінки студентів у окремій групі з певного предмета. Query {count}:")
    task_7_query = my_select.select_7(session)
    my_select.execute_query(task_7_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти середній бал, який ставить певний викладач зі своїх предметів. Query {count}:")
    task_8_query = my_select.select_8(session)
    my_select.execute_query(task_8_query)
    print("*" * 200)
    count += 1
    
    print(f"Знайти список курсів, які відвідує студент. Query {count}:")
    task_9_query = my_select.select_9(session)
    my_select.execute_query(task_9_query)
    print("*" * 200)
    count += 1
    
    print(f"Список курсів, які певному студенту читає певний викладач. Query {count}:")
    task_10_query = my_select.select_10(session)
    my_select.execute_query(task_10_query)
    print("*" * 200)

 

if __name__ == "__main__":
    main()



