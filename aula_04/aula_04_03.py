from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse


def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto 'text'

    Argumentos:
        - browser = Instância do browser [firefox, chrome, ...]
        - tag = tag onde o texto será procurado
        - text = conteúdo que deve estar na tag
    """

    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """ Encontrar o elemento 'a' com o link 'link'.


    Arguments:
        browser {[webdriver]} -- [Instância do browser]
        link {[webdriber]} -- [link que será procurado em todas as tags 'a']
    """

    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04_b.html")

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for texto in nomes_das_caixas:
    find_by_text(browser, 'div', texto).click()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.back()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.forward()
