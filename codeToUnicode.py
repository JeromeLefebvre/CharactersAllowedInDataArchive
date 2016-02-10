
# Python 3
# Characters in codepages can be found in pages such as the one below
# http://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP932.TXT
# This script simply adds readable version of each characters if possible

# specifiy the codepage
codepage = 'codepages/CP932.txt'
allCharacters = []
for line in open(codepage):
    try:
        code, uni, comment = line.split("\t")
        comment = comment.rstrip()
    except ValueError:
        print(line, end="")
        continue
    try:
        converted = chr(int(uni, 16))
        if converted in ["\n", "\t", "\r", '\x0c', '\x0b']:
            print(code, uni, repr(converted), comment)
            continue
        print(code, uni, converted, comment)
    except ValueError:
        print(code, uni, comment)
