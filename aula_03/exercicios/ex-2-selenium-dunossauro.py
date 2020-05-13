#! ../venv/bin/python

from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/exercicio_02.html'

browser = Firefox()

browser.get(url)

sleep(1)

# Crie um programa com selenium que
# * Jogue o jogo
# * Quando você ganhar o script deve parar de ser executado

a = browser.find_element_by_tag_name('a')

resultado = "Você ganhou"

msg = ""

while resultado not in msg:
    a.click()
    sleep(0.1)
    msg = browser.find_elements_by_tag_name('p')[-1].text
