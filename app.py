import os
import csv
from os import walk
from bs4 import BeautifulSoup

print("Iniciando processamento de notas fiscais.")

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    f.extend(filenames)
    break

rows = ['produto', 'ncm', 'unidade', 'quantidade', 'valorUnidade',
        'valorProduto', 'destCNPJ/destCPF', 'comprador', 'dataEmissao']
dataList = [rows]

for xml in f:
    if("xml" in xml):
        with open(xml, 'r') as f:
            print("Processando", xml)
            data = f.read()
            soup = BeautifulSoup(data, 'lxml')
            products = soup.find_all('prod')
            def check_cnpj(self):
                    cnpj = soup.find('dest').find('cnpj')
                    if cnpj:
                        return 'cnpj'
                    else:
                        return 'cpf'
            for product in products:
                try:
                    dataList.append([product.find('xprod').getText(),
                                 product.find('ncm').getText(),
                                 product.find('ucom').getText(),
                                 product.find('qcom').getText(),
                                 product.find('vuncom').getText(),
                                 product.find('vprod').getText(),
                                 soup.find('dest').find(check_cnpj).getText(),
                                 soup.find('dest').find('xnome').getText(),
                                 soup.find('dhemi').getText()])
                    with open('vendas.csv', 'w') as f:
                        write = csv.writer(f)
                        
                        write.writerows(dataList)
                except Exception as e:
                    print({xml},repr(e))
                except:
                    pass

print("Processamento finalizado com sucesso")
