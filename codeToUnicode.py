
# Python 3
# To run this code, change the file listed in the first for loop
# It needs to be in the same directory as where the file is run
# Those codes are usually find at
# http://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP932.TXT
# This code is simply used to make those codepage more readable
# It prints to the command line, thus you simply need to run it as:
# codeToUnicode.py > CP932_readable.txt
# Don't forget that some characters are visible in any font
allCharacters = []
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
        allCharacters.append(chr(int(uni, 16)))
    except ValueError:
        print(code, uni,comment)


#print()
#print("".join(allCharacters))

bad = { a for a in '''"'*;?[\]`{|}ー―‐～＋－±ＡゼソゾチボポマЪЫЬЯклмⅧⅨⅩ㌔閏噂云荏閲榎厭骸浬馨柿顎掛笠擬欺犠義宮弓急啓圭珪形鶏芸迎梗構江港砿鋼閤纂蚕讃餐施旨枝充十従汁旬楯殉深申疹秦須酢図措曾曽疏捜掃挿端箪綻蛋畜竹筑甜貼転伝怒倒党納能脳覗倍培媒票表評描府怖扶房暴望冒本翻凡夕予余輿養慾抑麓禄肋倭兌兔兢兪几處凩喙喀咯啻嘴嘶嘲媼媾嫋嫣學斈孺彈彌彎彖悳忿怡拏拿拆拜掉掟掵杣杤枉杼桀桍栲歇歃歉歔毬毫毳濕濬濔濮炮烟烋畆畚畩畫痣痞痾禺秉秕秡窖窩竈綣綵緇總縵縹繃膽臀臂臍艝艚艟藜藹蘊藾蛔蛞蛩觴觸訃訌諚諫諳躰軆躱軈轆轎轗鐚鐔鐓鐐閔閖閘饉饅饐饒驅驂驀鷦鷭鷯鸛黠黥黨倞偆偰僴垬埈埇劯砡硎礰葈蒴蕓∵纊褜蓜傔僴僘犱犾猤玽硺礰礼'''}
print("BAD")
print("".join(bad))
allCharacters = set(allCharacters) - bad
print("GOOD")
allCharacters = sorted(list(allCharacters))
print("".join(allCharacters))
