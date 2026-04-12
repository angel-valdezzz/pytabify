## 📌 pytabify

**📊 Tabify your data, Python-style**

*📊 Tabula tus datos con magia Python*

**pytabify** es una librería ligera para cargar, validar y persistir datos tabulares desde **CSV, JSON y Excel**, pensada para **automatización de pruebas**, **fixtures**, **scripts** y flujos de datos simples en Python y Robot Framework.

---

## 🚀 Características

✅ **Soporte para múltiples formatos:** Importa datos desde archivos CSV, JSON y Excel.  
✅ **Contrato tabular estable:** Mantiene columnas ordenadas y consistentes en toda la tabla.  
✅ **Preserva tipos nativos:** Conserva enteros, booleanos y `None` en memoria.  
✅ **Wrapper oficial para Robot Framework:** Expone keywords y adaptadores amigables para Robot.  
✅ **Exportación flexible:** Guarda los datos en distintos formatos según sea necesario.  

---

## 🧱 Arquitectura

El paquete sigue una separación basada en **Clean Architecture** y **arquitectura hexagonal**:

- `domain`: entidades y reglas del modelo tabular.
- `application`: puertos y casos de uso.
- `adapters`: adaptadores concretos para archivos y Robot Framework.
- `creator.py` y `saver.py`: fachadas públicas que componen los casos de uso sin exponer la infraestructura interna.

---

## 📦 Instalación

### Usando pip:
```sh
pip install pytabify
```

---

## 📖 Uso Básico

### 📌 Creando un DataTable desde un archivo
```python
from pytabify import DataTableCreator

# Desde CSV
datatable = DataTableCreator.from_file("data.csv")

# Desde JSON
datatable = DataTableCreator.from_file("data.json")

# Desde Excel (requiere indicar la hoja)
datatable = DataTableCreator.from_file("data.xlsx", sheet_name="Hoja1")
```

### 📌 Accediendo a los datos
```python
# Obtener una fila específica
row = datatable[0]
print(row.name.value)

# Iterar sobre filas
for row in datatable:
    print(row.to_dict())

# Modificar valores sin duplicar columnas
row["age"] = 31
row.country = "MX"
```

### 📌 Guardando datos
```python
from pytabify import DataTableSaver

# Guardar en CSV
DataTableSaver.into_csv(datatable, "output.csv")

# Guardar en JSON
DataTableSaver.into_json(datatable, "output.json")

# Guardar en Excel
DataTableSaver.into_xlsx(datatable, "output.xlsx")
```

---

## 🛠️ Integración con Pruebas Automatizadas

**pytabify** está diseñado para funcionar en entornos de **pruebas automatizadas**.

### Python
```python
from pytabify import DataTableCreator

datatable = DataTableCreator.from_records(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)

assert datatable[0].name.value == "Alice"
assert datatable[1].age.value == 25
```

### Robot Framework
```robot
*** Settings ***
Library    pytabify.robot.PyTabifyLibrary    WITH NAME    PyTabify

*** Test Cases ***
Leer datos desde CSV
    ${datatable}=    PyTabify.Create Data Table From File    path=data.csv
    Should Not Be Empty    ${datatable}

Validar un campo específico
    ${row}=    PyTabify.Get Data Table Row    ${datatable}    0
    Should Be Equal As Strings    ${row.name}    Alice
    Should Be Equal As Integers    ${row}[age]    30

Modificar una celda y guardar
    ${datatable}=    PyTabify.Set Data Table Value    ${datatable}    0    country    MX
    PyTabify.Save Data Table To Json    ${datatable}    path=output.json

Guardar datos en Excel
    PyTabify.Save Data Table To Xlsx    ${datatable}    path=output.xlsx
    File Should Exist    output.xlsx
```

---

## 🧪 Pruebas

El proyecto cuenta con dos suites principales:

- `utests`: suite unitaria enfocada en dominio, casos de uso, adaptadores y compatibilidad.
- `atests`: suite de aceptación con **pytest + Cucumber/Gherkin** en español para validar flujos end-to-end sobre la API pública y el wrapper de Robot.

### Instalar dependencias de desarrollo

```sh
poetry install
```

### Ejecutar toda la suite

```sh
poetry run pytest
```

### Ejecutar solo tests unitarios

```sh
poetry run pytest utests -q
```

### Ejecutar solo tests de aceptación con Cucumber

```sh
poetry run pytest atests -q --no-cov
```

### Notas sobre los tests de aceptación

- Los escenarios viven en archivos `.feature`.
- La sintaxis Gherkin usa `# language: es` para definir los pasos en español.
- Los tests de aceptación usan archivos temporales reales (`JSON`, `CSV`, `XLSX`) para validar flujos completos.
- La configuración de `pytest` exige cobertura mínima al ejecutar la suite completa.
- Si ejecutas solo `atests`, usa `--no-cov` para evitar que la puerta global de cobertura falle por ejecutar solo un subconjunto del proyecto.
```

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.
