## Eliminar columnas con la función DataFrame.drop

**df.drop(columns = ['Length', 'Height'])**

### Selección de filas

**df[df.Length > 7]**  Extrae filas que cumplen la condición lógica

**df.drop_duplicates()**  Remueve filas duplicadas (solo considera columnas)

**df.head(n)** Selecciona las primeras n filas

**df.tail(n)** Selecciona las últimas n filas

**df.sample(frac=0.5)** Selecciona aleatoriamente fracciones de filas

**df.sample(n=10)** Selecciona aleatoriamente n filas

**df.iloc[10:20]** Selecciona filas por posición

**df.nlargest(n, 'value')** Selecciona y ordena las n mayores entradas

**df.nsmallest(n, 'value')** Selecciona y ordena las n menores entradas


