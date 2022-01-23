#Loads all words from JSON FILE INTO DICTIONARY TABLE IN LOCAL DB
import sqlite3 as s
import json

path = "dict.db"

def create_dict():
    '''
    Creates dictionary table
    '''
    conn = s.connect(path)
    cur = conn.cursor()

    tbl = "CREATE TABLE IF NOT EXISTS dictionary(Word Text, Meaning Text)"
    cur.execute(tbl)
    conn.commit()


def fill_dict(tablename : str, data : tuple):
    '''
    Fills dictionary table with word and meaning

    Args:
        tablename: string
        data: tuple(word,meaning)
    '''
    insrt = f"INSERT INTO {tablename} VALUES(?, ?)"
    cur.execute(insrt, (data[0], data[1]))

dict_data = json.load(open("data.json"))

create_dict()

conn = s.connect(path)
cur = conn.cursor()

for (k,v) in dict_data.items():
    meaning = ""
    for m in v:
        meaning = meaning + m + "~~"

    data = (k,meaning)
    fill_dict('dictionary', data)

conn.commit()
print("Dictionary added to local db")