
for line in open("CP950.txt"):
    try:
        code, uni, comment = line.split("\t")
    except ValueError:
        continue
    try:
        print(chr(int(uni, 16)),end=",")
    except ValueError:
        print(uni)
