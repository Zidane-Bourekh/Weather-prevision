import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
import config


url = "https://meteostat.p.rapidapi.com/point/daily"

querystring = {"lat":"48.8566","lon":"2.3522","alt":"35","start":"2024-01-01","end":"2024-01-31"}  #latitude longitude of Paris

headers = {
	"x-rapidapi-key": config.API_KEY,
	"x-rapidapi-host": "meteostat.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json() #in the json "meta, data"

df = pd.DataFrame(data["data"])  #retrieve data from json response 


df.date = pd.to_datetime(df.date)   #convert date from string to datetime to use matplotlib

plt.plot(df.date, df.tavg)
plt.xticks(rotation = 90)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("average temperature on January 2024 in Paris")
plt.show()