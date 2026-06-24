#NLP assessment template 2026

# Note: The template functions here and the dataframe format for structuring your solution is a suggested but not mandatory approach. You can use a different approach if you like, as long as you clearly answer the questions and communicate your answers clearly.

import nltk
import spacy
import os
import pandas
from pathlib import Path


nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2000000



def fk_level(text, d):
    """Returns the Flesch-Kincaid Grade Level of a text (higher grade is more difficult).
    Requires a dictionary of syllables per word.

    Args:
        text (str): The text to analyze.
        d (dict): A dictionary of syllables per word.

    words = 0.0
    syllables = 0.0
    sentences = 0.0

    restult = round(((words/sentences)*0.39)+((syllables/words)*11.8) - 15.59), 2)

    return result

    Returns:
        float: The Flesch-Kincaid Grade Level of the text. (higher grade is more difficult)
    """
    pass


def count_syl(word, d):
    """Counts the number of syllables in a word given a dictionary of syllables per word.
    if the word is not in the dictionary, syllables are estimated by counting vowel clusters

    Args:
        word (str): The word to count syllables for.
        d (dict): A dictionary of syllables per word.

    

    Returns:
        int: The number of syllables in the word.
    """
    pass

def count_words(text):
    #print(text)
    tokens = nltk.word_tokenize(text.lower())
    alphanumTokens=[]
    for token in tokens:
        if token.isalnum():
            alphanumTokens.append(token)
    
    return len(alphanumTokens)




def read_novels(path=Path.cwd() / "texts" / "novels"):
    """Reads texts from a directory of .txt files and returns a DataFrame with the text, title,
    author, and year"""
    
    

    file_type = ".txt" # if your data is not in a plain text format, you can change this
    filenames = []
    rawData = {"text":[], "title": [], "author":[], "year":[]}

    # this for loop will run through folders and subfolders looking for a specific file type
    for root, dirs, files in os.walk(path, topdown=False):
    # look through all the files in the given directory
        for filename in files:
            with open(os.path.join(root, filename), encoding='utf-8') as currentFile:
                if (root + os.sep + filename).endswith(file_type):
                    details = filename.split("-")
                    rawData["year"].append(details.pop()[:-4])
                    rawData["title"].append(details.pop(0))
                    rawData["author"].append(details.pop(0))
                    rawData["text"].append(currentFile.read())
                    currentFile.close()

    dataframe = pandas.DataFrame(data=rawData)
    dataframe = dataframe.sort_values(by='year', ascending=True)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def parse(df, store_path=Path.cwd() / "pickles", out_name="parsed.pickle"):
    """Parses the text of a DataFrame using spaCy, stores the parsed docs as a column and writes 
    the resulting  DataFrame to a pickle file"""
    pass


def nltk_ttr(text):
    """Calculates the type-token ratio of a text. Text is tokenized using nltk.word_tokenize."""
    #print(text)
    tokens = nltk.word_tokenize(text.lower())
    alphanumTokens=[]
    for token in tokens:
        if token.isalnum():
            alphanumTokens.append(token)
    
    types = set(alphanumTokens)
    total_tokens = len(alphanumTokens)
    total_types = len(types)
    ttr = total_types / total_tokens
    print(ttr)
    return ttr


def get_ttrs(df):
    """helper function to add ttr to a dataframe"""
    results = {}
    for i, row in df.iterrows():
        results[row["title"]] = nltk_ttr(row["text"])
    return results


def get_fks(df):
    """helper function to add fk scores to a dataframe"""
    results = {}
    cmudict = nltk.corpus.cmudict.dict()
    for i, row in df.iterrows():
        results[row["title"]] = round(fk_level(row["text"], cmudict), 4)
    return results


#.. add functions for part (e) here



if __name__ == "__main__":
    """
    uncomment the following lines to run the functions once you have completed them
    """
    path = Path.cwd() / "texts" / "novels"
    print(path)
    read_novels(path)
    df = read_novels(path)
    print(df.head())
    # nltk.download("cmudict")
    # nltk.download("punkt")
    # parse(df)
    # print(df.head())
    # print(get_ttrs(df))
    # print(get_fks(df))
    # df = pd.read_pickle(Path.cwd() / "pickles" /"name.pickle")
    # call functions for part (e) here.
