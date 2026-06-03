from config import db

#(BD-4)galera, voces precisam herdar a classe model para que ele consiga mapear os objetos
class Usuario(db.Model):
    #coloque o nome sempre sem espaço e com letras minusc
    __tablename__ = 'usuarios'

    #agora a gente precisa mapear as colunas do BD no objeto
    #atributos da tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    matricula = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    curso = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    #construtor da classe
    def __init__(self, nome, matricula, email, curso, data_nascimento, senha):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.curso = curso
        self.data_nascimento = data_nascimento
        self.senha = senha

    def __repr__(self):
        return f'{self.nome} - {self.email}'