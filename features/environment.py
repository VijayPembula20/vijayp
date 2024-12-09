from selenium import webdriver
from pages.car_page import CarPage


def before_all(context):
    context.browser = webdriver.Chrome()


def after_all(context):
    context.browser.quit()