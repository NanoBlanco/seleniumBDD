from behave import given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    wait = WebDriverWait(context.driver, 10)
    user_menu = wait.until(EC.visibility_of_element_located((By.ID, "user-menu")))

    # Verificar que el texto del botón corresponda al usuario logueado
    user_name = user_menu.text.strip()
    assert user_name == "Emily", f"El usuario mostrado ('{user_name}') no es el esperado ('Emily')"

    # Verificar que el botón de login ya no esté visible
    login_buttons = context.driver.find_elements(By.ID, "login-btn")
    login_visible = any(btn.is_displayed() for btn in login_buttons)

    assert not login_visible, "El botón de login sigue visible tras iniciar sesión"

@when('ingresa credenciales inválidas')
def step_login_invalid(context):
    context.login_page.login("wrong_user", "wrong_pass")

@then('debería ver un mensaje de error')
def step_login_error(context):
    assert "error" in context.driver.page_source.lower() or "credenciales" in context.driver.page_source.lower()
