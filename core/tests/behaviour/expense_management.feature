Feature: Gestión de gastos
  Como estudiante
  Quiero registrar mis gastos
  Para controlar cuánto dinero gasto

  Scenario: Crear un gasto y comprobar cual es el total que llevo gastado
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    Then el total de dinero gastado debe ser 5 euros

  Scenario: Eliminar un gasto y comprobar cual es el total que llevo gastado
    Given un gestor con un gasto de 5 euros
    When elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear y eliminar un gasto y comprobar que no he gastado dinero
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear dos gastos diferentes y comprobar que el total que llevo gastado es la suma de ambos
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And añado un gasto de 10 euros llamado Comida
    Then el total de dinero gastado debe ser 15 euros

  Scenario: Crear tres gastos diferentes que sumen 30 euros hace que el total sean 30 euros

  Scenario: Crear tres gastos de 10, 30, 30 euros y elimino el ultimo gasto la suma son 40 euros

  Scenario: Crear tres gastos de 10, 30, 30 euros y elimino el ultimo gasto la suma son 40 euros

Scenario: Actualizar el nombre de un gasto existente
    Given un gestor con un gasto de 50 euros
    When actualizo el gasto con id 1 con el nombre "Gasto Actualizado"
    Then el gasto con id 1 debe llamarse "Gasto Actualizado"

  Scenario: Intentar eliminar un gasto que no existe no afecta al total
    Given un gestor con un gasto de 20 euros
    When elimino el gasto con id 99
    Then el total de dinero gastado debe ser 20 euros

  Scenario: El listado de gastos debe reflejar todos los registros
    Given un gestor con un gasto de 10 euros
    When añado un gasto de 20 euros llamado "Taxi"
    Then debe haber 2 gastos registrados
