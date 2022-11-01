#This module contains LiverpoolHomePage, the page object for the Liverpool results page.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LiverpoolHomePage:

  #url
  URL = "https://www.liverpool.com.mx/tienda/home"
  
  #locators
  SEARCH_INPUT = (By.ID, 'mainSearchbar')

  #initializer
  def __init__(self, browser):
    self.browser = browser

  #interaction methods
  def load(self):
    self.browser.get(self.URL)
    
  def search(self, product):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(product +  Keys.RETURN)
    

