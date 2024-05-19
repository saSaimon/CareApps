import time

from behave import given, then, when
from dotenv import load_dotenv
import os

load_dotenv()
username = os.environ.get('BT_USER')
password = os.environ.get('BT_PASS')

# website = 'https://staging.careapps.co.uk/auth/login'


@given('User can enter to the {website}')
def enter_into_website(context, website):
    try:
        context.app.login_page.enter_to_website(url=website)
    except Exception as e:
        context.logger.error(f"Error entering website {website}: {e}")
        raise


@when('User will input valid email')
def enter_valid_email(context):
    context.app.login_page.input_email(username)


@when('User will input valid password')
def enter_valid_password(context):
    context.app.login_page.input_password(password)


@when('User will input invalid email')
def enter_valid_email(context):
    context.app.login_page.input_email(username + 'abc')


@when('User will input invalid password')
def enter_valid_password(context):
    context.app.login_page.input_password(password + 'abc')


@when('User will click remember me toggle button')
def click_remember_me_button(context):
    context.app.login_page.click_remember_me_button()


@when('User will click login button')
def click_login_button(context):
    context.app.login_page.click_login_button()


@then('User will verify Login successful if they saw CareApp Logo on the up right corner')
def verify_logo(context):
    context.app.login_page.is_logo_present()


@then('User will see No User Found pop up modal')
def verify_pop_up(context):
    context.app.login_page.login_failed(context=context)

@then("User will see password is invalid")
def pass_invalid(context):
    context.app.login_page.password_invalid(context=context)