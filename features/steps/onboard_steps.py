from behave import *
from page.onboard_slide1_page import OnboardSlide1Page

onboard_slide1_page = None

@given(u'I am on the first onboard slide')
def step_impl(context):
    global onboard_slide1_page
    onboard_slide1_page = OnboardSlide1Page()
    onboard_slide1_page.check_onboard1_is_loaded()

@then(u'I click on the next button')
def step_impl(context):
    onboard_slide1_page.click_the_next_button()

@then(u'I click on the access button')
def step_impl(context):
    onboard_slide1_page.click_the_access_button()

