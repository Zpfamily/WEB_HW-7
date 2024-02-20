from sqlalchemy import func, select, label, desc, and_
from tabulate import tabulate
import sqlite3
import sqlalchemy
import main
from models import Group, Lector, Subject, Student, Mark
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from random import randint


def execute_query(query) -> None:
    engine = sqlalchemy.create_engine('sqlite:///tables.db', echo=True)
    with engine.connect() as con:
        result = con.execution_options(stream_results=True).execute(query)
        columns = result.keys()
        results = result.fetchall()
        print(tabulate(results, headers=columns, tablefmt="grid"))





def select_1(session):
    """
    SELECT s.name as student, ROUND(AVG(grade),2) as average_grade
    FROM marks m
    LEFT JOIN students s ON s.id = m.students_id_fn 
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5     SELECT s.name as student, ROUND(AVG(grade),2) as average_grade
    FROM marks m
    LEFT JOIN students s ON s.id = m.students_id_fn 
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5
    """
    query = (
        select(
            Student.name.label('student'),
            func.round(func.avg(Mark.grade), 2).label('average_grade')
        )
        .select_from(Student)
        .outerjoin(Mark, Student.id == Mark.student_id)
        .group_by(Student.id)
        .order_by(func.avg(Mark.grade).desc())
        .limit(5)
    )
    
    return query

def select_2(session):
    """    SELECT s.name AS subject, s.name as student, ROUND(AVG(grade),2) as average_garde
    FROM marks g
    LEFT JOIN students s ON s.id = g.students_id_fn 
    LEFT JOIN subjects d ON g.subjects_id_fn = d.id 
    WHERE g.subjects_id_fn = 2
    GROUP BY s.id
    ORDER BY average_garde DESC
    LIMIT 1
    """
    
    query = (
        select(
            Subject.name.label('subject'), Student.name.label('student'), func.round(func.avg(Mark.grade), 2).label('average_grade'))
        .outerjoin(Mark, Subject.id == Mark.subject_id)
        .outerjoin(Student, Mark.student_id == Student.id)
        .filter(Subject.id == Mark.subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Mark.grade).desc())
        .limit(1)
    )
    
    return query

def select_3(session):
    """
    SELECT  s.name AS subject, gr.name AS [group], ROUND(AVG(grade),2) as average_garde
    FROM marks g
    LEFT JOIN students s ON s.id = g.students_id_fn 
    LEFT JOIN subjects d ON g.subjects_id_fn = d.id 
    LEFT JOIN groups gr ON s.group_id = gr.id 
    WHERE g.subjects_id_fn = 2
    GROUP BY gr.id 
    ORDER BY average_garde DESC
    """
    
    query = (
        select(
            Subject.name.label('subject'),
            Group.name.label('group'),
            func.round(func.avg(Mark.grade), 2).label('average_grade'))
        .outerjoin(Mark, Subject.id == Mark.subject_id)
        .outerjoin(Student, Mark.student_id == Student.id)
        .outerjoin(Group, Student.group_id == Group.id)
        .filter(Subject.id == 2)
        .group_by(Group.id)
        .order_by(func.avg(Mark.grade).desc())
    )
    
    return query

def select_4(session):
    """
    SELECT ROUND(AVG(grade),2) as average_garde
    FROM marks 
    ORDER BY average_garde DESC
    """
    
    query = (
        select(
            func.round(func.avg(Mark.grade), 2).label('average_grade'))
        .order_by(func.avg(Mark.grade).desc())
    )
    
    return query

def select_5(session):
    """
    SELECT l.name AS lector, s.name AS subject
    FROM marks m 
    LEFT JOIN subjects s ON m.subjects_id_fn  = s.id 
    LEFT JOIN lectors l ON s.lector_id = l.id 
    WHERE l.id = 1
    GROUP BY s.id
    """
    
    query = (
        select(
            Lector.name.label("lector"),
            Subject.name.label("subject"),
            func.round(func.avg(Mark.grade), 2).label('average_grade'))
        .outerjoin(Subject, Mark.subject_id == Subject.id)
        .outerjoin(Lector, Subject.lector_id == Lector.id)
        .filter(Lector.id == 1)
        .group_by(Subject.id)
        
    )
    
    return query

