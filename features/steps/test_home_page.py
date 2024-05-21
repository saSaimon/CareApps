from behave import given, then, when
from time import sleep


@when('User will verify Login successful if they saw CareApp Logo on the up right corner')
def verify_logo(context):
    sleep(5)
    context.app.login_page.is_logo_present()


@then('User will verify if total job cart present')
def verify_user_verify_job_cart(context):
    context.app.home_page.verify_total_job_present()


@then('User will verify if viewed application cart present')
def verify_user_verify_viewed_application_cart(context):
    context.app.home_page.verify_viewed_application_present()


@then('User will verify if unseen application cart present')
def verify_user_verify_unseen_application_cart(context):
    context.app.home_page.verify_unseen_application_present()


@then('User will verify if total job application cart present')
def verify_user_verify_total_job_application_cart(context):
    context.app.home_page.verify_total_job_application_present()


@then('User will verify if accepted application cart present')
def verify_user_verify_accepted_application_cart(context):
    context.app.home_page.verify_accepted_application_present()


@then('User will verify if submitted application cart present')
def verify_user_verify_submitted_application_cart(context):
    context.app.home_page.verify_submitted_application_present()


@then('User will verify if jobs cart present')
def verify_user_verify_jobs_cart(context):
    context.app.home_page.verify_jobs_cart_present()


@then('User will verify if completion ratio present')
def verify_user_verify_completion_ratio(context):
    context.app.home_page.verify_completion_ratio_present()


@when('User will click job application button')
def user_will_click_job_application_button(context):
    context.app.home_page.click_job_application_button()


@then('User will verify Job Board text is present')
def user_will_verify_job_board_text(context):
    context.app.home_page.verify_job_board_text(context=context)


@then('User will verify Candidate List text is present')
def user_will_verify_job_board_text(context):
    context.app.home_page.verify_candidate_list_text(context=context)


@when('User will click back button of browser')
def user_will_click_back_button(context):
    context.app.home_page.back_to_previous_page()


@when('User will click view jobs button')
def user_will_click_view_jobs_button(context):
    context.app.home_page.click_view_jobs()


