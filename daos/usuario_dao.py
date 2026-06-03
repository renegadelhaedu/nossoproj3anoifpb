# daos/usuario_dao.py
from config import db
from modelos.usuario import Usuario


class UsuarioDAO:
    #definir métodos estáticos para serem acessados
    #nas rotas do servidor
    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def listar_todos():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_matricula(matricula):
        return Usuario.query.filter_by(matricula=matricula).first()

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()