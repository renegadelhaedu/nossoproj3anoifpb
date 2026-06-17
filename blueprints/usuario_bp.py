from flask import *
from daos.usuario_dao import UsuarioDAO

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuarios')

@usuario_bp.route('/listar')
def listarusuarios():
    usuarios = UsuarioDAO.listar_todos()
    return render_template('listarusuarios.html', usuarios=usuarios)


@usuario_bp.route('/remover/<usuario>')
def excluirusuario(usuario):
    print(usuario)
    obj_user = UsuarioDAO.buscar_por_email(usuario)
    UsuarioDAO.remover(obj_user)
    return render_template('logado.html')
