"""
Describe the program

Name - Date
"""

import string
def get_file_contents(filename: str) -> str:
    """
    Retrieves the entire contents of a file. This function will also print an
    error if there was an issue
    Parameters:
        filename(str): The name of the file to open
    Return:
        str: The contents of the file as a string    
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ruh-roh. File '{filename}' was not found.")
     

def clean_text(text: str) -> str:
    """
    Removes all non-alphabetic characters, including spaces from the text.
    Parameters:
        text(str): The text to clean up
    Return:
        str: The cleaned-up text
    """
    pass
    # TODO: Write code that only keeps alphabetic characters and returns the clean string

def get_char_count(text: str) -> dict[str,int]:
    """
    Counts up the individual characters in a string. Each key is a character - there is one key called "total"
    that adds up all the keys.
    Parameters: 
        text(str): The string to analyze
    Return:
        dict[str,int]: A dictionary where the keys are the characters and the values are the counts
    """
    result: dict[str, int] = {"total": 0} # start off with a total of 0
    
    # TODO: Write code that counts the characters in the text

    return result

def print_summary(summary: dict[str, int]) -> None:
    """
    Write the docstring for this function.
    """
        # sort by value in descending order
    sorted_data = sorted(summary.items(), key = lambda item: item[1], reverse = True)
        # print out the highest occuring characters, and get a relative frequency count
    for character, count in sorted_data:
        print(f"{character}: {count} ({count/summary["total"]*100:.2f}%)")

def main() -> None:
    pass
    # TODO: write code that reads in each of the data files and calls the various
    # functions to clean and count 
    

if __name__ == "__main__":
    main()