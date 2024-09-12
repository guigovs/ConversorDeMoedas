import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f'https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}'
    requisicao = requests.get(link)
    # Converte a resposta da API para o formato JSON e extrai o valor da cotação (bid)
    cotacao = requisicao.json()[f'{moeda_origem}{moeda_destino}']['bid']    
    return cotacao
