'''
Python uses file objects to interact with external files on your computer. 
These file objects can be any sort of file you have on your computer, whether it be an audio file, 
a text file, emails, Excel documents, etc. Note: You will probably need to install certain libraries 
or modules to interact with those various file types, but they are easily available. 
(We will cover downloading modules later on in the course).
Python has a built-in open function that allows us to open and play with basic file types. 
First we will need a file though. We're going to use some iPython magic to create a text file!
'''

#Let's first create a new text file. You can name it anything you like,
#in this example we will name it "newfile.txt".
s = ("hello world in the new file" + "\n" + 
     "this is great")
print(s)
file = open("newfile.txt", "w")
file.write(s)

file = open("newfile.txt")

'''
In order to not have to reset every time, we can also use the readlines method. Use caution
with large files, since everything will be held in memory. We will learn how to iterate over large
files later in the course
'''

print("TEXT FILE OBJECT METHODS")

print("")
print(".read")
print("")
print(".read RETURNS A STRING WITH ALL THE LINE CONTENT")
print(file.read())
print(file.read()) #Cursor at the end of the file
file.seek(0) #Re-sets cursor position
print(file.read())
file.seek(0) #Re-sets cursor position

print("")
print(".read().splitlines()")
print("")
print(".read RETURNS A LIST WITH THE CONTENT OF EACH LINE")
print("Note how the new character line us not included")
print(file.read().splitlines())
file.seek(0)

print("")
print(".readlines")
print("")
print(".readlines RETURNS A LIST OF THE LINES IN THE FILE")
print("note .readlines detects the newline character character")
print(file.readlines())
print "END"

#WRITING TO A FILE
print("")
print("WRITTING TO A FILE")

    #Note between w and w+
    #w
    #Opens a file for writing only. Overwrites the file if the file exists. 
    #If the file does not exist, creates a new file for writing.
    #w+
    #Opens a file for both writing and reading. Overwrites the existing file 
    #if the file exists. If the file does not exist, creates a new file for reading and writing.

# Add a second argument to the function, 'w' which stands for write
my_file = open('test.txt','w')

#NOTE: THE OPTION w+ yields an error, at least within my programming environment

# Write to the file
my_file.write('First Line' + "\n" + "Second Line" + "\n" + "Third Line")

my_file = open('test.txt','r')

#We could call the line object anything
for line in my_file:
    print line 

#IMPORTANT!! By not calling the .read() method, we avoided storing the file in memory

