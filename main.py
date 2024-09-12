import customtkinter as ctk
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Configurações iniciais da janela
ctk.set_appearance_mode('dark')  # Define o modo de aparência como "dark"
ctk.set_default_color_theme('dark-blue')  # Define o tema de cores padrão como "dark-blue"

janela = ctk.CTk()  # Cria a janela principal da aplicação
janela.geometry('500x500')  # Define o tamanho da janela

dic_conversoes_disponiveis = conversoes_disponiveis()  # Carrega um dicionário com as conversões disponíveis

# Criação de rótulos e campos de entrada
titulo = ctk.CTkLabel(janela, text='Conversor de Moedas', font=('', 20))  # Título do aplicativo
texto_moeda_origem = ctk.CTkLabel(janela, text='Selecione a moeda de origem')  # Rótulo para moeda de origem
texto_moeda_destino = ctk.CTkLabel(janela, text='Selecione a moeda de destino')  # Rótulo para moeda de destino

# Função para carregar as moedas de destino quando uma moeda de origem é selecionada
def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)  # Atualiza o menu de opções da moeda de destino
    campo_moeda_destino.set(lista_moedas_destino[0])  # Define a primeira moeda como selecionada por padrão

# Criação dos menus de opções para selecionar as moedas
campo_moeda_origem = ctk.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = ctk.CTkOptionMenu(janela, values=['Selecione uma moeda de origem'])

# Função que realiza a conversão de moeda
def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f'1 {moeda_origem} = {cotacao} {moeda_destino}')  # Exibe a cotação obtida

# Botão para acionar a conversão
botao_converter = ctk.CTkButton(janela, text='Converter', command=converter_moeda)

# Label para mostrar a cotação após a conversão
texto_cotacao_moeda = ctk.CTkLabel(janela, text='')

# Cria um quadro rolável para listar as moedas disponíveis
lista_moedas = ctk.CTkScrollableFrame(janela)

# Posicionamento dos elementos na janela usando o método pack
titulo.pack(padx=10, pady=15)
texto_moeda_origem.pack(padx=10, pady=5)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=5)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=5)
lista_moedas.pack(padx=10, pady=10)

# Preenche a lista de moedas disponíveis com seus códigos e nomes
moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = ctk.CTkLabel(lista_moedas, text=f'{codigo_moeda}: {nome_moeda}')
    texto_moeda.pack()  # Adiciona cada moeda como um rótulo no quadro rolável

# Inicia o loop principal da interface gráfica
janela.mainloop()
