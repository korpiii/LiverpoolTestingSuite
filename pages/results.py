#This module contains LiverpoolResultsPage, the page object for the Liverpool results page.

from selenium.webdriver.common.by import By


class LiverpoolResultsPage:
  PRODUCT_DESCRIPTION = (By.CLASS_NAME, 'm-product__listingPlp')
  SEARCH_INPUT = (By.ID, "mainSearchbar")
  PRODUCT_UNVAILABLE = (By.CLASS_NAME, 'o-nullproduct-title-query')
  PRODUCT_TITLE = (By.CLASS_NAME, 'a-product__information--title')


 # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def query_results(self):
    product_names = []
    descriptions = self.browser.find_elements(*self.PRODUCT_DESCRIPTION)
    for description in descriptions:
        product_names.append(description.text.lower())
    return product_names

  def query_results_unavailable(self):
    error_message = self.browser.find_element(*self.PRODUCT_UNVAILABLE).text.lower()
    return error_message

  def query_single_product_result(self):
    product_name = self.browser.find_element(*self.PRODUCT_TITLE).text.lower()
    return product_name

  def title(self):
    return self.browser.title

  def get_url(self):
    return self.browser.current_url
