from models import session, Base, engine
from models.blog import Blog
from models.post import Post

# Création des tables
Base.metadata.create_all(engine)

def menu():
    while True:
        print("\n=== Blog CLI ===")
        print("1. Créer un blog")
        print("2. Voir tous les blogs")
        print("3. Ajouter un post à un blog")
        print("4. Voir les posts d’un blog")
        print("5. Supprimer un blog")
        print("6. Quitter")
        choice = input("Choisis une option : ")

        if choice == "1":
            create_blog()
        elif choice == "2":
            list_blogs()
        elif choice == "3":
            add_post()
        elif choice == "4":
            view_posts()
        elif choice == "5":
            delete_blog()
        elif choice == "6":
            print("À bientôt 👋")
            break
        else:
            print("Option invalide.")

def create_blog():
    name = input("Nom du blog : ")
    blog = Blog(name=name)
    session.add(blog)
    session.commit()
    print(f"✅ Blog '{name}' créé.")

def list_blogs():
    blogs = session.query(Blog).all()
    if not blogs:
        print("Aucun blog trouvé.")
    else:
        for b in blogs:
            print(f"{b.id} - {b.name}")

def add_post():
    list_blogs()
    blog_id = input("ID du blog pour ajouter un post : ")
    blog = session.query(Blog).get(blog_id)
    if blog:
        title = input("Titre du post : ")
        content = input("Contenu du post : ")
        post = Post(title=title, content=content, blog=blog)
        session.add(post)
        session.commit()
        print("✅ Post ajouté.")
    else:
        print("❌ Blog introuvable.")

def view_posts():
    blog_id = input("ID du blog : ")
    blog = session.query(Blog).get(blog_id)
    if blog:
        print(f"\n📌 Posts de {blog.name}:")
        for p in blog.posts:
            print(f"- {p.title}: {p.content}")
    else:
        print("❌ Blog introuvable.")

def delete_blog():
    blog_id = input("ID du blog à supprimer : ")
    blog = session.query(Blog).get(blog_id)
    if blog:
        session.delete(blog)
        session.commit()
        print("✅ Blog supprimé.")
    else:
        print("❌ Blog introuvable.")