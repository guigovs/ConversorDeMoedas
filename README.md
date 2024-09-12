# Conversor de Moedas

Este projeto é um **Conversor de Moedas** que permite ao usuário selecionar uma moeda de origem e uma moeda de destino, e obter a cotação atual entre as duas. A interface gráfica foi desenvolvida utilizando a biblioteca **CustomTkinter** e as cotações são obtidas através de uma API pública.

## Funcionalidades

- Seleção de moeda de origem e destino.
- Exibição da cotação atual entre as moedas selecionadas.
- Lista de moedas disponíveis com seus códigos e nomes.
- Interface gráfica amigável e de fácil uso.

## Arquivos

- `main.py`: Arquivo principal que contém a interface gráfica do aplicativo.
- `pegar_cotacao.py`: Função responsável por buscar a cotação atual entre duas moedas usando a API **AwesomeAPI**.
- `pegar_moedas.py`: Funções que processam os arquivos XML contendo as informações sobre as moedas disponíveis e as conversões possíveis.

## Como Funciona

1. **Interface gráfica**: Utiliza a biblioteca `CustomTkinter` para criar a janela principal e todos os componentes gráficos (botões, labels, menus suspensos).
   
2. **Seleção de moedas**: O usuário escolhe uma moeda de origem e uma moeda de destino. A lista de moedas de destino é atualizada dinamicamente com base na moeda de origem selecionada.

3. **Cotação**: Ao clicar no botão "Converter", o sistema consulta a cotação atual entre as moedas selecionadas através da API **AwesomeAPI**.

4. **Exibição de resultado**: A cotação obtida é exibida na interface.

## Estrutura dos Arquivos XML

O projeto utiliza dois arquivos XML:

1. **moedas.xml**: Contém as informações sobre as moedas disponíveis (código e nome).
   
2. **conversoes.xml**: Contém as conversões possíveis entre as moedas (pares de moedas).

## Pré-requisitos

- Python 3.x
- Bibliotecas:
  - `customtkinter`
  - `requests`
  - `xmltodict`