from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Product
from config import DB_URL

engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)

def init_db():
    """ Создание таблиц в БД. """
    Base.metadata.create_all(engine)

def seed_data():
    """ Заполнение таблиц тестовыми данными. """
    session = Session()

    categories = [
        Category(name="Пирожки"),
        Category(name="Пирожные"),
        Category(name="Сочники"),
    ]
    products = [
        Product(
            name='Пирожок с картошкой',
            description='Классический пирожок с картофелем пюре и зеленым луком.',
            img_url='photo-228282732_456239022',
            price=25.00,
            category=categories[0]
        ),
        Product(
            name='Пирожок с творогом',
            description='Пирожок с творожной начинкой.',
            img_url='photo-228282732_456239028',
            price=29.50,
            category=categories[0]
        ),
        Product(
            name='Пирожок с яблоком',
            description='Пирожок с яблочной начинкой.',
            img_url='photo-228282732_456239027',
            price=34.50,
            category=categories[0]
        ),
        Product(
            name='Пирожное корзинка',
            description='''
                Пирожные «Корзиночки», называвшиеся ранее тарталетками, 
                представляют собой круглые или овальные, выпеченные из 
                песочного или другого теста чашечки — корзиночки, заполненные 
                разной начинкой и отделанные фруктами, кремом, цукатами, желе, посыпкой.
            ''',
            img_url='photo-228282732_456239023',
            price=77.00,
            category=categories[1]
        ),
        Product(
            name='Пирожное эклер',
            description='''
                пирожное в виде трубочки из заварного теста, покрытой помадкой, с 
                начинкой из сливочно-масляного или заварного крема.
            ''',
            img_url='photo-228282732_456239020',
            price=49.99,
            category=categories[1]
        ),
        Product(
            name='Пирожное манго',
            description='''
                Яркое пирожное в виде манго на основе белого кефирного бисквита с 
                лёгким манговым муссом, сливочным кремом и желе из пюре манго и маракуйи. 
                Дольки манго, пропитанные сахарным сиропом, добавляют экзотики. Десерт 
                покрыт зеркальной глазурью.
            ''',
            img_url='photo-228282732_456239019',
            price=59.99,
            category=categories[1]
        ),
        Product(
            name='Сочник с малиной',
            description='''
                Сочник с малиной — это вид выпечки в виде сложенной пополам лепёшки с 
                полуоткрытой или закрытой начинкой.
            ''',
            img_url='photo-228282732_456239018',
            price=59.99,
            category=categories[2]
        ),
        Product(
            name='Сочник с лимоном',
            description='''
                Сочник с лимоном — это нежное песочно-бисквитное тесто с необычной 
                начинкой из натурального лимона.
            ''',
            img_url='photo-228282732_456239026',
            price=69.00,
            category=categories[2]
        ),
        Product(
            name='Сочник с творогом',
            description='''
                Представители классической русской выпечки, пирожки из бездрожжевого 
                теста с творожной начинкой.
            ''',
            img_url='photo-228282732_456239021',
            price=49.00,
            category=categories[2]
        ),
    ]

    session.add_all(categories + products)
    session.commit()
    # session.close()
