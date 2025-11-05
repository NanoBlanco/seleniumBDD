Feature: Login de usuario
  Como usuario del ecommerce
  Quiero iniciar sesión con mis credenciales
  Para acceder al catálogo de productos


  Scenario: Login exitoso con credenciales válidas
    Given el usuario está en la página de inicio
    When el usuario navega al formulario de login
    And ingresa credenciales válidas
    Then debería ingresar al catálogo de productos

  Scenario: Login fallido con credenciales inválidas
    Given el usuario está en la página de inicio
    When el usuario navega al formulario de login
    And ingresa credenciales inválidas
    Then debería ver un mensaje de error
