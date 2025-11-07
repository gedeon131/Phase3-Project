# 📚 Course Management CLI App

Un projet Python Phase 3 permettant de gérer les **étudiants**, **cours** et **inscriptions** via une **interface en ligne de commande (CLI)**, avec **SQLAlchemy ORM** et une base de données SQLite.

---

## ✅ Objectifs pédagogiques

- Utiliser un **ORM (SQLAlchemy)** pour gérer une base relationnelle.
- Créer une **interface CLI** conviviale et orientée utilisateur.
- Respecter les bonnes pratiques de la **programmation orientée objet (OOP)**.
- Modéliser une relation **one-to-many** (`Course` ↔ `Enrollment` ↔ `Student`).

---


## 🛠️ Installation

1. Clone le projet :
   ```bash
   git clone https://github.com/tonprofil/Phase3-Project.git
   cd Phase3-Project
Installe les dépendances :

bash
Copier le code
pip install sqlalchemy click
Exécute le projet :

bash
Copier le code
python run.py
▶️ Utilisation
Une fois le programme lancé, un menu CLI s'affiche :


Copier le code
=== Course Management CLI ===
1. View all courses
2. Add a course
3. View all students
4. Add a student
5. Enroll student to course
6. Quit

🧑‍💻 Auteur
Gedeon Freycinet