from flask import Flask, jsonify, request
from lista_usuarios import usuarios

app = Flask(__name__)
@app.route('/')

def primeira_pagina():
    return '<h1> Minha primeira pagina</h1>'


@app.route('/segunda_pagina')
def segunda_pagina():
    return '<h1> Minha segunda pagina </h1>'




@app.route('/pagina_form')
def pagina_form():
    form = '''
    <form action="">
        <label>Primeiro nome</label>
        <input type="text" placeholder="primiero nome"><br><br>
        <label> Segundo nome</label>
        <input type="text" placeholder="Segundo nome"> <br><br><br>

         <button> Enviar</button>

        
    </form>
'''
    return form



@app.route('/dados')
def dados():
    nome = '''
<h1> Sou Juvenaldo Canja </h1>
<h1> Tenho 33 anos de idade. </h1>
        
'''
    return nome



@app.route('/dicion')
def dicion():
    dict = '''
'nome': Juvenaldo
'idade': 33
        
'''
    return dict


# @app.route('/dados_json')
# def meus_dados_json():
#     return jsonify(nome='Juvenaldo', idade=33)


# # ROTA DINAMICA

# @app.route('/v1/user/idade/<nome>', methods= ['GET'])
# def retorna_idade(nome):
#     if nome == 'Juvenaldo':
#         return jsonify(idade = 33)
#     else:
#         return jsonify(idade='Não encontrado!')
    

# LISTA_USUARIOS

@app.route('/v1/user/idade/<nome>', methods = ['GET'])
def consulta_idade(nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            return jsonify(idade = usuario['idade'])
        
    return jsonify('Usuario não encontrado'), 404
    


# ENDPOINT
@app.route('/v1/user/consulta', methods = ['GET'])
def consulta_usuario():
    nome = request.args.get('nome')
    email = request.args.get('email')
    for usuario in usuarios:
        if usuario['nome'] == nome or usuario['email'] == email:
            return jsonify(usuario)
    return jsonify(mensagem = 'Usuario não encontrado'), 404

# http://127.0.0.1:5000/v1/user/consulta?nome=Juvenaldo

   
if __name__ == '__main__':
    app.run(debug=True)