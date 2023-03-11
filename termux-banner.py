
bgreen="\033[37;96m"       # Green

p = "\033[37;95m"   #Pink

b = "\033[94m"          #Blue

bgreen1= "\033[37;43m"       # Green1

bgreen3 = "\033[93m"   #Green2

cf="\033[0m"       # Text Reset

import time

import sys

logo = """

Md Sabbir Hosen Shakib

"""

for x in logo:

 sys.stdout.write(b+x+cf)

 sys.stdout.flush()

 time.sleep(0.05)

sabbir = ("""

######     ###    ########  ########  #### ########

##    ##   ## ##   ##     ## ##     ##  ##  ##     ##

##        ##   ##  ##     ## ##     ##  ##  ##     ##

 ######  ##     ## ########  ########   ##  ########

      ## ######### ##     ## ##     ##  ##  ##   ##

##    ## ##     ## ##     ## ##     ##  ##  ##    ##

 ######  ##     ## ########  ########  #### ##     ##

 

 

 

 """)

for s in sabbir:

 sys.stdout.write(p+s+cf)

 sys.stdout.flush()

 time.sleep(0.009)

line =  '''--------------------------------------------------------------------------------

'''

for l in line:

 sys.stdout.write(b+l+cf)

 sys.stdout.flush()

 time.sleep(0.05)

welcome = """Welcome to Termux By 𝙎𝙖𝙗𝙗𝙞𝙧 彡 """

for w in welcome:

 sys.stdout.write(b+w+cf)

 sys.stdout.flush()

 time.sleep(0.05)
