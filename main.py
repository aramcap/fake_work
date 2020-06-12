from random import random, randint
from datetime import datetime, timedelta
from time import sleep

commandStart = ['Performing DNS Lookups for',
'Searching ',
'Analyzing ',
'Estimating Approximate Location of ',
'Compressing ',
'Requesting Authorization From : ',
'wget -a -t ',
'tar -xzf ',
'Entering Location ',
'Compilation Started of ',
'Downloading '
]

commandParts = ['Data Structure',
'http://www.com?au&2',
'Texture',
'TPS Reports',
' .... Searching ... ',
'http://anb.es/?23&88&far=2',
'http://abc.es/?timing=1ww'
]

commandResponses = ['Authorizing ',
'Authorized...',
'Access Granted..',
'Going Deeper....',
'Compression Complete.',
'Compilation of Data Structures Complete..',
'Entering Security Console...',
'Encryption Unsuccesful Attempting Retry...',
'Waiting for response...',
'....Searching...',
'Calculating Space Requirements '
]

def consoleOutput():
    while True:
        commandType = randint(0,10)
        if commandType == 0:
            print(commandStart[randint(0,len(commandStart)-1)] + commandParts[randint(0,len(commandParts)-1)])
        elif commandType % 3 == 0:
            processTime = randint(0,10)
            lastProcess = datetime.now()
            isProcessing = True
            while isProcessing:
                print(str(random()) + " ")
                sleep(0.1)
                if datetime.now() > lastProcess + timedelta(seconds=processTime):
                    isProcessing = False
        else:
            print(commandResponses[randint(0,len(commandResponses)-1)])
        sleep(0.5)

try:
    time_init = datetime.now()
    consoleOutput()
except KeyboardInterrupt:
    print("Work finished in "+str(datetime.now() - time_init))
    pass
