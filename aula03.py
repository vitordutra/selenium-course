#! ./venv/bin/python

from selenium.webdriver import Chrome

url = "https://curso-python-selenium.netlify.app/aula_03.html"

browser = Chrome()

browser.get(url)

browser.implicitly_wait(3)

a = browser.find_element_by_tag_name('a')

for click in range(10):
    p = browser.find_elements_by_tag_name('p')
    a.click()
    print(f"Valor de p: {p[-1].text} valor do click: {click}")

    print(f"Os valores são iguais {int(p[-1].text) == click}")


# browser.quit()
