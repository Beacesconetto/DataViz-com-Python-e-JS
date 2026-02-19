from sqlalchemy import Column, Integer, String, Enum, create_engine, UniqueConstraint
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base,sessionmaker
import csv


engine = create_engine('sqlite:///nobel_winners.db', echo=True)
Base = declarative_base()

class Winner(Base):
    __tablename__ = 'winners'
    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    nationality = Column(String)
    year = Column(Integer)
    gender = Column(Enum('male', 'female'))

    __table_args__ = (
        UniqueConstraint('name', 'category', 'year', name='uix_winner_unique'), # Não pode exister algo que o nome + categoria + ano sejam iguais
    )

    def __repr__(self):
        return "<Winner(name = '%s', category = '%s', year = '%s')>"\
            %(self.name, self.category, self.year)

Base.metadata.create_all(engine)

#Vai ler o CSV com os dados
with open('nobel_winners.csv') as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)

# Session é a ponte entre o código e o banco.
Session = sessionmaker(bind=engine)
session = Session()

# albert = Winner(**nobel_winners[0]) -> Objeto que vai pro banco
winner_rows = [Winner(**w) for w in nobel_winners]

result = session.query(Winner).filter_by(nationality = 'Swiss').all() # pega somente os que tem essa nacionalidade
result2 = session.query(Winner).filter(Winner.category == 'Physics', Winner.nationality != 'Swiss').all()
ById = session.query(Winner).get(2)
res = session.query(Winner).order_by('year').all()

marie = session.query(Winner).get(2)
marie.nationality = 'French' 
session.commit()

try:
    session.add_all(winner_rows) # Registra o objeto para ser salvo.
    session.commit() # Salva no banco o que foi criado
    print("Dados inseridos com sucesso!")
except IntegrityError:
    session.rollback()
    print("⚠️ Alguns registros já existem no banco.")

# session.expunge(albert) -> Retira o objeto da sessão e não do banco.
# session.new -> Mostra que tem algo novo esperando o commit

print(session.query(Winner).get(2).nationality)

# Se quiser ver de modo mais facil
#  winners = session.query(Winner).all()
# print(winners)