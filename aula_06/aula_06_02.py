from selenium.webdriver import Firefox

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

# Usando tag type [attr=valor]
# nome = b.find_element_by_css_selector('[type="text"]')
# senha = b.find_element_by_css_selector('[type="password"]')
# btn = b.find_element_by_css_selector('[type="submit"]')

# Usando tag name [attr=valor]
# nome = b.find_element_by_css_selector('[name="nome"]')
# senha = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# Usando atributo * [attr*=valor]
# nome = b.find_element_by_css_selector('[name*="ome"]')
# senha = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="l0"]')

# Usando atributo | [attr|=valor]
# Bug: começa por n mas não é exatamente igual a n
# o operador |= espera n <espaço> <outro_elemento>
# operador que começa com um caractere: ^=
# nome = b.find_element_by_css_selector('[name|="n"]')
# senha = b.find_element_by_css_selector('[name|="s"]')
# btn = b.find_element_by_css_selector('[name|="l"]')

# Usando atributo ^ [attr^=valor]
nome = b.find_element_by_css_selector('[name^="n"]')
senha = b.find_element_by_css_selector('[name^="s"]')
btn = b.find_element_by_css_selector('[name^="l"]')

# ---------------------------------------------------------------------------- #

nome.send_keys('Eduardo')
senha.send_keys('batatinha123')
btn.click()

"""
nome=Eduardo&senha=batatinha123&l0c0=Enviar%21#
"""
