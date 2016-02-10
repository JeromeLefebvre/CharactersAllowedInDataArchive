
# THe various code page used:
# CP392 is for Japanese: https://en.wikipedia.org/wiki/Code_page_932
# CP950 is used for some chinese langauges
# https://en.wikipedia.org/wiki/Code_page_950
# CP936 for simplified chinese: https://en.wikipedia.org/wiki/Code_page_936
# CP949 is for korean: https://en.wikipedia.org/wiki/Code_page_949
code_page = "CP932.txt"


# Generate a list of characters that cannot be used in tag name or properties
# This is according to:
# https://techsupport.osisoft.com/Troubleshooting/KB/KB00043
bad_for_tags_raw = [a for a in '''*\?;{}[]|\`'"'''] + ["\n", "\r", "\t"]
bad_for_properties_raw = [a for a in '''•'?|`"'''] + ["\n", "\r", "\t"]

# Converting the characters to hex format to look up in the code page
bad_for_tags = tuple(hex(ord(a)).swapcase()[2:] for a in bad_for_tags_raw)
bad_for_properties = tuple(hex(ord(a)).swapcase()[2:] for a in bad_for_properties_raw)

valid_for_tags, invalid_for_tags = [], []
valid_for_properties, invalid_for_properties = [], []

for line in open(code_page):
    # Gets a valid line
    try:
        code, uni, comment = line.split("\t")
        converted = chr(int(uni, 16))
    except ValueError:
        continue
    if code[2:4] in bad_for_tags or code[4:] in bad_for_tags:
        invalid_for_tags.append(converted)
    else:
        valid_for_tags.append(converted)
    if code[2:4] in bad_for_properties or code[4:] in bad_for_properties:
        invalid_for_properties.append(converted)
    else:
        valid_for_properties.append(converted)
    if converted == '!':
        break

print('Valid for tags:')
print(''.join(valid_for_tags))
print()
print('Invalid for tags:')
print(''.join(invalid_for_tags))
print()
print('Valid for properties:')
print(''.join(valid_for_properties))
print()
print('Invalid for properties:')
print(''.join(invalid_for_properties))
