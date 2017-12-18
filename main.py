import pandas,os
import geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def do_geocode(df):
    try:
        df["Coordinates"]=df["Address"].apply(nom.geocode)
        return
    except GeocoderTimedOut:
        return do_geocode(df)

df=pandas.read_csv("supermarkets.csv")
nom=Nominatim()
df["Address"]=df["StreeetNo"]+", "+df["StreetName_Suffix"]+", "+df["Municipality"]
do_geocode(df)
df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x!=None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x!=None else None)
df.to_csv('result.csv', sep=',', encoding='utf-8')
