from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Feature correspondante
scenarios("../features/search_on_google.feature")

google = "https://www.google.fr"
TIMEOUT = 5

@given(("je suis sur la page d'accueil de Google"))
def google_homepage(browser):
    pass

@when(parsers.parse("je recherche le jeu \'{search}\'"))
def search_query(browser, search):
    pass

@then(parsers.parse("je trouve le lien Google Play pour \'{search}\' dans les {research_area:d} premiers résultats de recherche"))
def verify_results(browser, search, research_area):
    pass