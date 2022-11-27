#### Seb Clendenning-Jimenez
#### Foundations of Programming: Python
#### November 26th, 2022
#### Assignment 07

# Pickling and Error-Handling Script:

## 1.1 Introduction:

This paper describes my script which addresses pickling and error-handling. Using the Separation of Concerns principles, I divided my script into one section for pickling and one for error-handling. These sections includes subsections for declaring data, processing data, and presenting or interacting with the user to obtain new data.

## 2.1 Pickling Article


## 2.2 Declaring Variables & Pickling Data:

For this section, I defined two variables: a binary file that would be used to store existing and new data, and a list variable that stored the data I wanted to pickle. Knowing that pickling can store and load complex sets of data, I created a list containing three elements. These variables can be seen in **Figure 1**. In **Figure 1**, my list is a variable which stores different book titles, which are represented as strings:

```
# Data: Pickling #

pickle_file = "datafile.dat" # a binary file that will be called upon and stored data to
book_titles = ["The Fifth Season", "Tehanu", "La Gesta dels Estels"] # loads in a list of 3 elements
```
##### Figure 1 — The code for the binary file that will store data and the existing list that will be used for this section of code.

For consistency within my script, I used the with statement and **open()** function throughout my section on pickling. This allowed me to review the parameters the function took, how the exact syntax worked, and allowed me to practice in understanding my own code as I wrote it. Therefore, each processing section for pickling in the following figures will look slightly similar, although object file names will look different.

After declaring my variables, I imported the pickle module. Since my data file was already declared, I could call and store it as an object file using the with statement and an **open()** function. Since this was the first time I would call the binary file, I set the object file’s name to **‘file’** (**Figure 2**). 

```
# Processing: Pickle existing data to file #

import pickle # imports the pickle module
with open(pickle_file, "wb") as file: # once this with() is complete, it automatically closes the file
    pickle.dump(book_titles, file)  # dumps the existing data into the file
```
#### Figure 2 — Importing the pickle module and using with and open() to pickle the existing list from Figure 1
The open function takes two arguments: the file name and the mode that you want the file to be stored as; I set this second argument to “wb”. In this mode, the “w” stands for ‘write’ and will write the existing list’s data to the binary file; the ‘b’ stands for binary, which will store the data in binary mode as opposed to storing it as comma-separated values, like we have been previously learning.

To remind myself of how pickling works, I added comments to each section. Specifically, I added that the with statement would close the function once it finishes working with the file. This allows me to not have to add a file.close() statement after the data is dumped into the binary file.

Within the with open() line, I added the pickle.dump() function. According to the Python documentation page on pickling (https://docs.python.org/3/library/pickle.html [External Link]), .dump “writes the object obj to the open file object file”. Following this notation, I wrote in the list book_titles to be written into my object file file. As before, this object file access the original binary file defined above.

Running this section of the script and opening the .dat file showed that the book titles from the list had been successfully dumped into the binary file. As mentioned by Professor Root and other articles I had read on pickling, **Figure 3** shows that the book titles are still in a readable format, but that the rest of the file contains unreadable characters:

![Figure 3 — The binary file opened in PyCharm, showing that the data is still somewhat readable to a human](https://github.com/scljimenez/IntroToProg-Python-Mod07/blob/main/docs/images/pickled_existing_data_to_file.png "Results of opening the binary file in PyCharm")
#### Figure 3 — The binary file opened in PyCharm, showing that the data is still somewhat readable to a human

## 2.3 Unpickling Existing Data:
The next step was to unpickle the stored data back into the script and display it to the user. I used a similar with-open() statement as I did in section 2.2, but this time renamed the file object that would open the pickled data as load_file (**Figure 4**). 
```
# Processing: Unpickle the file (load pickled data in) #
with open(pickle_file, "rb") as load_file:
    existing_data = pickle.load(load_file) # data in binary file is stored in this variable
    print("Here is the pickled data from your file: ")
    for item in existing_data: # loops through data and prints it out in a readable format
        print(item)
```
#### Figure 4 — Code that loads in and unpickles data from binary file
In the with-open line, I again called the .dat file, but this time set the mode to “rb”. In this mode, “rb” will read the pickled data from the binary file and assign it to the file object load_file. I also created a local variable, existing_data, that would load the pickled data from the file object. By creating a new local variable, I can use it and call the variable should I want to display the data to the user.

As we saw in **Figure 3**, the binary file does not present the most user-friendly or readable format for the pickled data to be understood by the user using my script. To remedy this, I used a for-loop to loop through the variable existing_data. Since existing_data has access to the binary file, it can easily loop through the data and print out each element from the original list. Before the for-loop, I included a print statement that reminded the user what this data is and where it comes from. **Figure 5** shows the results of running the code chunk from **Figure 4**: 

![Figure 5 — Printing out the unpickled data from the binary file](https://github.com/scljimenez/IntroToProg-Python-Mod07/blob/main/docs/images/unpickled_printed_data.png "The unpickled and printed out data that had been stored in the binary file")
#### Figure 5 — The unpickled and printed out data that had been stored in the binary file

## 2.4 Taking in and Pickling New Data:
To ensure that I understood how pickling worked, I wanted to try adding in some user-input data to the script. I created a new section called I/O: Pickling New Data that would take in a user’s new book title, append that title to the existing list, and pickle that new list to the binary file. **Figure 6** shows this process:
```
# I/O: Pickling New Data #

print('\n') # Add new line so that existing data
            # and user input prompt doesn't look too cluttered

new_book = str(input("Write the title of a book you'd like to read: "))
book_titles.append(new_book) # appends new data to existing list

with open(pickle_file, "wb") as reopen_file:
    new_data = pickle.dump(book_titles, reopen_file) # writes the new data to the file

print("Books To Read (New!):", '\n')
for item in book_titles: # prints out updated list
    print(item)
```
#### Figure 6 — Taking in user-input data and pickling it to the file.
In this section, I first added an additional new line so that when this script is run in PyCharm or a Command Shell, the existing list that is loaded in and presented to the user is separated from the user-input prompt. 

I created a new variable, new_book, which took a string input from the user and asked them to input a title of a book that they’d like to read. Using the .append() function, I then had that title be appended to the existing book_title s list.

I used similar code from **Figure 2** to write the updated list to the binary file. Calling on the binary file and using “wb” again to write the information to the binary file, I set the file-object as reopen_file. Since the data in book_titles had been updated through the .append() function, the data that is dumped into the binary file includes the new user data that was captured from the input prompt.

Similar to **Figure 4**, I used another for-loop that would loop through the updated list and print out each book title for the user. **Figure 7** and **Figure 8** show the entire pickling section of this script being run in PyCharm:
![Figure 7](https://github.com/scljimenez/IntroToProg-Python-Mod07/blob/main/docs/images/running_script_pycharm.png "The script running in PyCharm, showing three things: unpickled data displayed to the user, the user inputting a new book title, and the new updated list of data printed out to the user")
#### Figure 7 — The pickling section running in PyCharm, showing the first list, the user's input, and the new list with updated data

![Figure 8](https://github.com/scljimenez/IntroToProg-Python-Mod07/blob/main/docs/images/new_list.png "The new list saved to the binary file, showing four items in the updated list")
#### Figure 8 — The binary file opened in PyCharm, showing the updated list.
