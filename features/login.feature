Feature: Login de usuario

  Scenario: Login exitoso con credenciales válidas
    Given el usuario está en la página de login
    When ingresa credenciales válidas
    Then debería ingresar al catálogo de productos

  Scenario: Login fallido con credenciales inválidas
    Given el usuario está en la página de login
    When ingresa credenciales inválidas
    Then debería ver un mensaje de error
