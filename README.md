# Assignment-4
Codes of Assignment 4 from tude-due!
Task 1: Read a File and Handle Errors
Objective
The purpose of this task is to demonstrate how to open and read a text file in Python, display its contents line by line, and handle errors gracefully if the file does not exist.
Program Description
1. File Creation
The program creates a file named sample.txt (if required) and writes sample text into it.
This is done using file creation mode and the write() method.
"xt" mode creates a new file and raises an error if the file already exists.
The write() method stores text data inside the file.

2. Reading File Content
The file is opened in read mode ("rt"), and its content is displayed line by line.
A for loop is used to iterate through the file.
The enumerate() function provides automatic line numbering.
The strip() method removes unnecessary newline characters for clean formatting.
This ensures the output is structured and easy to read.
3. Exception Handling
The program uses a try-except block to handle potential errors.
If the file does not exist, Python raises a FileNotFoundError.
Instead of terminating abruptly, the program catches the error and displays a meaningful message.

Key Concepts Used
with open() context manager
File modes: "xt" and "rt"
try-except for exception handling
enumerate() for line numbering
strip() for formatting output

Task 2: Write and Append Data to a File
Objective
The purpose of this task is to demonstrate how to write user input to a file, append additional data, and display the final content of the file.
Program Description
1. Writing User Input
The program prompts the user to enter text.
The file output.txt is opened in write mode ("w").
Write mode creates the file if it does not exist.
If the file already exists, it overwrites the existing content.
The write() method stores the user input into the file.
2. Appending Additional Data
The program takes additional user input and opens the same file in append mode ("a").
Append mode adds new data to the end of the file.
It does not remove or overwrite existing content.
A newline character (\n) is added before appending to maintain proper formatting.
3. Reading Final Content
Finally, the file is opened in read mode ("r").
The read() method retrieves the entire content of the file.
The program then displays the combined final content.
Key Concepts Used
File modes: "w", "a", "r"
input() function
with open() context manager
Writing and appending data to files
Reading file content
Learning Outcome
After completing these tasks, the following concepts are understood:
File creation and writing
Appending data to existing files
Reading file content
Exception handling in file operations
Proper formatting of output
