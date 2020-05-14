#! venv/bin/python

from selenium.webdriver import Firefox
from time import sleep

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


preencher_form(firefox, "João", "joao@joao.com", "senha123", "987654321")


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
