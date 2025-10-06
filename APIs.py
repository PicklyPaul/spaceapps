#Imports
#from pyscript import Elements
import requests as req
import googlemaps
import pandas 
from bs4 import BeautifulSoup
from flask import Flask, request



#bs4: HTML inputs
with open("Will_It_Rain_On_My_Parade.html", 'r') as f:
    html_c = f.read()

soup = BeautifulSoup(html_c, 'html.parser')

post_form = soup.find('form', id='form')

if post_form:
        input_fields = {}
        for input_tag in post_form.find_all('input'):
            name = input_tag.get('name')
            value = input_tag.get('value')
            if name:  # Only store if the input has a name
                input_fields[name] = value if value is not None else '' # Handle cases where value might be missing

        print("Extracted input fields:", input_fields)
else:
    print("No POST form found in the HTML.")

#submit_Address = input_fields.get('zip-input')
#submit_Date = input_fields.get('date-input')

submit_Address = "4493 Hummingbird Cir, Folsom CA"
submit_Date = "08/05/2010"

#Google Maps : Location -> Cordinates
maps = googlemaps.Client(key='AIzaSyA2bVms-LLPV4VAYvWWUzKRHW90-ACAfFM')

address = f"{submit_Address}"
geocode = maps.geocode(address)

if geocode:
    location = geocode[0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
    print(f"{latitude}, {longitude}")
else:
    print("address not found")


#info = req.get("", x=latitude,y=longitude, date=submit_Date())

#Pandas : CSV from Paul's DB
df = pandas.read_csv("Sample.csv",header=None)

print(df)
#temp = df[0]
#print
temp = df.iloc[0,0]
print(temp)

with open("Will_It_Rain_On_My_Parade.html", 'r') as c:
    content = c.read()
print(content)

target_temp = soup.find('span', id='temp')
target_temp.string = temp