def select_6(session):
    """
    SELECT l.name AS lector, s.name AS subject
    FROM marks m 
    LEFT JOIN subjects s ON m.subjects_id_fn  = s.id 
    LEFT JOIN lectors l ON s.lector_id = l.id 
    WHERE l.id = 1
    GROUP BY s.id
    """
    
    query = (
        select(
            Group.name.label("group"),
            Student.name.label("student"),
            func.substr(Student.name, func.instr(Student.name, ' ') + 1).label('last_name'))
        .outerjoin(Group, Student.group_id == Group.id)
        .filter(Student.group_id == 1)
        .group_by('last_name')
        
    )
    
    return query

def select_7(session):
    """
    SELECT s.name as student, su.name AS subject, gr.name AS [group], grade
    FROM marks m
    LEFT JOIN students s ON s.id = m.students_id_fn 
    LEFT JOIN subjects su ON m.subjects_id_fn = su.id 
    LEFT JOIN groups gr ON s.group_id = gr.id 
    WHERE su.id = 1 AND gr.id = 1
    ORDER BY grade DESC
    """
    
    query = (
        select(
            Student.name.label("student"),
            Subject.name.label("subject"),
            Group.name.label('group'),
            Mark.grade)
        .outerjoin(Student, Mark.student_id == Student.id)
        .outerjoin(Subject, Mark.subject_id  == Subject.id)
        .outerjoin(Group, Student.group_id  == Group.id)
        .filter(Subject.id == 1 ,Group.id == 1)
        .order_by(Mark.grade.desc())
        
    )
    
    return query

def select_8(session):
    """
    SELECT l.name AS lector, su.name AS subject, ROUND(AVG(grade),2) as average_garde
    FROM marks m 
    LEFT JOIN subjects su ON m.subjects_id_fn  = su.id 
    LEFT JOIN lectors l ON su.lector_id = l.id 
    WHERE l.id = 1
    GROUP BY su.id
    """
    
    query = (
        select(
            Lector.name.label("lector"),
            Subject.name.label("subject"),
            func.round(func.avg(Mark.grade),2).label("average_garde"))
        .outerjoin(Subject, Mark.subject_id  == Subject.id)
        .outerjoin(Lector, Subject.lector_id  == Lector.id)
        .filter(Lector.id == 1)
        .order_by(Subject.id)
        
    )
    
    return query

def select_9(session):
    """
    SELECT  s.name as student, su.name AS subject
    FROM marks m
    LEFT JOIN students s ON s.id = m.students_id_fn 
    LEFT JOIN subjects su ON m.subjects_id_fn = su.id 
    WHERE s.id = 3
    GROUP BY subject
    ORDER BY subject
    """
    
    query = (
        select(
            Student.name.label('student'), 
            Subject.name.label('subject'))
        .outerjoin(Mark, Student.id == Mark.student_id)
        .outerjoin(Subject, Mark.subject_id == Subject.id)
        .filter(Student.id == 3)
        .group_by(Subject.name)
        .order_by(Subject.name)
    )
    
    return query

def select_10(session):
    """
    SELECT su.name AS subject, s.name as student, l.name AS lector
    FROM marks m
    LEFT JOIN students s ON s.id = m.students_id_fn 
    LEFT JOIN subjects su ON m.subjects_id_fn = su.id 
    LEFT JOIN lectors l ON su.lector_id = l.id 
    WHERE s.id = 3 AND l.id = 1
    GROUP BY subject
    ORDER BY subject
    """
    
    query = (
        select(
            Subject.name.label('subject'),
            Student.name.label('student'), 
            Lector.name.label('lector'))
        .outerjoin(Mark, Student.id == Mark.student_id)
        .outerjoin(Subject, Mark.subject_id == Subject.id)
        .outerjoin(Lector, Subject.lector_id == Lector.id)
        .filter(Student.id == 3)
        .group_by(Subject.name)
        .order_by(Subject.name)
    )
    
    return query

    