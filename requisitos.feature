Feature: pantalla de login 
#cosas que el tester tiene que escribir para refinar cada escenario
#Registro ?
#Error
#Bloqueo de usuario por intentos
#tiempos? 
#aplicacion seria por ej la url de login de la apli usuario y password serian parametros 
    Scenario: Validar mensaje de error al acceder en la  app con datos incorrectos 
        Given que tengo mi aplicación instalada y funcionando "aplicación"
        When un usuario registrado intenta acceder a la aplicación con "usuario" y "password" incorrecto
        And al dar click en "login"
        Then la pantalla de login no le debe permitir el acceso a la aplicación
        And genera mensaje de error "Mensaje de error"
    Scenario: Alguien malicioso quiere entrar en la  app 
        Given que tengo mi aplicación instalada y funcionando "aplicación"
        When un usuario no registrado intenta acceder a la aplicación con "usuario" y "password" incorrecto
        And al dar click en "login"
        Then la pantalla de login no le debe permitir el acceso a la aplicación
        And genera mensaje de error "Mensaje de error"
    Scenario: Alguien registrado reincide al querer entrar en la  app incorrectamente
        Given que tengo mi aplicación instalada y funcionando "aplicación"
        When un usuario registrado intenta acceder a la aplicación con "usuario" y "password" incorrectos mas de "n" veces en "tiempo"
        And al dar click en "login" 
        Then la pantalla de login no le debe permitir el acceso a la aplicación
        And genera mensaje de error "Mensaje de error"
        And se bloquea la cuenta del usuario "usuario"
    
    Scenario: Alguien registrado quiere entrar en la app
        Given que tengo mi aplicación instalada y funcionando "aplicación" 
        When un usuario registrado intenta acceder a la aplicación con "usuario" y "password" correctos
        And al dar click en "login"
        Then se permite el acceso a la aplicación
        And genera mensaje de ok "Mensaje de ok"