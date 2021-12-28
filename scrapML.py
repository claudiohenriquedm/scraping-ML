import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []
url = 'https://lista.mercadolivre.com.br/'
busca = 'iphone'
resposta = requests.get(url + busca)
htmlbs = BeautifulSoup(resposta.content, 'html.parser')
produtos = htmlbs.findAll('div', attrs={'class': 'ui-search-result__content-wrapper'})
for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    preco = produto.find('span', attrs={'class': 'price-tag-fraction'})
    lista_produtos.append([titulo.text, preco.text])
    # print(f'Nome: {titulo.text}')
    # print(f'Preço: R$ {preco.text}')
    # print()
tabela = pd.DataFrame(lista_produtos, columns=['Descrição', 'Preço'])
tabela.to_csv('tabelafinal.csv', index=False)

