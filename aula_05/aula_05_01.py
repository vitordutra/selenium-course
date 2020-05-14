#! venv/bin/python

from selenium.webdriver import Firefox

firefox = Firefox()

url = "http://selenium.dunossauro.live/aula_05_a.html"

firefox.get(url)

div_py = firefox.find_element_by_id('python')
div_hk = firefox.find_element_by_id('haskell')

print(div_hk.text)

firefox.quit()
