from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

blogs = []
posts = {}

@app.route('/')
def index():
    return render_template("index.html", blogs=blogs)

@app.route('/create_blog', methods=['POST'])
def create_blog():
    blog_name = request.form['blog_name']
    blog_id = len(blogs) + 1
    blogs.append({"id": blog_id, "name": blog_name})
    posts[blog_id] = []
    return redirect(url_for('index'))

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    blog = next((b for b in blogs if b["id"] == blog_id), None)
    if not blog:
        return "Blog not found", 404
    return render_template("blog.html", blog=blog, blog_posts=posts[blog_id])

@app.route('/blog/<int:blog_id>/add_post', methods=['POST'])
def add_post(blog_id):
    title = request.form['title']
    content = request.form['content']
    posts[blog_id].append({"title": title, "content": content})
    return redirect(url_for('view_blog', blog_id=blog_id))


if __name__ == "__main__":
    app.run(debug=True)