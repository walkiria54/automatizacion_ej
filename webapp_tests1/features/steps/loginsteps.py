from behave import *

#You can implement step definitions for undefined steps with these snippets:

@given(u'que tengo mi aplicación instalada y funcionando en la url "http://miapp.com" con titulo "mi pagina login"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que tengo mi aplicación instalada y funcionando en la url "http://miapp.com" con titulo "mi pagina login"')


@when(u'un usuario registrado intenta acceder a la aplicación con usuario "ruina" y password  "ruina"incorrecto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When un usuario registrado intenta acceder a la aplicación con usuario "ruina" y password  "ruina"incorrecto')


@when(u'al dar click en boton con texto login "Acceder"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When al dar click en boton con texto login "Acceder"')


@then(u'la pantalla de login no le debe permitir "no se permite"el acceso al usuario')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then la pantalla de login no le debe permitir "no se permite"el acceso al usuario')


@then(u'genera mensaje de error "usuario desconocido o pass incorrecta"Mensaje de error')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then genera mensaje de error "usuario desconocido o pass incorrecta"Mensaje de error')
