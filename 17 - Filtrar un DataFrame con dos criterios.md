### Filtrar un DataFrame con dos criterios

---

Uso del archivo players_20.csv

import pandas as pd

`fifa20 = pd.read_csv(filepath_or_buffer = "players_20.csv)`

Creación de otro dataset

`fifa20_1 = fifa20[["short_name", "age", "height_cm", "weight_kg", "club", "overall", "potential", "value_eur", "wage_eur",           "player_positions", "power_jumping", "power_long_shots"]]`

Doble filtro en una misma línea de código para crear un datset con los criterios deseados. En este caso, es un dataset con los jugadores del Barcelona con una edad de 24 años.

`barcelona_final = fifa20_1[(fifa20_1["Club"] == "FC Barcelona") & (fifa20_1["age"] >= 24]`





