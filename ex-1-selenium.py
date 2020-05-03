#! ./venv/bin/python

# Crie um programa em selenium que
# * Gere um diciconário onde a chave é a tag h1
#   * O valor deve ser um novo dicionário
#   * Cada chave do valor deverá ser o valor de 'atributo'
#   * Cada valor deve ser o texto contido no elemento

from selenium.webdriver import Chrome

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Chrome()

browser.get(url)

browser.implicitly_wait(2)

dict_h1 = {}
dict_p = {}

h1 = browser.find_element_by_tag_name('h1')

list_p = browser.find_elements_by_tag_name('p')

for i in range(len(list_p)):
    dict_p[list_p[i].get_attribute('atributo')] = list_p[i].text

dict_h1 = {h1.tag_name: dict_p}

print(dict_h1)