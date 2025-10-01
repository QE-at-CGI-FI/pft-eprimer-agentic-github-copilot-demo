import pytest
from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Page

HOME = "https://qe-at-cgi-fi.github.io/eprime/"

_text_input = "#test_field"
_test_button = "#test_button"
_number_1 = "#test_number_1"
_number_2 = "#test_number_2"
_number_3 = "#test_number_3"

@scenario('../features/eprimer.feature', 'Eprime analysis')
def test_eprime_analysis():
    pass

@scenario('../features/eprimer.feature', 'Incorrect Eprime analysis')
def test_incorrect_eprime_analysis():
    pass

@scenario('../features/eprimer.feature', 'Eprime samples are correctly analyzed')
def test_eprime_samples_correctly_analyzed():
    pass

@given("the eprime page is displayed")
def eprime_home(page: Page):
    page.goto(HOME)

@when(parsers.parse('user analyses sentence {phrase}'))
def analyze_phrase(page: Page, phrase):
    page.fill(_text_input, phrase)
    page.click(_test_button)

@then(parsers.parse('user learns sentence has {violations} be-verbs, {discouraged} possible be-verbs and total {words} words'))
def search_results(page: Page, words, violations, discouraged):
    assert page.inner_text(_number_1) == words
    assert page.inner_text(_number_2) == violations
    assert page.inner_text(_number_3) == discouraged