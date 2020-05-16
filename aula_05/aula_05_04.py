#! venv/bin/python

from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

firefox = Firefox()

url = "http://selenium.dunossauro.live/aula_05.html"

firefox.get(url)

sleep(1)

# --------------------------------------------------------------------- #

# nome, email, senha, telefone, btn


def preencher_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


dict_test = {
    'nome': "João",
    'email': "joao@joao.com",
    'senha': "senha123",
    'telefone': "987654321"
}

preencher_form(firefox, **dict_test)

parsed_url = urlparse(firefox.current_url)

sleep(1)

# ? query string
"""
https://selenium.dunossauro.live/aula_05.html
?
nome=Jo%C3%A3o
&
email=joao%40joao.com
&
senha=senha123
&
telefone=987654321
&
btn=Enviar%21#
"""

result_text = firefox.find_element_by_id('result').text
corrected_text = result_text.replace('\'', "\"")
dict_result = loads(corrected_text)

# assert == garanta

assert dict_result == dict_test
