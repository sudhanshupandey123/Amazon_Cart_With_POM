
from playwright.sync_api import sync_playwright
from behave import when,then
p=sync_playwright().start()
def before_scenario(context,scenario):
    context.browser=p.chromium.launch(headless=False, slow_mo=3000)
    context.page=context.browser.new_page()
    context.page.goto('https://www.amazon.in/')
    context.page.wait_for_load_state(timeout=10000)

def after_scenario(context,scenario):
    context.page.close()
    context.browser.close()


