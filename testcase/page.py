from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = 'q'  #es como en python.org se llama el sitio para buscar

class GoButtonElement(BasePageElement):
    locator = 'go'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):


    search_text_element = SearchTextElement()

    def is_title_matches(self):
        #if the title of the page matches what we want to match
        return 'Python' in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return 'No results found.' not in self.driver.page_source