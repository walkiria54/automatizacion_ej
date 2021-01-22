# Scenario: Validar mensaje de error al acceder en la  app con datos incorrectos
from behave import given, when, then

from selenium import webdriver  # navegador
from selenium.webdriver.firefox.options import Options

@given('que tengo mi aplicación instalada y funcionando en la url \"{url}\" con titulo \"{titulo}\"')
def step_impl(context, url, titulo):
    #assert True
    # config del driver que en este caso el navegador es firefox
    opciones = Options()
    opciones.headless = True
    navegador = webdriver.Firefox(executable_path='./drivers/geckodriver', options=opciones)
    navegador.set_window_position(0, 0)
    navegador.set_window_size(800, 500)
    titleido=navegador.title
    navegador.get(url)
    # cerrar navegador
    navegador.quit()
    assert titleido == titulo

####
@when('un usuario registrado intenta acceder a la aplicación con usuario \"{user}\" y password  \"{pwd}\"incorrecto')
def step_impl(context, user, pwd):
    assert user== 'xxx'
@when('al dar click en boton con texto login \"{btn_text}\"')
def step_impl(context, btn_text):
    assert True
@then('la pantalla de login no le debe permitir \"{txtaccede}\"el acceso al usuario')
def step_impl(context,txtaccede):
    assert True
@then('genera mensaje de error \"{errormsg}\"Mensaje de error')
def step_impl(context, errormsg):
    assert True