# in this project we are going to handle the file read the file

# first step create a folder in this i gave the file handling name to the folder

# then go to the note pade and create a text file write anything you want

#  past that txt file in which folder have you created i past it in file handling folder

file = open("poem.txt")   # here we declare variable as a file name ypu can change this name
# open is used to file opening

print(file.readline())   # here with this we can read 1st line in the file

print(file.read())     # with this w e can read all the line from file

file.close()       # file closed

                      # or

# here with the help of with function you not need to define variable and open and close statments
# with fun open and close file by itself

with open("poem.txt")as poem:
    print(poem.read())

# printing all text in upper case
with open("poem.txt") as abc:
    for line in abc:
        print(line.strip().upper())   # for lower case replace upper with lower
        # strip function you can remove
