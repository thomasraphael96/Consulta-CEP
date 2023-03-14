from config_database import Endereco
import requests
import json
import time

# tempo em segundos utilizado na função time.sleep(seconds)
seconds = 2

# variavel que armazena o CEP que o usuário digitar
cep_informado = input("Digite um CEP: ")
cep_informado = cep_informado.replace(" ","")
cep_informado = cep_informado.replace("-","")
cep_informado = cep_informado.replace(".","")

print('Procurando CEP informado...')
time.sleep(seconds)

# realiza a chamada na API passando o CEP informado pelo usuário
respostaAPI = requests.get("https://viacep.com.br/ws/%s/json/" %cep_informado)

# converte a resposta da chamada na API (JSON) para um dicionário
j = json.loads(respostaAPI.text)

# valida se existe o parâmetro 'erro' dentro do dicionário
jErro = 'erro' in j

# se a chamada for bem sucedida e o CEP informado for válido
if respostaAPI.status_code == 200 and jErro == False:
    
    print('CEP encontrado...')
    
    # criando o objeto do tipo Endereco() e abastecendo seus atributos
    info_cep = Endereco()
    
    info_cep.cep = j['cep']
    info_cep.logradouro = j['logradouro']
    info_cep.bairro = j['bairro']
    info_cep.localidade = j['localidade']
    info_cep.uf = j['uf']
    info_cep.ddd = j['ddd']

    time.sleep(seconds)

    # chama o método que insere os dados no banco de dados
    info_cep.inserir_dados()

# se a chamada for bem sucedida mas o CEP informado for inválido (ex.: 99999999)
elif respostaAPI.status_code == 200 and jErro == True:
    print("=========== ERRO ===========")
    print("CEP inexistente")

# se a chamada for mal sucedida porque o CEP informado não tiver 8 dígitos
elif respostaAPI.status_code == 400 and len(cep_informado) != 8:
    print("=========== ERRO ===========")
    print("CEP informado não contém 8 dígitos. Tente novamente.")

# se a chamada for mal sucedida porque o CEP informado contém letras
elif respostaAPI.status_code == 400 and cep_informado.isnumeric():
    print("=========== ERRO ===========")
    print("CEP informado deve conter somente números. Tente novamente.")

# se a chamada for mal sucedida e o motivo não está mapeado
else:
    print("=========== ERRO ===========")
    print("Erro não mapeado")