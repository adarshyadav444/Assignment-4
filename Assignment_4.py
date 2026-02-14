# Task 1: Read a File and Handle Errors
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
""""
#Step1: Let's Create a "sample.txt" file and store some lines into it.
with open("sample.txt", "xt") as fh:
    fh.write("Hii! I'm adarsh!")
    fh.write("\nI'm learning python form tudedude")

#Step2: Now Let's Open this file in read mode and print's it's content line by line!
#Also, If File Doesn't Exist then Handle Error!
try:
    with open("sample.txt", "rt") as fh:
        print("Reading File Content:")
        for line_no, Line in enumerate(fh, start=1):
            print(f"Line{line_no}: {Line.strip()}")
except FileNotFoundError as Error: #It Runs When Error Occur
    print("File Does Not Exist!")
    print(Error) #It Prints The Actual Error 
"""""
from importlib.resources import contents

#Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

#Step1: Take a input from user thne open file output.txt & write the variable in which input is stored
open_text = input("Enter text to write to the file: ")
with open("output.txt", "wt") as fh:
    fh.write(open_text)
    print("Data Successfully Written to output.txt.")
append_text = input("Enter text to append to the file: ")
#Step2: Similarly open file in "a" append mode & append the variable in which append input is stored
with open("output.txt", "at") as fh:
    fh.write("\n"+append_text)
    print("Data Appended to output.txt.")
#Step3: Atlast print the final output
print("Final Content of output.txt:")
with open("output.txt", "rt") as fh:
    data = fh.read()
    print(data)






