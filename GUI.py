# Importing the library
import os
import tkinter as tk
from datetime import date
from word_scraper import today_s_word

# Creating a window
window = tk.Tk()

# Title for the window
window.title("Word of the Day")


# Taking output from the function which scrapes the website and provdes
# the word, its meaning, its type and how it is pronounced as output
word,  meaning, pronoun, type_x = today_s_word()
whole_word = word.title() + ' - ' + meaning + "\n" + pronoun + " || " + type_x

# The whole word consists of everything stiched together to be displayed
disp = tk.Label(text=whole_word)

# Importing today's date
d = date.today()

# Stiching together everything to be saved in a file
word_stiched_together = word + ',' + meaning + ',' + type_x + ',' + "\n"

# Following function checks if file exists in the path or not


def file_exists_or_not(file_path):
    return os.path.isfile(file_path)


# Following function performs following tasks-
# 1. It searches if the file exists or not. If not, it creates one.
# 2. If file is already present, it reads the file and returns wheather the string is present or not
# 3. If present, it does not append the word to the file, and return a message and the date at which this word was encountered
# 4. If not present, it appends the word to the file along with the date


def string_to_be_searched(file_name, string_to_search):

    # Uncomment the print statements to view the flow of the program
    #print("Checking if the file exists or not.")

    x = file_exists_or_not(file_name)
    if x:

        #print("File exists. Checking if the word exists.")
        with open(file_name, 'r') as read_obj:
            for line in read_obj:
                if string_to_search in line:
                    date_appended = line.split(',')

                    #print("You already came across this word on", date_appended[0] + '.')
                    return None
        return 1
    else:

        #print("File does not exist. Creating a new one and appending the word to it.")
        return 0


file_path = os.getcwd() + '/word.txt'


out = string_to_be_searched(file_path, word_stiched_together)

# Updating the word to be appended to the file with the date
word_stiched_together = str(d) + ',' + word + ',' + \
    meaning + ',' + type_x + ',' + "\n"
if out == 0:
    with open(file_path, 'a') as f:

        #print('Creating a new file and writing to it')
        f.write(word_stiched_together)
elif out == 1:
    with open(file_path, 'a') as f:

        #print('Appending new word to the existing file')
        f.write(word_stiched_together)

disp.pack()
window.mainloop()
