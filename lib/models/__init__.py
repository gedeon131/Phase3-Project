# Initialise la base de données ORM et crée les tables
from lib.db import Base, engine
from lib.models.course import Course
from lib.models.student import Student
from lib.models.enrollment import Enrollment

Base.metadata.create_all(engine)
