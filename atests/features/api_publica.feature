# language: es
Característica: Flujos públicos de pytabify
  Como consumidor de pytabify
  Quiero manipular datos tabulares con la API pública
  Para automatizar flujos end-to-end con archivos reales

  Escenario: Convertir un archivo JSON a CSV con la API pública
    Dado un archivo JSON de personas
    Cuando cargo el DataTable con la API pública
    Y guardo el DataTable como CSV
    Entonces el archivo CSV generado contiene las columnas esperadas

  Escenario: Cargar un archivo XLSX y persistirlo como JSON
    Dado un archivo XLSX de personas en la hoja "Personas"
    Cuando cargo el DataTable XLSX con la API pública
    Y guardo el DataTable como JSON
    Entonces el archivo JSON generado conserva los registros esperados

  Escenario: Extender el esquema desde la API pública y persistirlo como JSON
    Dado una colección de registros en memoria
    Cuando creo un DataTable desde registros
    Y agrego la columna "country" con el valor "MX" en la fila 0
    Y guardo el DataTable como JSON
    Entonces el archivo JSON generado incluye la nueva columna en todas las filas
