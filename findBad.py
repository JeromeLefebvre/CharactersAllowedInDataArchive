

# Generate a list of bad characters
bad_character_raw = [a for a in '''*\?;{}[]|\`'"''']

# which we store in the correct hex character
bad_character = tuple(hex(ord(a)).swapcase()[2:] for a in bad_character_raw + ["\n", "\r", "\t"])

detail = False
i = 0
for line in open("CP950.txt"):
    try:
        code, uni, comment = line.split("\t")
    except ValueError:
        continue
    if code[2:4] in bad_character or code[4:] in bad_character:
        i += 1
        print(chr(int(uni, 16)),end=",")
        if detail:
            print(chr(int(uni, 16)), "is rejected since its code", code , "includes", end=" ")
            if code[2:4] in bad_character:
                print(chr(int(code[2:4], 16)), " which has code", code[2:4])
            if code[4:] in bad_character:
                print(chr(int(code[4:], 16)), " which has code", code[2:4])

print(i)
