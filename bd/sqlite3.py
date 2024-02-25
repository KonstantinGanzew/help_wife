import sqlite3 as sq

# Создание бд
async def db_start():
    global db, cur
    db = sq.connect(r'.\bd\posts.db')
    cur = db.cursor()

    # Определяем существует ли база с таблицей employees, если нет то создаем ее с необходимыми параметрами

    cur.execute('''CREATE TABLE IF NOT EXISTS posts(
        url_post TEXT PRIMARY KEY)
        ''')
        
    db.commit()

# Проверяем наличие сотрудника
async def search_url(url):
    with sq.connect(r'.\bd\posts.db') as con:
        cur = con.cursor()
        cur.execute(f'SELECT * FROM posts WHERE url_post="{url}"')
        return cur.fetchall()

# Добавляем посты
async def add_post(url):
    with sq.connect(r'.\bd\posts.db') as con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO posts (url_post) VALUES("{url}")')
        return cur.fetchall()