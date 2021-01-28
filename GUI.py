#Importing the library
from datetime import date
import tkinter as tk
from word_scraper import today_s_word

#Creating a window
window = tk.Tk()

#Giving the window a title
window.title("Word of the Day")

#Taking output from the function which scrapes the website and provdes 
#the word, its meaning, its type and how it is pronounced as output
word,  meaning, pronoun, type_x = today_s_word()
whole_word = word.title() + ' - ' + meaning[2:] +"\n" + pronoun + " || " + type_x

#The whole word consists of everything stiched together to be displayed
disp = tk.Label(text = whole_word)

#Importing today's date 
d = date.today()

#Stiching together everything to be saved in a file
a = str(d) + ',' + word + ',' + meaning + ',' + type_x + ',' + "\n"

#Following function performs following tasks-
#1. It searches if the file exists or not. If not, it creates one.
#2. If file is already present, it reads the file and returns wheather the string is present or not
#3. If present, it does not append the word to the file, and return a message and the date at which this word was encountered
#4. If not present, it appends the word to the file along with the date

def string_to_be_searched(file_name, string_to_search):
    try:
        with open(file_name, 'r' ) as read_obj:
            for line in read_obj:
                if string_to_search in line:
                    ''' #uncomment these if you wish to run the program without a scheduler
                    x = line.split(',')
                    print("You already came across this word on", x[0])
                    '''
                    return 1
    except:
        with open('word.txt', 'a') as f:
            f.write(a)
    
    return 0

out = string_to_be_searched('word.txt', a)
if out == 0:
    '''                #uncomment these if you wish to run the program without a scheduler
    print("New day, New word")
    '''
    with open('word', 'a') as f:
        f.write(a)
        

disp.pack() 
window.mainloop()