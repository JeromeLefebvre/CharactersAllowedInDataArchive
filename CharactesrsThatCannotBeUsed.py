
code_page = "CP950.txt"

# Generate a list of characters that cannot be used in tag name
# This is done according to: https://techsupport.osisoft.com/Troubleshooting/KB/KB00043
bad_character_raw = [a for a in '''*\?;{}[]|\`'"'''] + ["\n", "\r", "\t"]

# Converting the characters to hex format to look up in the code page
bad_character = tuple(hex(ord(a)).swapcase()[2:] for a in bad_character_raw )

detail = False
for line in open(code_page):
    # The only lines of values in the file are those with both an unicode and code value
    try:
        code, uni, comment = line.split("\t")
    except ValueError:
        continue
    if code[2:4] in bad_character or code[4:] in bad_character:
        try:
            print(chr(int(uni, 16)),end="\n")
        except UnicodeEncodeError:
            print('cannot print:', uni)
        if detail:
            print(chr(int(uni, 16)), "is rejected since its code", code , "includes", end=" ")
            if code[2:4] in bad_character:
                print(chr(int(code[2:4], 16)), " which has code", code[2:4])
            if code[4:] in bad_character:
                print(chr(int(code[4:], 16)), " which has code", code[2:4])


