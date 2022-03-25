### Cómo hacer Merge de DataFrames
---

`import pandas as pd`

#### Creación de dataset

~~~
staff_df = pd.DataFrame([{"Name": "Kelly", "Role": "Director of HR"},
                          {"Name": "Sally", "Role": "Course liasion"},
                          {"Name": "James", "Role": "Grader"}])

staff_df = staff_df.set_index("Name")

student_df = pd.DataFrame([{"Name": "James", "School": "Business"},
                           {"Name": "Mike", "School": "Law"},
                          {"Name": "Sally", "School": "Engineering"}])

student_df = student_df.set_index("Name")

print(staff_df.head())
print(student_df.head())
~~~

---
### Outer

Aquí obtenemos un dataset con todos los registros de los dos dataset

`pd.merge(staff_df, student_df, how = "inner", left_index = True, right_index = True)`

### Inner

Aquí obtenemos un dataset con los registros en común en ambos dataset. Se devuelve un DataFrame solo con Sally y James, ya que esos dos registros tienen valores en ambos datasets.

`pd.merge(staff_df, student_df, how = "inner", left_index = True, right_index = True)`

### Left

Aquí obtenemos un dataset con los registros del dataset izquierdo y con la información de las columnas correspondientes del dataset derecho. En este caso, los nombres a verse serían los de Kelly, Sally y James.

`pd.merge(staff_df, student_df, how = "left", left_index = True, right_index = True)`

### Right

Aquí obtenemos un dataset con los registros del dataset derecho y con la información de las columnas correspondientes del dataset izquierdo. En este caso, los nombres a verse serían los de James, Mike y Sally.

`pd.merge(staff_df, student_df, how = "right", left_index = True, right_index = True)`

### Right sin Index

Eliminamos los índices asignados previamente en los dos dataset

`staff_df = staff_df.reset_index()`
`student_df = student_df.reset_index()`

Aquí obtenemos un dataset con los registros del dataset derecho y con la información de las columnas correspondientes del dataset izquierdo

`pd.merge(staff_df, student_df, how = "right", on = "Name")`

---

## Parte 2

Creación de otros dataset

~~~
staff_df_2 = pd.DataFrame([{"Name": "Kelly", "Role": "Director of HR", "Location": "State Street"},
                          {"Name": "Sally", "Role": "Course Ilation", "Location": "Washington Avenue"},
                          {"Name": "James", "Role": "Grader", "Location": "Washington Avenue"}])

student_df_2 = pd.DataFrame([{"Name": "James", "School": "Business", "Location": "1024 Billiard Avenue"},
                          {"Name": "Mike", "School": "Law", "Location": "Fraternity House #22"},
                          {"Name": "Sally", "School": "Engineering", "Location": "512 Wilson Crescent"}])
~~~

### Left sin Index

Aquí obtenemos el dataset con los registros del dataset izquiero y con la información que corresponde de las columnas del dataset derecho

`pd.merge(staff_df_2, student_df_2, how = "left", on = "Name")`

### Creación de otros dataset

~~~
staff_df_3 = pd.DataFrame([{"First Name": "Kelly", "Last Name": "Desjardins", "Role": "Director of HR"},
                          {"First Name": "Sally", "Last Name": "Brooks", "Role": "Course liasion"},
                          {"First Name": "James", "Last Name": "Wilde", "Role": "Grader"}])

student_df_3 = pd.DataFrame([{"First Name": "James", "Last Name": "Hammond", "School": "Business"},
                            {"First Name": "Mike", "Last Name": "Smith", "School": "Law"},
                            {"First Name": "Sally", "Last Name": "Brooks", "School": "Engineering"}])
~~~

### Inner con lista

Aquí creamos un dataframe en donde se ubican los registros exactos según la lista

`pd.merge(staff_df_3, student_df_3, how = "inner", on = ["First Name", "Last Name"])`

Solo muestra a Sally Brooks, ya que es el único registro que tiene los mismos datos en ambos datasets

---

Fin del curso
