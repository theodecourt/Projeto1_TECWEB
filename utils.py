import json

def extract_route(request):
    return request.split('\n')[0].split(" ")[1][1:]


def read_file(path):
    with open(path, "rb") as file:
        return file.read()
    
def load_data(ar_json):
    with open('data/' + ar_json, 'r') as arquivo:
        return json.load(arquivo)

def load_template(nome_arquivo):
    with open('templates/' + nome_arquivo, 'r') as arquivo:
        return arquivo.read()

def adiciona_note(anotacao):
    try:
        # Carregar o conteúdo existente do arquivo JSON
        with open('data/notes.json', 'r') as file:
            data = json.load(file)
        
        print(data)
        # Criar um novo objeto com as chaves "titulo" e "detalhes"
        nova_receita = {
            "titulo": anotacao['titulo'],
            "detalhes": anotacao['detalhes']
        }
        
        # Adicionar o novo objeto à lista existente
        data.append(nova_receita)
        
        # Escrever o conteúdo atualizado de volta ao arquivo JSON
        with open('data/notes.json', 'w') as file:
            json.dump(data, file, indent=4)
        
    except Exception as e:
        print("Ocorreu um erro:", str(e))

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    if headers:
        response += headers + '\n'
    response += '\n' + body
    return response.encode()
