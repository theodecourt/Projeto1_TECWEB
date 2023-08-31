import json
from database import Database
from database import Note

db = Database('banco')

def extract_route(request):
    return request.split('\n')[0].split(" ")[1][1:]


def read_file(path):
    with open(path, "rb") as file:
        return file.read()
    
def load_data(): #precisa pegar informações do
    base = db.get_all()
    base_arrumado = []
    for note in base:
        dic = {}
        dic['titulo'] = note.title
        dic['detalhes'] = note.content
        base_arrumado.append(dic)

    return base_arrumado

def load_template(nome_arquivo):
    with open('templates/' + nome_arquivo, 'r') as arquivo:
        return arquivo.read()

def adiciona_note(anotacao):
    try:
        db.add(Note(title=anotacao['titulo'], content=anotacao['detalhes']))
        
    except Exception as e:
        print("Ocorreu um erro:", str(e))

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    if headers:
        response += headers + '\n'
    response += '\n' + body
    return response.encode()
