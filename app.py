import os
import pandas as pd
from os import walk
from bs4 import BeautifulSoup

print("Iniciando processamento de notas fiscais.")

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    f.extend(filenames)
    break

rows = ['produto', 'ncm', 'unidade', 'quantidade', 'valorUnidade',
        'valorProduto', 'destCNPJ', 'comprador', 'dataEmissao']
dataList = [rows]

for xml in f:
    if("xml" in xml):
        with open(xml, 'r') as f:
            print("Processando", xml)
            data = f.read()
            soup = BeautifulSoup(data, 'lxml')
            products = soup.find_all('prod')
            for product in products:
                try:
                    dataList.append([product.find('xprod').getText(),
                                 product.find('ncm').getText(),
                                 product.find('ucom').getText(),
                                 product.find('qcom').getText(),
                                 product.find('vuncom').getText(),
                                 product.find('vprod').getText(),
                                 soup.find('dest').find('cnpj').getText(),
                                 soup.find('dest').find('xnome').getText(),
                                 soup.find('dhemi').getText()])
                    pd.DataFrame(dataList).to_csv("vendas.csv")
                except:
                    pass

print("Processamento finalizado com sucesso")

