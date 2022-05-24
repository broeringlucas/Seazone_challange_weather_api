
import requests 
import pandas as pd 

#Requesting the data from the weather api;
url = "https://api.hgbrasil.com/weather?key=b661e56d&city_name=Jurerê"

r = requests.get(url).json()

#FIltering the data from the weather api;
final_list = []
index = 0 
city_name = r['results']['city_name']
acquisition_date = r['results']['date']

for item in r["results"]["forecast"]:
    adding = ([index, acquisition_date, item["date"], item["max"], item["min"], city_name, item["condition"]]) 
    index += 1
    final_list.append(adding)

#Saving the data in a csv file with the pandas module;
save = pd.DataFrame(final_list, columns = ('Index', 'Acquisition date', 'Target date', 'Max temp', 'Min temp', 'Location', 'Conditions'))
save.to_csv('jurere_forecast.csv', mode = 'a', index = False )

#Reading the data and deleting duplicates to save multiple times in the same csv file;
df = pd.read_csv('jurere_forecast.csv')
df.drop_duplicates(inplace=True)
df.to_csv('jurere_forecast.csv',index = False)

#Filtering the data from the csv file to aswer the questions;
type_forecast = input("Type 1 to the forecast of a specfic date and 2 to a range of dates: ")

forecast = df
#Input a date is this format: (day/month), Example: 20/03;
if type_forecast == "1": 
    city_name ,date= input("Choose a location and a date(%d/%m): ").split()
    forecast = df.loc[df["Target date"].str.contains(date) == True]
    if date == False:
        forecast = print("Invalid input, try again. ")
        city_name ,date= input("Choose a location and a date(%d/%m): ").split()

elif type_forecast == "2": 
    city_name, start_date, end_date = input("Choose a location and a range of dates(%d/%m): ").split() 
    forecast = df = df[(df['Target date']>=start_date ) & (df['Target date']<=end_date)]

print(forecast)