from urllib.request import urlopen
import json
import pandas as pd

# List of cities
liste_ville = ["bruxelles","brisbane","namur","santander", "lyon", "toyama", "toulouse", "marseille","nantes","rouen","amiens","stockholm","lillestrom","vilnius"]
liste_url = [f"https://developer.jcdecaux.com/rest/vls/stations/{ville}.json" for ville in liste_ville]


df = []

num_id = 1


for ville, url in zip(liste_ville, liste_url):
    #Recup data url
    response = urlopen(url)
    data_json = json.loads(response.read())
    # Convert the JSON data into a DataFrame
    d = pd.DataFrame(data_json)    
    # Add the 'ville' column (city name for each row)
    d['ville'] = ville 
    # Add the 'idstation' column (unique station IDs across all cities)
    d['idstation'] = range(num_id, num_id + len(d))  
    # Update the counter for the next city
    num_id += len(d) 
    # Append this DataFrame to the list
    df.append(d)

# Concatenate les dataframes
final_df = pd.concat(df, ignore_index=True)

df_csv = final_df.to_csv("stations.csv", sep = ';', index=False)

