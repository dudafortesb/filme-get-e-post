from models.filme_models import Filme  # Importa o modelo Filme
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os filmes
def get_filmes():
    filmes = Filme.query.all()  # Busca todos os filmes no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de filmes.',
            'dados': [filme.json() for filme in filmes]  # Converte os objetos de filme para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para criar um novo filme
def create_filme(filme_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in filme_data for key in ['título', 'gênero', 'duração','ano de lançamento','diretor']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Título, Gênero, Duração, Ano de lançamento e Diretor são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo filme
    novo_filme=Filme(
        título =filme_data['titulo'],
        genero =filme_data['genero'],
        duração =filme_data['duração'],
        ano de lançamento =filme_data['ano de lançamento'],

    )
    db.session.add(novo_filme)# Adiciona o novo filme ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo filme
    response = make_response(
        json.dumps({
            'mensagem': 'Filme cadastrado com sucesso.',
            'filme': novo_filme.json() # Retorna os dados do filme cadstrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response