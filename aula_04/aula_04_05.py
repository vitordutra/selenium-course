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


def get_links(browser, element):
    """
    pega todos os links dentro de um elemento
        - browser = instância do navegador
        - element = webelement ['aside', main, body, ul, ol]
    """
    resultado = {}
    element = browser.find_element_by_tag_name(element)
    anchors = element.find_elements_by_tag_name('a')

    for anchor in anchors:
        resultado[anchor.text] = anchor.get_attribute('href')

    return resultado


sleep(2)

"""
Parte 1
browser.get(resultado_1['Aula 3'])
browser.get(resultado_1['Aula 4'])
"""

aulas = get_links(browser, 'aside')

pprint(aulas)

"""
Parte 2
"""

exercicios = get_links(browser, 'main')

pprint(exercicios)

browser.get(exercicios['Exercício 3'])
