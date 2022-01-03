import pandas as pd
import pycep_correios
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geolocalização")

df = pd.read_csv("C:\\Users\\bru-c\\Documents\\Python Projects\\extract-cep\\df.csv", encoding='cp1252', sep=';')

#df.drop_duplicates(subset=['bairro'], inplace=True)

#df.reset_index(drop=True, inplace=True)

print(df)

lat = []
long = []

for index, row in df.iterrows():

    try:
        endereco = pycep_correios.get_address_from_cep(row['CEP'])

        location = geolocator.geocode(endereco['bairro'] + ", " + endereco['cidade'] + ' - ' + endereco['uf'])

        lat.append(location.latitude)
        long.append(location.longitude)

        print((location.latitude, location.longitude))

    except:
        lat.append(0)
        long.append(0)

        pass


df['latitude'] = lat
df['longitude'] = long

df.to_csv("C:\\Users\\bru-c\\Documents\\Python Projects\\extract-cep\\df_coords.csv",index=False, header=True, encoding='cp1252', sep=';')