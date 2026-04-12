# language: es
Característica: Integración oficial con Robot Framework
  Como usuario del wrapper oficial para Robot
  Quiero usar adaptadores con acceso por atributo y por llave
  Para automatizar pruebas con un contrato estable

  Escenario: Crear una tabla desde registros y acceder a una fila de Robot
    Dado una colección de registros en memoria
    Cuando creo una RobotDataTable desde registros
    Y obtengo la fila 0 con la librería de Robot
    Entonces la fila de Robot expone acceso por atributo y por llave

  Escenario: Mutar una RobotDataTable y guardarla como JSON
    Dado una colección de registros en memoria
    Cuando creo una RobotDataTable desde registros
    Y asigno la columna "country" con el valor "MX" en la fila 0 usando Robot
    Y guardo la RobotDataTable como JSON
    Entonces el archivo JSON generado incluye la nueva columna en todas las filas

  Escenario: Crear una RobotDataTable desde archivo JSON
    Dado un archivo JSON de personas
    Cuando creo una RobotDataTable desde archivo JSON
    Entonces los headers de Robot coinciden con el archivo fuente
