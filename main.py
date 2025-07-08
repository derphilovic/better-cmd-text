lines = ["","","","","",""]
editedLine = 0
header = "HHEAD"
#arrays of doom
A = ["    _    ","   / \   ","  / _ \  "," / ___ \ ","/_/   \_\\",""]
D = [" ____  ","|  _ \ ","| | | |","| |_| |","|____/ ",""]
E = [" _____ ","| ____|","|  _|  ","| |___ ","|_____|",""]
H = [" _   _ ","| | | |","| |_| |","|  _  |","|_| |_|",""]
#main loop
while editedLine != 5:
    for letter in header:
            if letter == "H":
                lines[editedLine] += H[editedLine]
            elif letter == "A":
                lines[editedLine] += A[editedLine]
            elif letter == "E":
                lines[editedLine] += E[editedLine]
            elif letter == "D":
                lines[editedLine] += D[editedLine]
    print(lines[editedLine])
    editedLine += 1