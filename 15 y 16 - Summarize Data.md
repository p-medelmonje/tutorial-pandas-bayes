## 15 - Summarize Data en pandas
### Calcular la Tasa de Conversión de una Camapaña de Marketing
---
**df['w'].value_counts()** Cuenta el número de filas con cada valor único de variable  

**len(df)** número de valores distintos en una columna  

**df['w'].nunique()** número de valores distintos en una columna  

**df.describe()** Estadísticas básicas descriptivas para cada columna (o GroupBy)  

---

Continuación con el cuaderno creado en la lección 13.

### Summarize data

Veamos qué nivel de escolaridad tienen los clientes registrados en la campaña de marketing.

**df['Education'].value_counts()**

Con el siguiente código veremos el estado civil de los clientes que recibieron la campaña de marketing

**df['Marital_Status'].value_counts()**

Creación de dos datasets. Uno con los clientes que respondieron positivamente a la primera campaña y el otro dataset tiene a los clientes que no respondieron a la primera campaña.

**df1 = df[df.AcceptedCmp1 == 1]**
**df2 = df[df.AcceptedCmp1 == 0]**

En el siguiente código vemos la cantidad de quejas y el número de niños en su hogar de los clientes que respondieron a la primera campaña de marketing.

**print(df1['Complain'].value_counts())**
**print(df1['Kidhome'].value_counts())**

En el siguiente código vemos la cantidad de quejas y el número de niños en su hogar de los clientes que no respondieron a la primera campaña de marketing.

**print(df2['Complain'].value_counts())**
**print(df2['Kidhome'].value_counts())**

Podemos ver que las personas que no han tenido quejas y no tienen niños en sus hogares, son más propensos a aceptar la oferta en la primera campaña de marketing.

Con la función .describe() podemos ver las medidas de tendencia central y las medidas de dispersión de los dataset

**df1.describe()**  
**df2.describe()**

Nuevamente podemos concluir que las personas que no tienen reclamos y que no tienen niños en sus hogares son más propensas a aceptar la oferta en la primera campaña de marketing. Las personas que aceptan la oferta en la primera campaña suelen consumir más vino, frutas, carnes y dulces.

---
#### Fórmula de la tasa de conversión:

`"La tasa de conversión en la primera campaña es de " + str((df1.shape[0] / (df.shape[0] + df1.shape[0])) * 100) + "%"`

Lo anterior no obedece a un modelo predictivo o estadístico, pero sí entrega información muy relevante para tomar decisiones a nivel empresarial.

---

## 16 - Summarize Data - Parte 2

pandas proporciona un gran conjunto de funciones de resumen que operan en diferentes tipos de objetos pandas (DataFrame, Series, GroupBy) y producri valores únicos para cada uno de los grupos. Cuando se aplica a un DataFrame, el resultado se devuelve como una serie pandas para cada columna. Ejemplos:

**sum()** Suma los valores de cada objeto  
**count()** Cuenta los valores de cada objeto que no sean nulos/NaN  
**median()** El valor media de cada objeto  
**quantile([0.25,0.75])** Cuantiles de cada objeto  
**apply(*función*)** Aplica función a cada objeto  
**min()** El valor mínimo en cada objeto  
**max()** El valor máximo en cada objeto  
**mean()** Valor promedio de cada objeto  
**var()** Variación de cada objeto  
**std()** Desviación estándar de cada objeto  

### Lo que vamos a hacer

Comprar estadísticamente a los clientes que compraron el producto en la primera campaña de marketing con los de la última campaña de marketing.

---
Continuación con un cuaderno creado en Colab

### El código

import pandas as pd
import numpy as np

Importación de archivo

`url = ("https://raw.githubusercontent.com/p-medelmonje/tutorial-pandas-bayes/main/marketing_data.csv")`  
`df = pd.read_csv(url)`

Comparar a los clientes que aceptaron la oferta en la primera campaña con los que aceptaron la oferta en la sexta y última campaña

firstc = df[df["AcceptedCmp1"] == 1]
lastc = df[df["Response"] == 1]
print(firstc.shape, lastc.shape)

Tasa de conversión

`tc1 = ((firstc.shape[0] / df.shape[0]) * 100)`
`print("La tasa de conversión en la primera campaña fue de " + str(tc1) + "%")`

Promedio general del primer dataset

`firstc.mean()`

Promedio general del segundo dataset

`lastc.mean()`

#### ¿Quiénes son los más jóvenes?

`print(firstc.mean()[1], lastc.mean()[1])`

Devuelve: 1968.5347222222222 1969.4161676646706

No existe una diferencia significativa, pero los que compraron en la última campaña son más jóvenes.

#### ¿Qué cantidad de niños tienen en casa los dos grupos de clientes?

`print(firstc.mean()[2], lastc.mean()[2])`

Devuelve: 0.09027777777777778 0.3413173652694611

Los clientes que respondieron a la primera campaña tienen menos niños en casa que el otro grupo de clientes.

#### Número de días desde la última compra

`print(firstc.mean()[4], lastc.mean()[4])`

Los clientes que compraron en la primera campaña tienen más días desde que compraron

#### ¿Quiénes consumen más vino?

`print(firstc.mean()[5], lastc.mean()[5])`

Los clientes que compraron en la primera campaña consumen más vino que los clientes del otro grupo

#### Los clientes con más reclamos

print(firstc.mean()[-1], lastc.mean()[-1])

Los clientes que compraron en la primera campaña prácticamente no tienen reclamos

### Otras funciones resumidas

Desviación estándar

`std1 = firstc.std()`
`std2 = lastc.std()`

`print("El promedio de días desde la última compra para los clientes que compraron con la primera campaña son de " + str(firstc.mean()[4]) + " con una desviación de " + str(firstc.std()[4]))`

El promedio de días desde la última compra para los clientes que compraron con la primera campaña son de 46.979166666666664 con una desviación de 28.380646599374746

#### Uso de .describe para resumir las estadísticas de todas las variables

firstc.describe()








