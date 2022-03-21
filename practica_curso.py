# Importar librerías

import pandas as pd
import matplotlib.pyplot as plt

# Importar el archivo

fifa20 = pd.read_csv("players_20.csv")
fifa20_1 = fifa20[["short_name", "age", "height_cm", "weight_kg", "club",
                   "overall", "potential", "value_eur", "wage_eur",
                   "player_positions", "power_jumping", "power_long_shots"]]


#df1 = pd.DataFrame(fifa20)

# Hacer un dataset a partir del principal

realmadrid = fifa20_1[fifa20_1["club"] == "Real Madrid"]
#print(realmadrid.shape)
#print("")
#print(realmadrid.head(10))

barcelona = fifa20_1[fifa20_1["club"] == "FC Barcelona"]
#print(barcelona.shape)
#print(barcelona.head())
#print("")

# Potencia en tiros largos

plt.hist(fifa20_1["power_long_shots"])
plt.xlabel("Potencia en tiros largos")
plt.ylabel("Frecuencia")
plt.title("Potencia en tiros largos")