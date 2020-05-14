from collections import defaultdict

from flask import Flask, jsonify, request #importando o flask e jsonify
import json
app = Flask(__name__)

desenvolvedores = [
    {"nome":"Daniel",
     "habilidades":["Python","Flask"]
     },
    {"nome":"Rafael",
     'habilidades':["Python","Django"]}
]
# Devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods = ['GET','POST','PUT','DELETE'])#Rota 01
def desenvolvedor(id):
    #PEgar o registro de um desenvolvedor
    if(request.method ==  "GET"):
        try:
            # pegar posicao na lista
            response = desenvolvedores[id]
        except IndexError:
            messagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {'status': 'ERRO', "messagem": messagem}
        except Exception:
            messagem = "Erro desconhecido. Procure o admistrador da API"
            response = {'status': 'erro', "mensagem": messagem}

        return jsonify(response)# retornar as imformações do desenvolvedor
    # METODO PARA EDITAR REGISTROS
    elif(request.method == "PUT"):
        dados = json.loads(request.data)#editando nformaçao
        desenvolvedores[id] = dados#enserindo informaçao
        return jsonify(dados)
    elif(request.method == "DELETE"):#METODO PARA DELETAR DESENVOLVEDOR
        desenvolvedores.pop(id)
        return jsonify({'Status':'sucesso', 'messagem':'Registro Excluido.'})

# Lista todos os  desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=["POST", "GET"])
def lista_desenvolvedores():
    if(request.method == "POST"):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({"status":"sucesso", "messagem":"registro inserido"})
    elif(request.method == "GET"):
        return jsonify(desenvolvedores)

if(__name__ == '__main__'):
    app.run(debug=True)
