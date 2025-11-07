from lib.db import session
from lib.models.student import Student

# Création d'un étudiant pour tester
student = Student(name="Alice", email="alice@example.com")

# Ajout à la session puis enregistrement
session.add(student)
session.commit()

print("Étudiant ajouté avec succès.")
