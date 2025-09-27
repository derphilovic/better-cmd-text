#modules
import os
import cmdstyler as cs
from textwrap import wrap
#split screen output
ts = os.get_terminal_size()
def split(count: int = 1):
    cs.cursor.clear("system")
    a = 0
    b = 0
    global scount
    scount = int(count) + int(1)
    while a < ts.lines:
        line = ""
        seperation = ts.columns / scount
        while b < int(count):
            line = line + " " * int(seperation - 1) + "|"
            b += 1
        b = 0
        print(line)
        a += 1
    cs.cursor.move(0, 0)

def printsplit(text: str, side: int = 0):
    line = ""
    cs.cursor.clear_line()
    space = ts.columns / scount - 1
    textlen = len(text)
    
    if textlen <= space:
        remspace = space - textlen
        line = text + " " * int(remspace) + "|"
        print(line, end="")
        cs.cursor.down()
        cs.cursor.back(500)
    else:
        #line = text[0:int(space)]
        lines = wrap(text, space)
        for line in lines:
            textlen = len(line)
            remspace = space - textlen
            line1 = str(line) + " " * int(remspace) + "|"
            print(line1, end="")
            cs.cursor.down()
            cs.cursor.back(500)

split(5)
printsplit("Halp")
printsplit("Halp too and I am a spudid guy that writes for fun and has no hobbies. Skibidi toilet is my favorite series, I enjoy watching it very much!")
cs.cursor.down(70)