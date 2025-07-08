lines = ["","","","","",""]
editedLine = 0
header = "BECHAD"
#arrays of doom
A = ["    _    ","   / \\   ","  / _ \\  "," / ___ \\ ","/_/   \\_\\",""]
B = [" ____  ","| __ ) ","|  _ \\ ","| |_) |","|____/ ",""]
C = ["  ____ "," / ___|","| |    ","| |___ "," \\____|",""]
D = [" ____  ","|  _ \\ ","| | | |","| |_| |","|____/ ",""]
E = [" _____ ","| ____|","|  _|  ","| |___ ","|_____|",""]
H = [" _   _ ","| | | |","| |_| |","|  _  |","|_| |_|",""]
#main loop - optimized
letter_map = {"H": H, "A": A, "E": E, "D": D, "B" : B, "C" : C}

for editedLine in range(5):
    for letter in header:
        if letter in letter_map:
            lines[editedLine] += letter_map[letter][editedLine]
    print(lines[editedLine])
