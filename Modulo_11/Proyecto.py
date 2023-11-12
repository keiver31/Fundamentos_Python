import bs4
import requests


resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

sopa=bs4.BeautifulSoup(resultado.text, 'lxml')


#columna_lateral= sopa.select('p')[3].get_text()

columna_lateral= sopa.select('.section p')

for p in columna_lateral:
    print(p.getText())
