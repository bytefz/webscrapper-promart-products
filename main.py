from bs4 import BeautifulSoup as bs
import requests
from constants import _URL, _AGENT
import pandas as pd


def get_url(url_prefix):
    cont = 1
    while cont < 11:
        url = url_prefix + str(cont)
        cont += 1
        yield url


def list2xlsx(list_name, list_price, list_marca):
    df = pd.DataFrame(
        {'Nombre': list_name, 'Precio': list_price, 'Marca': list_marca})
    df.to_excel('cables_precio.xlsx', index=False, sheet_name="Precios")
    return df


def main():

    list_name_product = []
    list_price_product = []
    list_marca_product = []

    urls = get_url(_URL)
    for i in urls:
        r = requests.get(i, headers=_AGENT)
        soup = bs(r.content, 'html.parser')
        for i, j, k in zip(soup.find_all(class_='productName'),
                           soup.find_all(class_='sin-fto'),
                           soup.find_all(class_='brand js-brand')):
            list_name_product.append(i.text)
            list_price_product.append(j.text)
            list_marca_product.append(k.text)

    print(list2xlsx(list_name_product, list_price_product, list_marca_product))


if __name__ == "__main__":
    main()
