#! ./venv/bin/python

from selenium.webdriver import Chrome

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Chrome()

browser.get(url)

browser.implicitly_wait(3)

a = browser.find_element_by_tag_name('a')
p = browser.find_elements_by_tag_name('p')

for click in range(10):
    a.click()


# browser.quit()
