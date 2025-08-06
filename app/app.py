from flask import Flask, render_template, request
from prometheus_client import Counter, Gauge
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # This exposes /metrics automatically

# Sample book entries
book_entries = [
    {"title": "The Alchemist", "author": "Paulo Coelho"},
    {"title": "Atomic Habits", "author": "James Clear"}
]

# Prometheus custom metrics
book_add_counter = Counter('book_add_requests', 'Number of book add requests')
total_books_gauge = Gauge('total_books', 'Total number of books')

@app.route('/')
def index():
    total = len(book_entries)
    total_books_gauge.set(total)
    return render_template("index.html", books=book_entries, total=total)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    book_entries.append({"title": title, "author": author})
    book_add_counter.inc()
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
