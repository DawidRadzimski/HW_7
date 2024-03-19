from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
import random
import datetime

# Inicjalizacja generatora losowych danych
fake = Faker()

# Konfiguracja połączenia z bazą danych
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

# Wypełnianie tabeli Nauczyciele
def fill_teachers():
    for _ in range(3, 6):
        teacher = Teacher(
            name=fake.name()
        )
        session.add(teacher)
    session.commit()

# Wypełnianie tabeli Przedmioty i przypisywanie nauczycieli
def fill_subjects():
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Computer Science']
    teachers = session.query(Teacher).all()
    for subject_name in subjects:
        teacher = random.choice(teachers)
        subject = Subject(
            name=subject_name,
            teacher=teacher
        )
        session.add(subject)
    session.commit()

# Wypełnianie tabeli Studenci
def fill_students():
    groups = session.query(Group).all()
    for _ in range(random.randint(30, 50)):
        student = Student(
            fullname=fake.name(),
            group=random.choice(groups)
        )
        session.add(student)
    session.commit()

# Wypełnianie tabeli Oceny
def fill_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for _ in range(random.randint(5, 20)):
            subject = random.choice(subjects)
            grade_value = round(random.uniform(2.0, 5.0), 1)
            date_received = fake.date_time_between(start_date='-1y', end_date='now')
            grade = Grade(
                student=student,
                subject=subject,
                value=grade_value,
                date_received=date_received
            )
            session.add(grade)
    session.commit()

# Wypełnianie tabeli Grupy
def fill_groups():
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        group = Group(
            name=group_name
        )
        session.add(group)
    session.commit()

# Funkcja główna do wypełniania bazy danych
def main():
    fill_teachers()
    fill_subjects()
    fill_groups()
    fill_students()
    fill_grades()

if __name__ == '__main__':
    main()
