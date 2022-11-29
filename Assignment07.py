# ------------------------ #
# Title: Assignment 07
# Description: Create a new script that demonstrates how Pickling
#              and Structured Error Handling work.
# ChangeLog:
# SClendenning,25.11.2022, Created script & project folder
# SClendenning,26.11.2022, Added data variables & wrote pickling section
# SClendenning, 27.11.2022, Added section for structured error handling
# SClendenning, 29.11.2022, Adjusted print statements
# ------------------------ #

# Data: Pickling #
pickle_file = "datafile.dat" # a binary file that will be called upon and stored data to
book_titles = ["The Fifth Season", "Tehanu", "La Gesta dels Estels"] # loads in a list of 3 elements

# Processing: Pickle existing data to file #
import pickle # imports the pickle module
with open(pickle_file, "wb") as file: # once this with() is complete, it automatically closes the file
    pickle.dump(book_titles, file)  # dumps the existing data into the file

# Processing: Unpickle the file (load pickled data in) #
with open(pickle_file, "rb") as load_file:
    existing_data = pickle.load(load_file) # data in binary file is stored in this variable
    print("========================================" + '\n'
          + "Here is the pickled data from your file: " +
          '\n' + "========================================")
    for item in existing_data: # loops through data and prints it out in a readable format
        print(item)

# I/O: Pickling New Data #
print('\n') # Add new line so that existing data
            # and user input prompt doesn't look too cluttered

new_book = str(input("Write the title of a book you'd like to read. This title will be saved to your file: "))
book_titles.append(new_book) # appends new data to existing list

with open(pickle_file, "wb") as reopen_file:
    new_data = pickle.dump(book_titles, reopen_file) # writes the new data to the file

print("====================" + '\n' + "Books To Read (New!):" +
      '\n' + "====================")

for item in book_titles: # prints out updated list
    print(item)

# Combining Pickling and Structure Error Handling #
while(True):
    value1 = int(input("Please input a first number to be divided: "))
    value2 = int(input("Please input a second number to be divided: "))
    try:
        new_quotient = value1 / value2
        with open(pickle_file, "wb") as combined_file:
            new_values = pickle.dump(str(new_quotient), combined_file) # convert int to string
            print("Data saved to file.")

        with open(pickle_file, "rb") as load_quotient:
            load_result = pickle.load(load_quotient)
            print("This is the quotient from the unpickled file: ", load_result)
        break
    except ZeroDivisionError:
        print("Numbers cannot be divided by 0. Please input a different number.")