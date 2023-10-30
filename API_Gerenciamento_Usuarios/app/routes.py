from flask import Response, request, json
from app import app, db
from app.models import users
from flask_jwt_extended import create_access_token, jwt_required

import uuid


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
    
    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

#AUTENTICAÇÃO/LOGIN
@app.route("/authenticate", methods=["POST"])
def authenticate():
    body = request.get_json()
    login_email = body.get("email")
    login_document = body.get("document")
    login_phone = body.get("phone")
    password = body.get("password")

    if not (login_email or login_document or login_phone) or not password:
        return gera_response(400, "user", {}, "Dados inválidos")

    authentique_user = None

    for user in users.query.all():
        if ((user.email == login_email or user.document == login_document or user.phone == login_phone) and user.password == password):
            authentique_user = user
            break

    if authentique_user:
        access_token = create_access_token(identity=authentique_user.uuid)
        return gera_response(200, "user", {"Baerer Token": access_token}, "Autenticação concluída")
    else:
        return gera_response(401, "user", {}, "Falha na autenticação")

# Rota para listar usuários com busca simples, filtro e ordenação
@app.route("/users", methods=["GET"])
def listar_usuarios():
    name_filter = request.args.get("name")
    search_query = request.args.get("q")
    order_type = request.args.get("order_type", "asc")  # Parâmetro de tipo de ordenação (padrão: asc)

    user_filtro = users.query

    try:
        if search_query:
            user_filtro = user_filtro.filter(
                (users.name.ilike(f"%{search_query}%")) 
            )

        if name_filter:
            user_filtro = user_filtro.filter(users.name.ilike(f"%{name_filter}%"))

        if order_type == "asc":
            user_filtro = user_filtro.order_by(users.name.asc())
        elif order_type == "desc":
            user_filtro = user_filtro.order_by(users.name.desc())
        else:
            return gera_response(400, "user", {}, "Parâmetro de tipo de ordenação inválido")

        users_objetos = user_filtro.all()
        return gera_response(200, "users", [user.to_json() for user in users_objetos])
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "Nenhum usuário encontrado")
    

#LISTAR UM USUARIO
@app.route("/users/<uuid>", methods=["GET"])
def seleciona_user(uuid):
    user_objeto = users.query.filter_by(uuid=uuid).first()
    user_json = user_objeto.to_json()
    
    return gera_response(200, "user", user_json)
    

#CADASTRAR USUARIO
@app.route("/users", methods =["POST"])
@jwt_required()
def cria_user():
    body = request.get_json()
    novo_uuid = str(uuid.uuid4())


    try:
        user = users(uuid=novo_uuid, name= body["name"], fancyname= body["fancyname"], document= body["document"], phone= body["phone"], email= body["email"], password= body["password"])
        db.session.add(user)
        db.session.commit()
        return gera_response(201, "user", user.to_json(), "Criado com Sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "Erro ao cadastrar")


#ATUALIZAR USUARIO
@app.route("/users/<uuid>", methods =["PUT"])
@jwt_required()
def atualizar_user(uuid):
    usuario_objeto = users.query.filter_by(uuid=uuid).first()
    body = request.get_json()

    try:
        if("name" in body):
            usuario_objeto.name = body["name"]
        if("fancyname" in body):
            usuario_objeto.fancyname = body["fancyname"]
        if("document" in body):
            usuario_objeto.document = body["document"]
        if("phone" in body):
            usuario_objeto.phone = body["phone"]
        if("email" in body):
            usuario_objeto.email = body["email"]
        if("password" in body):
            usuario_objeto.password = body["password"]

        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "user", usuario_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print("Erro", e)
        return gera_response(400, "user", {}, "Erro ao atualizar")

#DELETAR
@app.route("/users/<uuid>", methods=["DELETE"])
@jwt_required()
def deleta_user(uuid):
    usuario_objeto = users.query.filter_by(uuid=uuid).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "user", usuario_objeto.to_json(), "Desabilitado com sucesso")
    except Exception as e:
        print("Erro", e)
        return gera_response(400, "user", {}, "Erro ao desabilitar")