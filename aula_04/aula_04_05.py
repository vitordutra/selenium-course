"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""
from selenium.webdriver import Firefox
from time import sleep
# Pretty Print
from pprint import pprint
browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04.html")

sleep(2)

"""
Parte 1
browser.get(resultado_1['Aula 3'])
browser.get(resultado_1['Aula 4'])
"""

aside = browser.find_element_by_tag_name('aside')
aside_ancoras = aside.find_elements_by_tag_name('a')

resultado_1 = {}

for ancora in aside_ancoras:
    resultado_1[ancora.text] = ancora.get_attribute('href')

pprint(resultado_1)

"""
Parte 2
"""
