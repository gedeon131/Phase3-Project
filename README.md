Description

Ce projet est une application en Python qui combine :

Un ORM maison (Object-Relational Mapping) pour gérer la base de données SQLite.

Une interface en ligne de commande (CLI) pour interagir avec l’utilisateur.

L’application permet de gérer des blogs et leurs posts.
Un Blog peut contenir plusieurs Posts (relation One-to-Many).

Fonctionnalités

Créer un blog

Afficher tous les blogs

Ajouter un post à un blog

Voir les posts d’un blog

Supprimer un blog et ses posts associés

Menu interactif avec validation des entrées

Technologies utilisées

Python 3

SQLite (base de données relationnelle)

Pipenv (gestion d’environnement virtuel et des dépendances)

Structure du projet
phase3_project/
│── app.py         # CLI (interface utilisateur)
│── models.py      # ORM (classes Blog & Post)
│── db.py          # Connexion SQLite
│── Pipfile        # Dépendances
│── Pipfile.lock   # Versions verrouillées
│── README.md      # Documentation
│── blog.db        # Base de données SQLite (créée automatiquement)

Installation et exécution
1. Cloner le projet
git clone <url-du-repo>
cd phase3_project

2. Installer les dépendances
pipenv install

3. Activer l’environnement virtuel
pipenv shell

4. Lancer l’application
python app.py

 Exemple d’utilisation
=== Blog CLI ===
1. Créer un blog
2. Voir tous les blogs
3. Ajouter un post à un blog
4. Voir les posts d’un blog
5. Supprimer un blog
6. Quitter
Choisis une option : 1
Entrez le nom du blog : Mon Premier Blog
Blog créé avec succès !

Modèle de données
Blog
Attribut	Type
id	int (PK)
name	str
Post
Attribut	Type
id	int (PK)
title	str
content	str
blog_id	int (FK → Blog)
Critères respectés

 Deux classes modèles (Blog, Post)

 Relation One-to-Many (un blog → plusieurs posts)

 ORM avec méthodes CRUD (create, delete, get_all, find by id)

 CLI avec menu interactif

 Bonne organisation du code et des fichiers

 README.md explicatif
