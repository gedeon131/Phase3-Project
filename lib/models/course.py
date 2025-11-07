# Modèle Course (cours)
from sqlalchemy import Column, Integer, String
from lib.db import Base, session


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course {self.name}>"


def list_courses():
    courses = session.query(Course).all()
    for c in courses:
        print(c)


def create_course():
    name = input("Enter course name: ")
    course = Course(name=name)
    session.add(course)
    session.commit()
    print("Course added.")


def delete_course():
    try:
        course_id = int(input("Enter course ID to delete: "))
        course = session.query(Course).get(course_id)
        if course:
            session.delete(course)
            session.commit()
            print("✅ Course deleted.")
        else:
            print("❌ Course not found.")
    except ValueError:
        print("❌ Invalid input.")
