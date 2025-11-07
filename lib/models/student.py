# Modèle Student (étudiant)
from sqlalchemy import Column, Integer, String
from lib.db import Base, session


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student {self.name} ({self.email})>"


def list_students():
    students = session.query(Student).all()
    for s in students:
        print(s)


def create_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    print("Student added.")


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        student = session.query(Student).get(student_id)
        if student:
            session.delete(student)
            session.commit()
            print("✅ Student deleted.")
        else:
            print("❌ Student not found.")
    except ValueError:
        print("❌ Invalid input.")
