import pandas as pd
import requests as r
from bs4 import BeautifulSoup 
import time
import numpy as np

df = pd.DataFrame(columns=['bairro', 'CEP', 'page', 'error'])

page_init = 1
page_end = 5000

try:
    for i in range(page_init, page_end):

        time.sleep(25)

        result = r.get(f"https://cep.guiamais.com.br/busca/rio+de+janeiro-rj?page={i}")

        soup = BeautifulSoup(result.text, 'html.parser')

        div = soup.find("div", {"class": "col-md-8"})

        td_without_class = div.find_all("td")

        td = div.find_all("td", {"class": "hidden-lg"})

        k = 1
        while k < 130:
            try:
                print(str(td_without_class[k]).split('>')[2].split('<')[0])
                print(str(td_without_class[k+3]).split('>')[2].split('<')[0])

                new_line = pd.DataFrame([[str(td_without_class[k]).split('>')[2].split('<')[0], str(td_without_class[k+3]).split('>')[2].split('<')[0], i, np.nan]],
                                            columns=['bairro', 'CEP', 'page', 'error'])

                df = df.append(new_line)

                k = k + 5
            except:
                break

        df.reset_index(drop=True, inplace=True)

        df.to_csv(f"C:\\Users\\bru-c\\Documents\\Python Projects\\extract-cep\\df_{page_init}_{page_end}.csv", 
                    index=False, header=True, encoding='cp1252', sep=';', mode='a')


    print(df)

    #df.to_csv(f"C:\\Users\\bru-c\\Documents\\Python Projects\\extract-cep\\df_{page_init}_{page_end}.csv", index=False, header=True, encoding='cp1252', sep=';')

except Exception as error:
    new_line = pd.DataFrame([[np.nan, np.nan, i, error]], columns=['bairro', 'CEP', 'page', 'error'])

    df.to_csv(f"C:\\Users\\bru-c\\Documents\\Python Projects\\extract-cep\\df_{page_init}_{page_end}.csv", 
                index=False, header=True, encoding='cp1252', sep=';', mode='a')

    #for link in td_without_class:
    #    print(link.a)

    #print(i, '/n')
    #print(td_without_class)
    #print(str(td.a).split(',')[0].split('>')[1])

#print(len(div.find_all("td")))

