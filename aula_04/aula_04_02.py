from selenium.webdriver import Firefox


def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto 'text'

    Argumentos:
        - browser = Instância do browser [firefox, chrome, ...]
        - tag = tag onde o texto será procurado
        - text = conteúdo que deve estar na tag
    """

    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """ Encontrar o elemento 'a' com o link 'link'.


    Arguments:
        browser {[webdriver]} -- [Instância do browser]
        link {[webdriber]} -- [link que será procurado em todas as tags 'a']
    """

    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04_a.html")


#elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')
