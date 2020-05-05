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

list_p = browser.find_elements_by_tag_name('p')

h1 = browser.find_element_by_tag_name('h1').text

attributes_dict = {}

# Outra solução:
# Parecida com a minha mas menos "convoluted"
# Em vez de usar os índices da lista,
# Pega cada atributo de cada p individualmente,
# e adiciona no dict

for p in list_p:
    attributes_dict[p.get_attribute('atributo')] = p.text

dict_h1 = {h1: attributes_dict}

print(dict_h1)

browser.close()
