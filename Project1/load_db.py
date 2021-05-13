#Loads all words from JSON FILE INTO DICTIONARY TABLE IN LOCAL DB
#Because loading the json file everytime the program is run is inefficient
#Import libraries
import sqlite3 as s
import json

#Path for database
path = "app.db"

#Creates dictionary table
def create_dict():
    #Connects to database
    conn = s.connect(path)
    cur = conn.cursor()

    #Creates a table with 2 columns for word and meaning if the table doesnt already exist
    tbl = "CREATE TABLE IF NOT EXISTS dictionary(Word Text, Meaning Text)"
    cur.execute(tbl)
    conn.commit()

#Fills dictionary table with word and meaning -> data is a tuple of (word,meaning)
def fill_dict(tablename : str, data : tuple):
    #Connects to database
    conn = s.connect(path)
    cur = conn.cursor()

    #data[0] -> string -> WORD
    #data[1] -> list of tuples -> MEANING(S)
    # print("DATA[0]:", data[0])
    # print("DATA[1]:", data[1])

    #Insert each word into the dictionary as many times as the number of meanings for that word
    for i in range(len(data[1])):
        print(data[1][i])
        #Insert word and meaning
        insrt = f"INSERT INTO {tablename} VALUES(?, ?)"
        # insrt = f"INSERT INTO {tablename} VALUES {data[0], data[1][i]}"
        cur.execute(insrt, (data[0], data[1][i]))
        conn.commit()
        print("INSERTED WORD/MEANING INTO TABLE INTO TABLE")

#Load data from JSON file into dictionary
dict_data = json.load(open("data.json"))

#Create the table in the database 
create_dict()
#For all items in the dictionary
for (k,v) in dict_data.items():
    #Create a word,meaning tuple
    data = (k,v)
    #print(data)
    #Insert the data into the table
    fill_dict('dictionary', data)

print("Dictionary added to local db")