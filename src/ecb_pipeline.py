import requests
import xml.etree.ElementTree as ET
import pandas as pd

url="https://data-api.ecb.europa.eu/service/data/EXR/M.USD.EUR.SP00.A"

try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from ECB API: {e}")
    exit(1)
root = ET.fromstring(response.content)
data = []

for element in root.iter():
    if element.tag.endswith("Obs"):
        date = None
        value = None

        for child in element:
            if child.tag.endswith("ObsDimension"):
                date = child.attrib["value"]
            elif child.tag.endswith("ObsValue"):
                value = child.attrib["value"]

        data.append([date, value])

df = pd.DataFrame(data, columns=["date", "exchange_rate"])
df["date"] = pd.to_datetime(df["date"], format="%Y-%m")
df["exchange_rate"] = pd.to_numeric(df["exchange_rate"])

df.to_csv("data/exchange_rates.csv", index=False)

print(df.head())
print(df.dtypes)

    

