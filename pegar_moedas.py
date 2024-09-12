import xmltodict

def nomes_moedas():
    # Abre o arquivo 'moedas.xml' no modo de leitura binária
    with open('moedas.xml', 'rb') as arquivo_moedas:
        # Converte o conteúdo XML do arquivo para um dicionário Python usando xmltodict
        dic_moedas = xmltodict.parse(arquivo_moedas)
    # Acessa o conteúdo do dicionário que está dentro da chave 'xml'
    moedas = dic_moedas['xml']
    return moedas

def conversoes_disponiveis():
    # Abre o arquivo 'conversoes.xml' no modo de leitura binária
    with open('conversoes.xml', 'rb') as arquivo_conversoes:
        # Converte o conteúdo XML do arquivo para um dicionário Python usando xmltodict
        dic_conversoes = xmltodict.parse(arquivo_conversoes)
    # Acessa o conteúdo do dicionário que está dentro da chave 'xml'
    conversoes = dic_conversoes['xml']
    dic_conversoes_disponiveis = {}
    # Itera sobre as conversões disponíveis no dicionário
    for par_conversao in conversoes:
        # Divide o par de conversão em moeda de origem e moeda de destino
        moeda_origem, moeda_destino = par_conversao.split('-')
        # Verifica se a moeda de origem já existe no dicionário de conversões
        if moeda_origem in dic_conversoes_disponiveis:
            # Se existir, adiciona a moeda de destino à lista de conversões disponíveis
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            # Se não existir, cria uma nova entrada para a moeda de origem com a moeda de destino
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]    
    return dic_conversoes_disponiveis
