#! ./venv/bin/python

# Crie um programa em selenium que
# * Gere um diciconário onde a chave é a tag h1
#   * O valor deve ser um novo dicionário
#   * Cada chave do valor deverá ser o valor de 'atributo'
#   * Cada valor deve ser o texto contido no elemento

from selenium.webdriver import Chrome

url = "https://selenium.dunossauro.live/exercicio_01.html"

browser = Chrome()

browser.get(url)

browser.implicitly_wait(2)

# ------------------------------------------------------------ #

h1 = browser.find_element_by_tag_name('h1').text

list_p = browser.find_elements_by_tag_name('p')

attributes_dict = {}

attrs = []
texts = []

for p in list_p:
    attrs.append(p.get_attribute('atributo'))

for p in list_p:
    texts.append(p.text)

dict_p = dict(zip(attrs, texts))

dict_sol = {h1: dict_p}

print(dict_sol)

browser.quit()
