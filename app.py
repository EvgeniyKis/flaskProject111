from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wfou200ef2h0ehf2eij1-fi2h2'


def get_db_connection():
    connection = sqlite3.connect('database.db')
    return connection


@app.route('/')
def index():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM "articles";')
    articles = cur.fetchall()
    cur.close()
    connection.close()
    return render_template("index.html", articles=articles)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute('INSERT INTO articles (title, author, content)'
                    'VALUES (?, ?, ?)',
                    (title,
                     author,
                     content)
                    )
        connection.commit()
        cur.close()
        connection.close()
        return redirect(url_for('index'))
    return render_template("create.html")


if __name__ == '__main__':
    app.run(DEBUG=True)
