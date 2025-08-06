from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho"},
    {"title": "Atomic Habits", "author": "James Clear"}
]

@app.route('/')
def index():
    total = len(books)
    return render_template("index.html", books=books, total=total)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    books.append({"title": title, "author": author})
    return index()
