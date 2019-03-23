import urllib
import random
import time
import pyperclip
# chosen file
filename = 'bee-movie-script.txt'
lineRn = 0 # For ordered mode
randomVal = 0;
copyTime = False;

def getDelay():
    print("Start time in seconds?\n")
    y = input()
    try:
        while int(y) > 0:
            print("Starting in: ", y)
            y = int(y) - 1
            time.sleep(1)
    except ValueError:
        print("That's not a number, try again. \n")
        getDelay()


def getCopyDelay():
    global copyTime
    if copyTime == False:
        print("Copy time (in seconds)?\n")
        copyTime = input()

        try:
            int(copyTime)
            copyTime = int(copyTime)
            print("Copy time: ", copyTime, "\n")
            getDelay()
        except ValueError:
            print("That's not a number, try again. \n")
            copyTime = False
            getCopyDelay()




def randomOrOrdered():
    global randomVal
    print("Random or ordered? \n")
    x = input()

    if x == "random" or x == "Random":
        randomVal = True
        getCopyDelay()
    elif  x == "ordered" or x == "Ordered":
        randomVal = False
        getCopyDelay()
    else:
        print("Invalid input: \nPossible inputs are: 'Random', 'random', 'Ordered, 'order' \nPlease try again. \n")
        randomOrOrdered()

# Gets lines, picks 10 random lines from the script
def getLines():
    global randomVal
    # pick random lines
    if randomVal == True:
        rand = random.randint(0, (len(lines)))
        numOfLines = random.randint(0, 8)
        choosenLines = lines[rand:(rand + numOfLines)]
    elif randomVal == False:
        global lineRn
        numOfLines = random.randint(1, 4)
        choosenLines = lines[lineRn:(lineRn + numOfLines)]
        lineRn = lineRn + numOfLines

        if lineRn == len(lines):
            lineRn = 0;

    text = ""
    # remove line breaks so it's ready for pasting
    for line in choosenLines:
        line = line.replace('\n', '')
        text = text + line
    # copies line to clipboard
    pyperclip.copy(text)
    print(text)

randomOrOrdered()

# Open the file and read lines
with open(filename, 'r') as infile:
    # Read all lines into memory
    lines = infile.readlines()
    # Get rid of new lines
    # runs this function with a new line every 2 seconds
    while(True):
        getLines()
        time.sleep(copyTime)

# Changes:
    # Input to select file name => so it's not hard coded in
    # And an algorithmn that organizes text files properly with a certain range of characters per line
    # Updated readme and more info there
