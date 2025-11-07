# Modèle d'inscription (enrollment) d'un étudiant à un cours
from sqlalchemy import Column, Integer, ForeignKey
from lib.db import Base, session
from lib.models.student import Student
from lib.models.course import Course


class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))


def enroll_student():
    try:
        student_id = int(input("Enter student ID: "))
        student = session.query(Student).get(student_id)
        if not student:
            print("❌ Student ID not found.")
            return

        course_id = int(input("Enter course ID: "))
        course = session.query(Course).get(course_id)
        if not course:
            print("❌ Course ID not found.")
            return

        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        session.add(enrollment)
        session.commit()
        print("✅ Student enrolled in course.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
