from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse

browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04_b.html")


parsed_url = urlparse(browser.current_url)
