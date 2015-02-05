
# Python 3
# To run this code, change the file listed in the first for loop
# It needs to be in the same directory as where the file is run
# Those codes are usually find at
# http://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP932.TXT
# This code is simply used to make those codepage more readable
# It prints to the command line, thus you simply need to run it as:
# codeToUnicode.py > CP932_readable.txt
# Don't forget that some characters are visible in any font
for line in open("CP932.txt"):
    try: # ignore the comments
        code, uni, comment = line.split("\t")
        comment = comment.rstrip()
    except ValueError:
        print(line, end="")
        continue
    try:
        if "\n" in chr(int(uni, 16)) or "\t" in chr(int(uni, 16)) or "\r" in chr(int(uni, 16)):
            print(code, uni, repr(chr(int(uni, 16))), comment)
            continue
        print(code, uni, chr(int(uni, 16)), comment)
    except ValueError:
        print(code, uni,comment)
