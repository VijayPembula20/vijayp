import pandas as pd
from behave import given, when, then
from behave import *

from pages.car_page import CarPage

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
