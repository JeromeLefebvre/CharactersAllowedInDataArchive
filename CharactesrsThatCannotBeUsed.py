
# THe various code page used:
# CP392 is for Japanese: https://en.wikipedia.org/wiki/Code_page_932
code_page = "CP932.txt"

# Generate a list of characters that cannot be used in tag name
# This is done according to:
# https://techsupport.osisoft.com/Troubleshooting/KB/KB00043
# For
bad_character_for_tags_raw = [a for a in '''*\?;{}[]|\`'"'''] + ["\n", "\r", "\t"]
bad_character_for_properties_raw = [a for a in '''•'?|`"'''] + ["\n", "\r", "\t"]

# Converting the characters to hex format to look up in the code page
bad_character_for_tags = tuple(hex(ord(a)).swapcase()[2:] for a in bad_character_for_tags_raw)
bad_character_for_properties = tuple(hex(ord(a)).swapcase()[2:] for a in bad_character_for_properties_raw)

detail = False
invalid_for_tags = []
invalid_for_properties = []

for line in open(code_page):
    # The only lines of values in the file are those with both
    # an unicode and code value
    try:
        code, uni, comment = line.split("\t")
    except ValueError:
        continue
    if code[2:4] in bad_character_for_tags or code[4:] in bad_character_for_tags:
        # No errors should occur in python3
        try:
            invalid_for_tags.append(chr(int(uni, 16)))
        except UnicodeEncodeError:
            print('cannot print:', uni)
        except ValueError:
            print('cannot print:', uni)
    if code[2:4] in bad_character_for_properties or code[4:] in bad_character_for_properties:
        # No errors should occur in python3
        try:
            invalid_for_properties.append(chr(int(uni, 16)))
        except UnicodeEncodeError:
            print('cannot print:', uni)
        except ValueError:
            print('cannot print:', uni)

        if detail:
            print(chr(int(uni, 16)), "is rejected since its code",
                  code, "includes")
            if code[2:4] in bad_character_for_tags:
                print(chr(int(code[2:4], 16)), " which has code", code[2:4])
            if code[4:] in bad_character_for_tags:
                print(chr(int(code[4:], 16)), " which has code", code[2:4])

print(''.join(invalid_for_tags))
print(''.join(invalid_for_properties))
