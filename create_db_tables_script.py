import sqlite3

conn = sqlite3.connect('vk_bot_def_company.db')
conn.cursor()

# Создаем таблицу с категориями
conn.execute(
    '''
    
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30) NOT NULL
        );
    '''
)

# Создаем таблицу с выпечкой по категориям
conn.execute(
    '''

        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30) NOT NULL,
            description VARCHAR(150),
            img_url VARCHAR(150) NOT NULL,
            price INTEGER NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
    '''
)

conn.commit()
conn.close()
