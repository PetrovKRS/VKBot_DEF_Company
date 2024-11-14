import sqlite3

conn = sqlite3.connect('vk_bot_def_company.db')
conn.cursor()

# Добавляем категории в бд
conn.execute(
    '''

        INSERT INTO categories (name)
        VALUES ('Пирожки'), ('Пирожные'), ('Сочники');
    '''
)

# Добавляем выпечку в бд
conn.execute(
    '''

        INSERT INTO products (name, description, img_url, price, category_id) 
        VALUES ('Пирожок с картошкой', 'Классический пирожок с картофелем пюре и зеленым луком.', '', 25.00, 1),
               ('Пирожное корзинка', 'Пирожные «Корзиночки», называвшиеся ранее тарталетками, представляют собой круглые или овальные, выпеченные из песочного или другого теста чашечки — корзиночки, заполненные разной начинкой и отделанные фруктами, кремом, цукатами, желе, посыпкой.', '', 77.00, 2),
               ('Сочник с творогом', 'представители классической русской выпечки, пирожки из бездрожжевого теста с творожной начинкой.', '', 49.00, 3);
    '''
)


conn.commit()
conn.close()

print("Данные успешно добавлены в базу данных")
