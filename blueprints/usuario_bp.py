from flask import *
from daos.usuario_dao import UsuarioDAO

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuarios')

@usuario_bp.route('/listar')
def listarusuarios():
    usuarios = UsuarioDAO.listar_todos()
    print(usuarios)
    return render_template('listarusuarios.html', usuarios=usuarios)