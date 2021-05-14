#Loads all words from JSON FILE INTO DICTIONARY TABLE IN LOCAL DB
#Because loading the json file everytime the program is run is inefficient
#Import libraries
import sqlite3 as s
import json

#Path for database
path = "dict.db"

#Creates dictionary table
def create_dict():
    #Connects to database
    conn = s.connect(path)
    cur = conn.cursor()

    #Creates a table with 2 columns for word and meaning if the table doesnt already exist
    tbl = "CREATE TABLE IF NOT EXISTS dictionary(Word Text, Meaning Text)"
    cur.execute(tbl)
    #Commits to database
    conn.commit()

#Fills dictionary table with word and meaning -> data is a tuple of (word,meaning)
def fill_dict(tablename : str, data : tuple):
    #data[0] -> string -> WORD
    #data[1] -> string -> MEANING(S) separated by "~~"
    # print("DATA[0]:", data[0])
    # print("DATA[1]:", data[1])

    #Insert word and meaning
    insrt = f"INSERT INTO {tablename} VALUES(?, ?)"
    # insrt = f"INSERT INTO {tablename} VALUES {data[0], data[1]}"
    cur.execute(insrt, (data[0], data[1]))
    #conn.commit()
    print("INSERTED WORD/MEANING INTO TABLE INTO TABLE")

#Load data from JSON file into dictionary
dict_data = json.load(open("data.json"))

#Create the table in the database 
create_dict()

#Connects to database before filling the db with word/meanings
conn = s.connect(path)
cur = conn.cursor()

#For all items in the dictionary
for (k,v) in dict_data.items():
    #Extract meanings from list into 1 string
    meaning = ""
    #Strings are separated by "~~"
    for m in v:
        meaning = meaning + m + "~~"
    # print(meaning)
    # print(type(meaning))
    #Create a word,meaning tuple
    data = (k,meaning)
    #print(data)
    #Insert the data into the table
    fill_dict('dictionary', data)

#Commit all changes to the db after entire dictionary has been filled
conn.commit()
print("Dictionary added to local db")