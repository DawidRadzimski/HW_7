import os
from connect_db import create_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Teacher

# Odczytaj zmienną środowiskową DATABASE_URL
DATABASE_URL = os.environ.get('DATABASE_URL')

# Utwórz silnik bazy danych
#engine = create_engine()

session = create_session()

# Przykładowe zapytanie, na przykład wybór pierwszego nauczyciela z bazy
teacher = session.query(Teacher).first()
if teacher:
    print(f'Pierwszy nauczyciel w bazie: {teacher.name}, przedmiot: {teacher.subjects}')
else:
    print('Brak nauczycieli w bazie.')
