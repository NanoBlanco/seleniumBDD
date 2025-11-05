from behave import given, when, then
from pages.login_page import LoginPage

@given('el usuario está en la página de login')
def step_open_login(context):
    context.page = LoginPage(context.driver)
    context.driver.get("https://ecommerce-e2e.netlify.app/")

@when('ingresa credenciales válidas')
def step_login_valid(context):
    context.page.login("standard_user", "secret_sauce")

@when('ingresa credenciales inválidas')
def step_login_invalid(context):
    context.page.login("wrong_user", "wrong_pass")

@then('debería ingresar al catálogo de productos')
def step_login_success(context):
    assert "inventory" in context.driver.current_url

@then('debería ver un mensaje de error')
def step_login_error(context):
    assert "Epic sadface" in context.page.get_error_message()
