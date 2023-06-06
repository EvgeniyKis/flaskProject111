import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS articles;')
cur.execute('CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'title varchar(100) NOT NULL,'
            'author varchar(100) NOT NULL,'
            'content text NOT NULL,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

cur.execute('INSERT INTO articles (title, author, content)'
            'VALUES (?, ?, ?)',
            ('Первая статья',
             'Кислицин Женя',
             'Это просто проверочная статья, здесь нет интересного текста.')
            )

connection.commit()
cur.close()
connection.close()
