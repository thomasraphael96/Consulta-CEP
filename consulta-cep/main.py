from config_database import Endereco
import requests as chamadaAPI
import json

# variavel que armazena o CEP que o usuário digitar
cep = input("Digite um cep: ")

print('Procurando CEP informado...')

# realiza a chamada na API passando o CEP informado pelo usuário
respostaAPI = chamadaAPI.get("https://viacep.com.br/ws/%s/json/" %cep)

# validação do código de retorno da chamada
if respostaAPI.status_code == chamadaAPI.codes.ok:
    
    print('CEP encontrado...')
    
    #converte a resposta da chamada na API para um objeto do tipo json
    j = json.loads(respostaAPI.text)

    # criando o objeto do tipo Endereco() e abastecendo seus atributos
    endereco = Endereco()
    
    endereco.cep = j['cep']
    endereco.logradouro = j['logradouro']
    endereco.complemento = j['complemento']
    endereco.bairro = j['bairro']
    endereco.localidade = j['localidade']
    endereco.uf = j['uf']
    endereco.ddd = j['ddd']
    endereco.ibge = j['ibge']
    endereco.gia = j['gia']

    endereco.salvar()

else:
    print('CEP não encontrado')