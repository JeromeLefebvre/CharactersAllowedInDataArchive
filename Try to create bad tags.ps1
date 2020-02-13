$badCharacters = "'*;?[\]`{|}ー―‐～＋－±ＡゼソゾチボポマЪЫЬЯклмⅧⅨⅩ㌔閏噂云荏閲榎厭骸浬馨柿顎掛笠擬欺犠義宮弓急啓圭珪形鶏芸迎梗構江港砿鋼閤纂蚕讃餐施旨枝充十従汁旬楯殉深申疹秦須酢図措曾曽疏捜掃挿端箪綻蛋畜竹筑甜貼転伝怒倒党納能脳覗倍培媒票表評描府怖扶房暴望冒本翻凡夕予余輿養慾抑麓禄肋倭兌兔兢兪几處凩喙喀咯啻嘴嘶嘲媼媾嫋嫣學斈孺彈彌彎彖悳忿怡拏拿拆拜掉掟掵杣杤枉杼桀桍栲歇歃歉歔毬毫毳濕濬濔濮炮烟烋畆畚畩畫痣痞痾禺秉秕秡窖窩竈綣綵緇總縵縹繃膽臀臂臍艝艚艟藜藹蘊藾蛔蛞蛩觴觸訃訌諚諫諳躰軆躱軈轆轎轗鐚鐔鐓鐐閔閖閘饉饅饐饒驅驂驀鷦鷭鷯鸛黠黥黨倞偆偰僴垬埈埇劯砡硎礰葈蒴蕓∵纊褜蓜傔僴僘犱犾猤玽硺礰礼"

$conn = Connect-PIDataArchive -PIDataArchiveMachineName localhost


foreach ($index in 1..$a.Length) {
    $badCharacter = $badCharacters[$index]
    $tagName = "T" + $badCharacter
    Write-Output $tagName
    $c = Add-PIPoint -Connection $conn -Name $tagName
    if ($index -gt 50) {
        break
    }
}