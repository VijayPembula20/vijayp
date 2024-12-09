import pandas as pd
import os
from behave import given, when, then
from behave import *
from selenium.webdriver.chrome import webdriver

from pages.car_page import CarPage
from utils.file_handler import extract_registration_numbers, load_expected_output

use_step_matcher("re")


@given("I navigate to the car valuation website")
def step_navigate_to_website(context):
    context.logger.info(f'STEP: {context.step_name}')
    context.page = CarPage()
    context.page.open()
    # driver.sleep(10)


@when('I search for a car with registration with "(?P<registration>.+)"')
def step_impl(context, registration):
    context.logger.info(f'STEP: {context.step_name}')

    # context.page = registration
    context.page.enter_registration(registration)
    context.car_info = context.page.get_car_details()


@step('I enter the car "(?P<mileage>.+)"')
def step_impl(context, mileage):
    context.logger.info(f'STEP: {context.step_name}')

    context.page.enter_mileage(mileage)
    context.car_info = context.page.enter_mileage()

@then("the car details should match the expected output")
def step_impl(context):
    context.logger.info(f'STEP: {context.step_name}')
    expected_data = pd.read_csv('data/expected_output.csv').set_index("registration")
    expected_info = expected_data.loc[context.car_info["registration"]].to_dict()
    assert context.car_info == expected_info, f"Mismatch: {context.car_info} != {expected_info}"


@given('I have an input file {input_file}')
def step_impl(context, input_file):
    context.input_file = input_file
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    context.car_valuation_page = CarPage(context.driver)



@when("I extract vehicle registration numbers")
def step_impl(context):
    context.reg_numbers = extract_registration_numbers(context.input_file)



@step("I fetch valuations from the car valuation website")
def step_impl(context):
    context.fetched_results = {}
    for reg in context.reg_numbers:
        try:
            context.fetched_results[reg] = context.car_valuation_page.fetch_valuation(reg)
        except Exception as e:
            context.fetched_results[reg] = f"Error: {e}"


@then('I compare the fetched valuations with "car_output\.txt"')
def step_impl(context, output_file):
    expected_results = load_expected_output(output_file)
    context.mismatches = []
    for reg, fetched in context.fetched_results.items():
        expected = expected_results.get(reg)
        if fetched != expected:
            context.mismatches.append((reg, fetched, expected))


@step("I should see all mismatches highlighted")
def step_impl(context):
    if context.mismatches:
        print("Mismatches found:")
        for reg, fetched, expected in context.mismatches:
            print(f"Reg: {reg} | Fetched  {fetched} | Expected: {expected}")
        assert False, "Some valuations did not match expected results."
    else:
        print("No mismatches found.")
        assert True, "No mismatches found."
    context.driver.quit()


@given('I have an input file name "car_input\.txt"')
def step_impl(context, car_input):
    context.car_input = car_input
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    context.car_valuation_page = CarPage(context.driver)