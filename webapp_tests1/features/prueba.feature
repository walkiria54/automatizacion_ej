Feature: pantalla de login
  Scenario: Validar mensaje de error al acceder en la  app con datos incorrectos
        Given que tengo mi aplicación instalada y funcionando en la url "http://miapp.com" con titulo "mi pagina login"
        When un usuario registrado intenta acceder a la aplicación con usuario "ruina" y password  "ruina"incorrecto
        And al dar click en boton con texto login "Acceder"
        Then la pantalla de login no le debe permitir "no se permite"el acceso al usuario
        And genera mensaje de error "usuario desconocido o pass incorrecta"Mensaje de error