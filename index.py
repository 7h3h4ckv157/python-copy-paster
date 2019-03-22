import urllib
import random
import time
import pyperclip
# chosen file
filename = 'bee-movie-script.txt'

# Gets lines from the bee movie script, picks 10 random lines from the script
def getLines():
    # pick random lines
    rand = random.randint(0, (len(lines)))
    numOfLines = random.randint(0, 8)
    choosenLines = lines[rand:(rand + numOfLines)]
    #print(choosenLines)
    text = ""
    # remove line breaks so it's ready for pasting
    for line in choosenLines:
        line = line.replace('\n', ' ')
        text = text + line
    # copies line to clipboard
    pyperclip.copy(text)
    # print(text)
    pyperclip.paste()


# Open the file and read lines
with open(filename, 'r') as infile:
    # Read all lines into memory
    lines = infile.readlines()
    # Get rid of new lines
    # runs this function with a new line every 2 seconds
    while(True):
        getLines()
        time.sleep(2)
