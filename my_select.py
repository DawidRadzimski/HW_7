from models import  Group, Teacher, Student, Subject, Grade
from sqlalchemy import func, desc
from connect_db import create_session


def select_1():
    results = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.value), 3).label("avg_grade")
        )
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
    )
    for res in results:
        print(res.fullname, res.avg_grade)


def select_2(course_id_number):
    results = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.value), 3).label("avg_grade")
        )
        .join(Student)
        .where(Grade.subject_id == course_id_number)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
    )
    for res in results:
        print(res.fullname, res.avg_grade)


def select_3(course_id_number):
    results = (
        session.query(
            Group.name, func.round(func.avg(Grade.value), 3).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .where(Grade.subject_id == course_id_number)
        .group_by(Group.id)
        .order_by(desc("avg_grade"))
    )
    for res in results:
        print(res.name, res.avg_grade)


def select_4():
    results = (
        session.query(
            Group.name, func.round(func.avg(Grade.value), 3).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .group_by(Group.id)
    )
    for res in results:
        print(res.name, res.avg_grade)


def select_5(teacher_id_number):
    teacher = session.query(Teacher).filter_by(id=teacher_id_number).one()
    print(f"Subject taught by: {teacher.name}:")
    for subject in teacher.subjects:
        print(subject.name)


def select_6(group_id_number):
    group = session.query(Group).filter_by(id=group_id_number).one()
    print(f"Students in '{group.name}' group:")
    for student in group.students:
        print(student.fullname)


def select_7(group_id_number, course_id_number):
    grades = (
        session.query(Grade)
        .filter_by(subject_id=course_id_number)
        .order_by(Grade.student_id)
    )
    filtered_grades = filter(
        lambda grade: grade.student.group_id == group_id_number, grades
    )
    for grade in filtered_grades:
        print(grade.value, grade.student.fullname, grade.student.group.name)


def select_8(teacher_id_number):
    results = (
        session.query(
            Subject.name,
            func.round(func.avg(Grade.value), 3).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Subject)
        .join(Teacher)
        .where(Teacher.id == teacher_id_number)
        .group_by(Subject.id)
    )
    for res in results:
        print(res)


def select_9(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        print("Student o podanym identyfikatorze nie został znaleziony.")
        return

    passed_subjects = (
        session.query(Subject)
        .join(Grade)
        .filter(Grade.student_id == student_id, Grade.value >= 2.0)
        .distinct()
        .all()
    )

    if not passed_subjects:
        print("Student nie zaliczył jeszcze żadnego przedmiotu.")
        return

    print(f"Lista przedmiotów zaliczonych przez studenta {student.fullname}:")
    for subject in passed_subjects:
        print(subject.name)


def select_10(student_id_number, teacher_id_number):
    results = (
        session.query(Subject.name)
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .where(Student.id == student_id_number)
        .where(Teacher.id == teacher_id_number)
        .distinct()
    )
    for subj in results:
        print(subj.name)




if __name__ == "__main__":
    session = create_session()
    select_1()
    select_2(1)
    select_3(8)
    select_4()
    select_5(1)
    select_6(1)
    select_7(1, 3)
    select_8(1)
    select_9(1)
    select_10(12, 2)

