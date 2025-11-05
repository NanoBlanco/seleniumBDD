from behave import given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage

@given('el usuario está en la página de inicio')
def step_open_home(context):
    context.home = HomePage(context.driver)
    context.home.open("https://ecommerce-e2e.netlify.app/")

@when('el usuario navega al formulario de login')
def step_go_to_login(context):
    context.home.go_to_login()
    context.login_page = LoginPage(context.driver)

@when('ingresa credenciales válidas')
def step_login_valid(context):
    context.login_page.login("emilys", "emilyspass")

@then('debería ingresar al catálogo de productos')
def step_verify_login(context):
    assert "catalogo" in context.driver.current_url.lower() or "productos" in context.driver.page_source.lower()

@when('ingresa credenciales inválidas')
def step_login_invalid(context):
    context.login_page.login("wrong_user", "wrong_pass")

@then('debería ver un mensaje de error')
def step_login_error(context):
    assert "error" in context.driver.page_source.lower() or "credenciales" in context.driver.page_source.lower()
