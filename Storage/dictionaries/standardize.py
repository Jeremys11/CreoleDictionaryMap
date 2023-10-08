import json
import csv
import ast
import pandas as pd


ACROLECT_LIST = {"Haitian Creole":"French","Jamaican Creole":"English","Louisiana Creole":"French",
    "Martinique Antillean Creole":"French","Antillean Creole":"French","Suriname Saramaccan Creole":"English-Portugese",
    "Nigerian Pidgin English":"English"}

## CREOLE LAT-LON COORDIATES
TEMP = open("Storage/dictionaries/location_point.json")
CREOLE_LOCATIONS = json.load(TEMP)

## LOCATION OF CREOLE DICTIONARIES CSV
CREOLE_DICTIONARY_LIST = {"Haitian Creole":"hatian_creole_dictionary_v4.csv",
    "Jamaican Creole":"Jamaican Creole.csv",
    "Louisiana Creole":"louisiana_creole_dictionary.csv",
    "Martinique Antillean Creole":"Excelmartinique.csv",
    "Antillean Creole":"stLucia.csv",
    "Suriname Saramaccan Creole":"Saramaccan.csv",
    "Nigerian Pidgin English":"nigeria.csv"
}

def createCombined():
    with open('Storage/dictionaries/BigThing.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        row = ['word','creole_word','creole_name','latlon','acrolect']
        writer.writerow(row)

    for key in ACROLECT_LIST.keys():
        with open('Storage/dictionaries/'+CREOLE_DICTIONARY_LIST[key]) as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            for row in rows[1:]:
                if(row[2]) == "Haitian":
                    row[2] = "Haitian Creole"
                elif(row[2] == "Martinique"):
                    row[2] = "Martinique Antillean Creole"
                elif(row[2]) == "Jamaican Creole":
                    row[2] = "Jamaican Creole"
                elif(row[2] == "Louisiana Creole"):
                    row[2] = "Louisiana Creole"
                elif(row[2] == "Nigeria"):
                    row[2] = "Nigerian Pidgin English"
                elif(row[2] == "Saramaccan"):
                    row[2] = "Saramaccan"
                elif(row[2] == "St. Lucia"):
                    row[2] = "Antillean Creole"
                else:
                    break
                row.append(CREOLE_LOCATIONS[key])
                row.append(ACROLECT_LIST[key])
        with open('Storage/dictionaries/BigThing.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows[1:])

    with open("Storage/dictionaries/BigThing.csv",'r',newline='') as csvfile, open('Storage/dictionaries/combined.csv','w',newline='') as combo:
            reader = csv.reader(csvfile, delimiter=",")
            writer = csv.writer(combo,delimiter=",")
            for row in reader:
                mylist = []
                for field in row:
                    myfield = field.strip()
                    mylist.append(myfield)
                writer.writerow(mylist)

def csvTojson():
    df = pd.read_csv ("Storage/dictionaries/Creole_Languages.csv")
    df.to_json ("Storage/dictionaries/Creole_Languages.json")


csvTojson()