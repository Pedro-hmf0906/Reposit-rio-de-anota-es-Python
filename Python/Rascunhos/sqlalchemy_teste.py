from sqlalchemy import create_engine, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# as tabelas

#   O Banco de Dados sempre adiciona o 's' no final da tabela e tudo minusculo automaticamente
class Usuario(Base):
    __tablename__ = 'usuarios' #-> Adiciona o nome desejado manualmente da tabela
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha

# nome automatico da tabela: 'usuarios'


class Livro(Base):
    __tablename__ = 'livros'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column('titulo', String)
    qtd_paginas = Column('qtd_paginas', Integer)
    dono = Column('dono', ForeignKey('usuarios.id'))

    def __init__(self, titulo, qtd_paginas, dono):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.dono = dono

# nome automatico da tabela = 'livros'

Base.metadata.create_all(bind=db)

# C - CREATE
# usuario = Usuario(nome='Lira',email='qlqcoisa@gmail.com',senha='123456')
# session.add(usuario)
# session.commit()

# R - READ
# lista_usuarios = session.query(Usuario).all()
# usuario_lira = session.query(Usuario).filter_by(email='qlqcoisa@gmail.com').first() # exite .all()


# livro = Livro(titulo='Nome do Vento', qtd_paginas=1000, dono=usuario_lira.id)
# session.add(livro)
# session.commit()

# U - UPDATE

# usuario_lira.nome = 'João Lira'
# session.add(usuario_lira)
# session.commit()

# D - DELETE

# delete_livro = session.query(Livro).filter_by(id=2).first()

# del delete_livro[-1]
# session.query(Livro).delete()
# session.commit()
