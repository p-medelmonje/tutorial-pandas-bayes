### Selección de filas

#### Métodos a utilizar:

`df.iloc[10:20]` Selecciona filas por posición

`df.nlargest(n, 'value')` Selecciona y ordena los n valores mayores
`df.nsmallest(n, 'value')` Selecciona y ordena los n valores menores

---

Uso de archivo **marketing_data.csv**. En el repositorio original de kaggle, actualmente ha sido reemplazado por otro archivo.

El dataset contiene datos de clientes que recibieron alguna campaña de Marketing, con datos como ID; año de nacimiento; nivel de educación; cantidad de distintos productos consumidos durante el año; si es que aceptó una campaña de marketing; etc.

---

### El código en Python

Importar librerías:

`import pandas as pd`    
`import numpy as np`

Importar el archivo:

`df = pd.read_csv("marketing_data.csv")`

#### Seleccionar filas

Selección de las filas de la 10 a la 20; la 10 incluída y la 20 no se incluye.

`df.iloc[10:20]`

Aquí se enlistan los nombres de todas las columnas del dataset:

`df.columns.values`

### Otro tipo de selección de filas

#### ¿Los clientes más jóvenes?

Se utiliza el siguiente código para encontrar los 5 mayores valores de la columna "Year_Birth". Con esto podemos encontrar a los clientes más jóvenes.

`df.nlargest(5, "Year_Birth")`

#### ¿Los clientes mayores?

Se utiliza el siguiente código para encontrar los 5 menores valores de la columna "Year_Birth". Con esto podemos encontrar a los clientes de mayor edad.

`df.nsmallest(5, "Year_Birth")`

#### ¿Los clientes con la mayor cantidad de días desde la última compra?

Con esto podemos encontrar a los 5 clientes con los valores más altos en la columna de "Recency", es decir, se ubicaron a los 5 clientes con la mayor cantidad de días desde la última compra.

`df.nlargest(5, "Recency")`

#### ¿Los clientes con la menor cantidad de días desde la última compra?

Con esto podemos encontrar a los 5 clientes con los valores más bajos en la columna de "Recency", es decir, se ubicaron a los 5 clientes con la menor cantidad de días desde la última compra.

`df.nsmallest(5, "Recency")`





