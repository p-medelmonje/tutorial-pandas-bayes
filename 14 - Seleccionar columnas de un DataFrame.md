### Cómo seleccionar columnas de un DataFrame en pandas
---

**df[['width', 'length', 'species']]** Selecciona múltiples columnas con nombres específicos.

**df['width']* o *df.width** Selecciona una columna con un nombre específico.

**df.filter(regex='regex')** Selecciona columnas cuyo nombre coincide con la expresión regular regex.

---

#### Ejemplos de expresiones regulares:

**'\ \.'**  Empareja strings que contienen un período '.'

**'Length$'** Empareja strings que terminen con la palabra 'Length'  

**'Sepal'** Empareja strings con la palabra 'Sepal'

**'^x[1-5]$'** Empareja strings que empiecen con x y que terminen con 1, 2, 3, 4, 5

**^(?!Species$).*'** Empareja strings con la excepción del string 'Species'

---

**df.loc[:, 'x2': 'x4']** Selecciona todas las columnas entre x2 y x4 (inclusive).

**df.iloc[:, [1,2,5]]** Selecciona las columnas en las posiciones 1, 2 y 5 (la primera columna es 0).

---

#### El código en Python

Continuación con el cuaderno anterior

#### Subset Variables (columnas)

Aquí se seleccionan las columnas "Education", " Income ", "Recency" y "Response" del dataset df

**df[["Education", " Income ", "Recency", "Response"]].head()**

Aquí se selecciona únicamente la columna "Response"

**df.Response**

Aquí se selecciona las columnas que empiecen su nombre con "Accepted"

**df.filter(regex = 'Accepted').head()**

Aquí seleccionamos las columnas que terminen su nombre con 'home'

**df.filter(regex = 'home$').head()**

Aquí seleccionamos las columnas desde "Year_Birth" hasta "Kidhome", incluyéndose.

**df.loc[:, 'Year_Birth': 'Kidhome']**

Aquí se incluyen las columnas 1, 2 y 5

**df.iloc[:, [1, 2, 5]]**











