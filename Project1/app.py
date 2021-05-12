#Import libraries
from difflib import get_close_matches
import sqlite3 as s
import json

#Path and Tablename for the database
path = "app.db"
tablename = "dictionary"

#Function to convert a list of tuples (of all the words) to a list of strings
def create_list_of_all_words():
    #Connects to database
    conn = s.connect(path)
    cur = conn.cursor()

    #Selects Word column from the table and fetches all words into list
    sel = "SELECT Word FROM dictionary"
    cur.execute(sel)
    conn.commit()
    #List has words stored as tuples
    allwords_tuples = cur.fetchall()
    #print(allwords_tuples)
    
    #Converts all the tuples to strings in another list
    allwords = []
    for word in allwords_tuples:
        allwords.append(word[0])

    #Returns list of all the words (as strings)
    return allwords


#Queries the database for a word
def query_word(word : str):
    #Connects to database
    conn = s.connect(path)
    cur = conn.cursor()

    #Selects from the table any data related to the particular word
    find = f"SELECT * FROM {tablename} WHERE Word='{word}'"
    cur.execute(find)
    conn.commit()
    #Stores this data in a list and returns list of word and meaning(s)
    res = cur.fetchall()
    return res


#Function to find words similar to the entered word if the word is misspelt
def select_similar(word : str):
    #A word is compared with a list of words to find similar words from the list to the user typed one
    #The function used takes the word, a list of words to compare and a cutoff percentage
    #The cutoff percentage means that a word has to be atleast that much similar to the current word to be considered
    #If the list that is returned is empty
    if len(get_close_matches(word, allwords, cutoff=0.7))==0:
        #There are no similar words and thus the word doesnt exist
        error = "The word does not exist or has been spelt incorrectly. Please double check it"
        return error
    else:
        #If the word entered is similar to another word, we fetch the most similar word from the list which is the first element
        #We ask the user if that is the word they meant
        most_similar_word = get_close_matches(word, allwords, cutoff=0.7)[0]
        query = input("Did you mean %s? Enter Y if yes and N if no: " % most_similar_word)
        #We change the user response to upper case to remove any room for confusion
        query = query.upper()
        #If the user types yes
        if query=='Y':
            #We query the most similar word in the database and return the meanings of that word
            meaning = query_word(most_similar_word)
            return meaning
        #If the user types no
        elif query=='N':
            #We give the user an error message
            error = "The word does not exist or has been spelt incorrectly. Please double check it"
            return error
        #If the user types a wrong option
        else:
            #Error message
            return "Please Enter a Valid Option"
    

#Function to find meaning of word
def find_meaning(word : str):
    #Lower case for normal words
    word = word.lower()
    #Capitalisation for Proper Nouns EG Texas, Delhi
    pnoun = word.title()
    #Upper case for acronyms EG API, USA, NASA
    acro = word.upper()

    #We query each type of word format in the database
    res1 = query_word(word)
    res2 = query_word(pnoun)
    res3 = query_word(acro)

    #If any of the queries return a response the other two will be empty
    #We return the response in a list with word and meaning(s)
    if res1:
        print("Normal Word")
        return res1
    elif res2:
        print("Proper Noun")
        return res2
    elif res3:
        print("Acronym")
        return res3
    #If none of the queries return anything the user has probably entered a wrong word
    else:
        print("Wrong Word")
        #We now check for a similar word in the database
        sim_res = select_similar(word)
        #This will either return a list of word and meanings or an error message 
        return sim_res

#List to store all the words of the dictionary as strings
allwords = create_list_of_all_words()
#print(allwords)


#Ask user for input word
word = input("Enter word: ")
#Find the meaning(s) of that particular word
meanings = find_meaning(word)
#print("MEANINGS:", meanings)

#If the returned value is a list and has content (is not empty)
if isinstance(meanings, list) and meanings:
    #Print each meaning
    for meaning in meanings:
        print(meaning[1])
#Else print whatever error message is necessary
else:
    print(meanings)

'''
#Loads data from JSON file into a dictionary
dict_data = json.load(open("data.json"))
#print(type(dict_data))
#print(dict_data)

#Function to find meaning of the word
def find_meaning(word : str):
    #Lower case for normal word
    word = word.lower()
    #If word is in the dictionary
    if word in dict_data:
        #We query the dictionary for the meanings
        word_meaning = dict_data[word]
        #Return the meaning
        return word_meaning
    
    #If word is not in dictionary we capitalise it for Proper Nouns Like Texas, Delhi etc
    elif word.title() in dict_data:
        #We then query the dictionary
        word_meaning = dict_data[word.title()]
        #Return the meaning
        return word_meaning

    #If word is not in dictionary we convert it to upper case for ACRONYMS -> USA, API, NASA
    elif word.upper() in dict_data:
        #We then query the dictionary
        word_meaning = dict_data[word.upper()]
        #Return the meaning
        return word_meaning

    #If word is not in the dictionary at all
    else:
        #The word is compared with a list of all the words to find similar words from the list to the user typed one
        #The function used takes the word, a list of words to compare and a cutoff percentage
        #The cutoff percentage means that a word has to be atleast that much similar to the current word to be considered
        #If the list that is returned is empty
        if len(get_close_matches(word, dict_data.keys(), cutoff=0.7))==0:
            #The word is not in the dictionary and nor does it have a similar word
            error = "The word does not exist or has been spelt incorrectly. Please double check it"
            #Return error
            return error

        #If the word returns a match of similar words
        else:
            #we fetch the most similar word from the list which is the first element
            #We ask the user if that is the word they meant
            most_similar_word = get_close_matches(word, dict_data.keys(), cutoff=0.7)[0]
            query = input("Did you mean %s? Enter Y if yes and N if no: " % most_similar_word)
            #We change the user response to upper case to remove any room for confusion
            query = query.upper()
            #If the user types yes
            if query=='Y':
                #We query the most similar word in the dictionary and return the meanings of that word
                word_meaning = dict_data[most_similar_word]
                return word_meaning
            #If the user types no
            elif query=='N':
                #Return error message
                error = "The word does not exist or has been spelt incorrectly. Please double check it"
                return error
            #If the user types an invalid option
            else:
                #Return error message
                return "Please Enter a Valid Option"

#Ask user to input word
word = input("Enter word: ")
#Find the meanings of that word
meanings = find_meaning(word)
#If the returned value is a list
if(isinstance(meanings, list)):
    #Print all the meanings
    for meaning in meanings:
        print(meaning)
#Print necessary error message
else:
    print(meanings)
'''