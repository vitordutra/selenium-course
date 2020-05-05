from selenium.webdriver import Firefox


browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04_a.html")

lista_nao_ordenada = browser.find_element_by_tag_name('ul')

lis = lista_nao_ordenada.find_elements_by_tag_name('li')

lis[0].find_element_by_tag_name('a').text


"""

1. buscamos ul
2. buscamos todos li
3. no primeiro li, buscamos a e pegamos o seu texto

"""
