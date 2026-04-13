import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            font=str(sys.argv[2])
        else:
            sys.exit('Not a Valid Font')
    else:
        sys.exit('Invalid command')
elif len(sys.argv) == 1:
    font=random.choice(fonts)
else:
    sys.exit("Invalid ")

text = input('Input: ')
figlet.setFont(font=font)
print(figlet.renderText(text))
