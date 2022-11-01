import random
from pages.results import LiverpoolResultsPage
from pages.home import LiverpoolHomePage

products_list = ["zapato", "televisión", "celular", "vasos", "lavadora", "perfume"]
products_list_description = ["televisión samsung", "zapato negro", "reloj citizen"]
unvailable_products = ["omeprazol", "tajin"]
products_list_full_description = ["Mesa de comedor Lottus Ginger de vidrio", "Lámpara de mesa Gaia Nité", "Gomitas Lunch Bag E-Frutti 77.5 g"]
invalid_chars = [".",","," ","  ","o"]


def test_simple_product_query(browser):
  home_page = LiverpoolHomePage(browser)
  results_page = LiverpoolResultsPage(browser)
  product = random.choice(products_list_description)
  product = random.choice(products_list)

  # Given the Liverpool home page is displayed
  home_page.load()

  # When the user searches for a given product
  home_page.search(product)

  # Then the search results contains products related to query

  products = results_page.query_results()
  matches = [s for s in products if product in s]
  assert len(matches) > 0


def test_product_search_with_description(browser):
  home_page = LiverpoolHomePage(browser)
  results_page = LiverpoolResultsPage(browser)
  product = random.choice(products_list_description)

  # Given the Liverpool home page is displayed
  home_page.load()

  # When the user searches for a given product with some description
  home_page.search(product)

  # Then the search results contains products related to query

  products = results_page.query_results()
  matches = [s for s in products if product in s]
  assert len(matches) > 0


def test_unvailable_products(browser):
  home_page = LiverpoolHomePage(browser)
  results_page = LiverpoolResultsPage(browser)
  product = random.choice(unvailable_products)

  # Given the Liverpool home page is displayed
  home_page.load()

  # When the user searches for a given unavailable product
  home_page.search(product)

  # Then the search results contains an error message on product unavailable

  message = results_page.query_results_unavailable()
  assert product in message

def test_product_search_with_full_description(browser):
  home_page = LiverpoolHomePage(browser)
  results_page = LiverpoolResultsPage(browser)
  product = random.choice(products_list_full_description)

  # Given the Liverpool home page is displayed
  home_page.load()

  # When the user searches for a given product with full description
  home_page.search(product)

  # Then the search results redirects to that product
  product_result = results_page.query_single_product_result()
  assert product.lower() in product_result


def test_product_search_using_invalid_chars(browser):
  home_page = LiverpoolHomePage(browser)
  results_page = LiverpoolResultsPage(browser)
  product = random.choice(invalid_chars)

  # Given the Liverpool home page is displayed
  home_page.load()

  # When the user enters invalid characters
  home_page.search(product)

  # Then the page stays the same
  current_url = results_page.get_url()
  assert "tienda/home" in current_url
