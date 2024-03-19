from sqlalchemy import create_engine as sqlalchemy_create_engine
from sqlalchemy.orm import sessionmaker

# Tworzenie silnika bazy danych
def create_engine(url):
    return sqlalchemy_create_engine(url)

# Tworzenie sesji
def create_session():
    engine = create_engine("sqlite:///school.db")
    Session = sessionmaker(bind=engine)
    return Session()
