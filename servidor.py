from flask import *
from config import db
from modelos.usuario import Usuario
from daos.usuario_dao import UsuarioDAO
from blueprints.usuario_bp import usuario_bp

app = Flask(__name__)
#1 passo - senha secreta
app.secret_key = 'KJ#H4k3jh412dasd'
usuarios = []

app.register_blueprint(usuario_bp)

# (BD-1) bora configurar o banco na aplicacao
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/teste3anoifpb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

#(BD-2) assim que inicia o servidor, vc precisa gerar contexto para informar que a aplicação está executando
#e assim pode-se fazer alteração no banco de dados via sqlalchemy
with app.app_context():
    db.create_all()#responsável por criar a estrutura do BD

#rotas ou endpoints
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'GET':
        return render_template('cadastrar.html')

    matricula = request.form.get('matricula')
    nome = request.form.get('nome')
    email = request.form.get('email')
    curso = request.form.get('curso')
    data = request.form.get('data')
    senha = request.form.get('senha')
    #instanciando um objeto da classe Usuario
    novo_usuario = Usuario(nome, matricula, email, curso, data, senha)

    # usuarios.append(novo_usuario)
    #(BD-3)
    UsuarioDAO.salvar(novo_usuario)

    return render_template('login.html')


@app.route('/logar', methods=['POST'])
def logar():
    login = request.form.get('login')
    senha = request.form.get('senha')
    usuario = UsuarioDAO.buscar_por_email(login)
    #if login == 'rene' and senha == '123':
    if usuario.senha == senha:
        #2 passo: colocar o usuário na sessão
        session['usuario'] = login
        return render_template('logado.html')
    else:
        return render_template('login.html')


@app.route('/listarusuarios')
def listarusuarios():
    us1 = Usuario('mirela', '1234', 'saberaverdade@gmail.com', "meio ambiente", '17/03/2009')
    us2 = Usuario('junior', '8456', 'dancarino@gmail.com', "informatica", '06/06/2008')
    lista = [us1, us2]
    return render_template('listausuarios.html', lista=lista)


#controle de acesso
@app.route('/listarfofocas')
def listar_fofocas():
    # 3 passo - cada rota, verifico se ele está logado
    if 'usuario' in session:
        x = 1
        return 'fofoca 1 <br> fofoca 2'
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    #4 passo - fazer o logout
    session.clear()
    return render_template('login.html')


@app.route('/filmes')
def filmes():
    filmes = [['a vida é bela', 2026], ['HP do bruxo', 2011]]
    return render_template('index2.html', filmes=filmes)


if __name__ == '__main__':
    app.run()