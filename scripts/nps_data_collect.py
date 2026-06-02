import os
import requests
import pandas as pd

api_key = "cQmOw0xrMD43At2kz7d5IgDgyhmymaPcFiTAj4vj"
url = "https://developer.nps.gov/api/v1/parks"
parameters = {"api_key": api_key, "limit": 5}
resp = requests.get(url, params=parameters)

parks = resp.json()["data"]

records = []

for park in parks:
    print(f"Park: {park['fullName']}")
    print(f"State: {park['states']}")
    print(f"Latitude: {park['latitude']}")
    print(f"Longitude: {park['longitude']}")
    print("-" * 50)
    records.append({
        "fullName": park["fullName"],
        "states": park["states"],
        "latitude": park["latitude"],
        "longitude": park["longitude"],
    })

df = pd.DataFrame(records)
print(df.head())
os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/nps_parks.csv", index=False)