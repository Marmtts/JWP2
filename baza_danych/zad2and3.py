# • Stwórz tabelę o nazwie 'students', która zawiera kolumny 'id' (Integer, Primary Key), 'name'
# (String), 'age' (Integer) oraz ‘grade’ (Float).
# • Dodaj do tabeli trzech studentów.
# • Napisz zapytanie, które wybiera wszystkich studentów z tabeli i wypisze ich na ekran.
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()

# Definicja klasy reprezentującej tabelę w bazie danych
class User(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Integer)

# Tworzenie wszystkich tabel
Base.metadata.create_all(engine)

# Utworzenie sesji
with Session(engine) as session:
    new_user = User(name="Jan Kowalski", age=34,grade = 2.2)
    session.add(new_user)
    new_user = User(name="Krystian Nowak", age=22, grade = 3.5)
    session.add(new_user)
    new_user = User(name="Ela Wozniak", age=31, grade = 4.4)
    session.add(new_user)
    session.commit()

# odczyt danych z sesji
with Session(engine) as session:
    users = session.execute(text("SELECT * FROM students")).all()
    for user in users:
        print(f'Student: {user.name}, Wiek: {user.age}, Ocena: {user.grade}')


# Dodanie studenta 
with Session(engine) as session:
    user_to_add = User(name="Nowy student", age=25,grade = 5.2)
    if user_to_add:
        session.add(user_to_add)
        session.commit()

# Pobranie danych dla studenta z Id=1
with Session(engine) as session:
    users = session.execute(text("SELECT * FROM students WHERE Id = 1")).all()
    for user in users:
        print(f'Student: {user.name}, Wiek: {user.age}, Ocena: {user.grade}')

# aktualizacja danych dla studenta z Id=2
with Session(engine) as session:
    user_to_update = session.get(User, 2) # Zalóżmy, że rekord z ID 2 istnieje
    if user_to_update:
        user_to_update.name = "Robert Koks"
        session.commit()

# Usuwanie studenta z Id 1
with Session(engine) as session:
    user_to_delete = session.get(User, 1)
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()

# odczyt danych z sesji
with Session(engine) as session:
    users = session.execute(text("SELECT * FROM students")).all()
    for user in users:
        print(f'Student: {user.name}, Wiek: {user.age}, Ocena: {user.grade}')