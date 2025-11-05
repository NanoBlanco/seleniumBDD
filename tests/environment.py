from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def after_all(context):
    context.driver.quit()
