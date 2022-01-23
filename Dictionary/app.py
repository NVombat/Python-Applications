from difflib import get_close_matches
import sqlite3 as s
import json

tablename = "dictionary"
path = "dict.db"

def create_list_of_all_words() -> list:
    '''
    Convert a list of tuples (of all the words) to a list of strings

    Returns:
        list
    '''
    conn = s.connect(path)
    cur = conn.cursor()

    sel = "SELECT Word FROM dictionary"
    cur.execute(sel)
    conn.commit()

    allwords_tuples = cur.fetchall()
    allwords = []
    for word in allwords_tuples:
        allwords.append(word[0])

    return allwords


def query_word(word : str) -> list:
    '''
    Queries the database for a word

    Args:
        word

    Returns:
        list
    '''
    conn = s.connect(path)
    cur = conn.cursor()

    find = f"SELECT * FROM {tablename} WHERE Word='{word}'"
    cur.execute(find)
    conn.commit()
    res = cur.fetchall()
    return res


def select_similar(word : str) -> str:
    '''
    Find words similar to the entered word if the word is misspelt

    Args:
        word

    Returns:
        str
    '''
    if len(get_close_matches(word, allwords, cutoff=0.7))==0:
        error = "The word does not exist or has been spelt incorrectly. Please double check it"
        return error
    else:
        most_similar_word = get_close_matches(word, allwords, cutoff=0.7)[0]
        query = input("Did you mean %s? Enter Y if yes and N if no: " % most_similar_word)
        query = query.upper()

        if query=='Y':
            meaning = query_word(most_similar_word)
            return meaning
        elif query=='N':
            error = "The word does not exist or has been spelt incorrectly. Please double check it"
            return error
        else:
            return "Please Enter a Valid Option"


def find_meaning(word : str) -> list:
    '''
    Find meaning of word

    Args:
        word

    Returns:
        list
    '''

    orig_word = word
    lword = word.lower()
    pnoun = word.title()
    acro = word.upper()

    res1 = query_word(lword)
    res2 = query_word(pnoun)
    res3 = query_word(acro)

    if res1:
        print("Normal Word")
        return res1
    elif res2:
        print("Proper Noun")
        return res2
    elif res3:
        print("Acronym")
        return res3
    else:
        print("Wrong Word")
        sim_res = select_similar(orig_word)
        return sim_res


allwords = create_list_of_all_words()

word = input("Enter word: ")
meanings = find_meaning(word)

if isinstance(meanings, list) and meanings:
    for meaning in meanings[0][1].split("~~"):
        if meaning=='':
            break
        print(meaning)
else:
    print(meanings)

'''
#Loads data from JSON file into a dictionary
dict_data = json.load(open("data.json"))

#Function to find meaning of the word
def find_meaning(word : str):
    word = word.lower()
    if word in dict_data:
        word_meaning = dict_data[word]
        return word_meaning

    elif word.title() in dict_data:
        word_meaning = dict_data[word.title()]
        return word_meaning

    elif word.upper() in dict_data:
        word_meaning = dict_data[word.upper()]
        return word_meaning

    else:
        if len(get_close_matches(word, dict_data.keys(), cutoff=0.7))==0:
            error = "The word does not exist or has been spelt incorrectly. Please double check it"
            return error

        else:
            most_similar_word = get_close_matches(word, dict_data.keys(), cutoff=0.7)[0]
            query = input("Did you mean %s? Enter Y if yes and N if no: " % most_similar_word)
            query = query.upper()
            if query=='Y':
                word_meaning = dict_data[most_similar_word]
                return word_meaning
            elif query=='N':
                error = "The word does not exist or has been spelt incorrectly. Please double check it"
                return error
            else:
                return "Please Enter a Valid Option"

word = input("Enter word: ")
meanings = find_meaning(word)
if(isinstance(meanings, list)):
    for meaning in meanings:
        print(meaning)
else:
    print(meanings)
'''