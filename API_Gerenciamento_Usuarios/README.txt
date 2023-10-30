# API de Gerenciamento de Usuários

Esta é uma API simples para gerenciamento de usuários, desenvolvida em Python com o framework Flask e usando um banco de dados MySQL para armazenar informações de usuários. Ela fornece várias funcionalidades, incluindo autenticação, listagem, criação, atualização e desativação de usuários.

## Requisitos

Certifique-se de ter o Python instalado na sua máquina. Além disso, instale as dependências necessárias listadas no arquivo `requirements.txt` usando o comando:

## Não se esqueça de criar a tabela no MySQL

CREATE TABLE users (
    uuid CHAR(36) NOT NULL,
    name VARCHAR(20) NOT NULL,
    fancyname VARCHAR(20) NOT NULL,
    document CHAR(11) NOT NULL,
    phone CHAR(11) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password CHAR(30) NOT NULL,
    PRIMARY KEY (uuid),
    UNIQUE KEY (document),
    UNIQUE KEY (phone),
    UNIQUE KEY (email)
);


```shell
pip install -r requirements.txt


Configuração
Banco de dados MySQL:
Certifique-se de que você tenha um servidor MySQL em execução e ajuste as configurações de conexão no arquivo app.py conforme necessário.

Para utilizar as funções "Cadastrar usuário, atualizar usuário e deletar usuário é necessário fazer a autenticação Baerer Token

Uso
Autenticação/Login
Endpoint: /authenticate
Método: POST
Descrição: Rota responsável pela autenticação do usuário. O login pode ser realizado com e-mail, documento ou telefone.

Listagem de Usuários
Endpoint: /users
Método: GET
Descrição: Rota para listar usuários com busca simples, filtro e ordenação.

Cadastro de Usuário
Endpoint: /users
Método: POST
Descrição: Rota responsável por cadastrar novos usuários.
Listagem de um Único Usuário
Endpoint: /users/<uuid>

Método: GET
Descrição: Rota responsável por listar dados de um usuário específico filtrando por UUID.

Atualização de Usuário
Endpoint: /users/<uuid>
Método: PUT
Descrição: Rota para atualizar dados de um usuário por UUID.

Desabilitar Usuário
Endpoint: /users/<uuid>
Método: DELETE
Descrição: Rota para desabilitar um usuário por UUID.
Exemplos de Uso
Certifique-se de ajustar as URLs e os dados de acordo com suas necessidades específicas.


Autenticação/Login
POST /authenticate
{
    "email": "exemplo@email.com",
    "password": "senha"
}

Listagem de Usuários
GET /users?q=termo_de_pesquisa&filter=valor_do_filtro&order_type=asc

Cadastro de Usuário
POST /users
{
    "uuid": "uuid_aleatorio", // a linha UUID É APENAS UM EXEMPLO, NÃO PRECISA POR POIS ELA É GERADA AUTOMATICAMENTE
    "name": "Nome do Usuário",
    "fancyname": "Apelido",
    "document": "12345678901",
    "phone": "9876543210",
    "email": "novousuario@email.com",
    "password": "novasenha"
}

Atualização de Usuário
PUT /users/uuid_do_usuario
{
    "name": "Novo Nome",
    "fancyname": "Novo Apelido",
    "document": "9876543210",
    "phone": "12345678901",
    "email": "novousuario_atualizado@email.com",
    "password": "novasenha_atualizada"
}

Desabilitar Usuário
DELETE /users/uuid_do_usuario