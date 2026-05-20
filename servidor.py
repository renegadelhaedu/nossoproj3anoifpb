from flask import *

from modelos.usuario import Usuario

app = Flask(__name__)
#1 passo - senha secreta
app.secret_key = 'KJ#H4k3jh412dasd'
usuarios = []

#rotas ou endpoints
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    matricula = request.form.get('matricula')
    nome = request.form.get('nome')
    email = request.form.get('email')
    curso = request.form.get('curso')
    data = request.form.get('data')

    #instanciando o objeto
    novo_usuario = Usuario(nome, matricula, email, curso, data)
    usuarios.append(novo_usuario)
    return render_template('criarpagina.html')


@app.route('/logar', methods=['POST'])
def logar():
    login = request.form.get('login')
    senha = request.form.get('senha')
    if login == 'rene' and senha == '123':
        #2 passo: colocar o usuário na sessão
        session['usuario'] = login
        return render_template('teste.html')
    else:
        return render_template('login.html')

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

if __name__ == '__main__':
    app.run()