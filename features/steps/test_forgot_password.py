from behave import given, then, when
from time import sleep


@when('User will click forgot password button')
def click_forgot_password(context):
    context.app.login_page.click_forgot_pass_link()


@when('User will input {email} in forgot password page')
def input_email_in_forgot_password_page(context, email):
    context.app.forgot_password_page.type_email_to_email_address(email)


@when('User will click send now button')
def user_click_send_now_button(context):
    context.app.forgot_password_page.click_send_now_button()


@then('User will verify the email is sent and a success text is shown')
def user_will_verify_text(context):
    context.app.forgot_password_page.verify_text_email_sent(context=context)


@then('User will see email is not valid validation message')
def user_see_validation_message(context):
    context.app.forgot_password_page.verify_email_not_valid_text(context=context)
