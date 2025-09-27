#modules
import os
import cmdstyler as cs
#split screen output
def split(count: int = 1):
    cs.cursor.clear("system")
    ts = os.get_terminal_size()
    a = 0
    b = 0
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

split()