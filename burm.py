from nyathetdetector import classify
def convertToEng(string, debug=False):
    consonants = {
        "က": "k",
        "ခ": "kh",
        "ဂ": "g",
        "ဃ": "gh",
        "င": "ng",
        'ဉ': "ng",
        "စ": "s",
        "ဆ": "ss",
        "ဇ": "z",
        "ဈ": "zz",
        "ည": "ny",
        "ဋ": "t",
        "ဌ": "tt",
        "ဍ": "d",
        "ဎ": "dh",
        "ဏ": "n",
        "တ": "t",
        "ထ": "tt",
        "ဒ": "d",
        "ဓ": "dh",
        "န": "n",
        "ပ": "p",
        "ဖ": "pp",
        "ဗ": "b",
        "ဘ": "bh",
        "မ": "m",
        "ယ": "y",
        "ရ": "y",
        "လ": "l",
        "ဝ": "w",
        "သ": "th",
        "ဟ": "h",
        "ဠ": "l",
        "အ": ""
    }
    semi_consonants = {
        "ျ": "y",
        "ြ": "y",
        "ွ": "w",
        "ှ": "h"
    }
    vowels = {
        'ီ': "ee",
        'ိ': "ee(short)",
        'ေ': "ay",
        'ဲ': "ehh",
        'ူ': "uu",
        'ု': "uu(short)",
    }
    punctuation = {
        "။": ".",
        "၊": ","
    }
    word_vowels = {
        "ဣ": "ee(short)",
        "ဤ": "ee",
        "ဧ": "ay",
        "ဩ": "aww",
        "ဪ": "aw",
        "ဥ": "uu(short)",
        "ဦ": "uu"
    }
    numbers = {
        "၀": "0",
        "၁": "1",
        "၂": "2",
        "၃": "3",
        "၄": "4",
        "၅": "5",
        "၆": "6",
        "၇": "7",
        "၈": "8",
        "၉": "9"
    }
    eng = []
    dot = False
    for index, i in enumerate(string):
        if i in consonants:
            if eng != []:
                eng.append(" ")
                dot = 0
            eng.append(consonants[i])
            eng.append("ah(short)")
        elif i in semi_consonants:
            if i == "ှ":
                if eng[-2] == "y":
                    eng[-2] = "sh"
                else:
                    count = -2
                    while True:
                        if eng[count] in semi_consonants.values():
                            count-=1
                        else:
                            break
                    eng.insert(count, semi_consonants[i])
            elif i == "ြ" or i == "ျ":
                if eng[-2] == "k":
                    eng[-2] = "chy"
                elif eng[-2] == "kh":
                    eng[-2] = "ch"
                else:
                    eng[-2] = eng[-2] + "y"
            else:
                eng.insert(-1, semi_consonants[i])
        elif i in vowels:
            if i == 'ု' and eng[-1] == "ee(short)":
                eng[-1] = "oh"
            else:
                eng[-1] = vowels[i]
        elif i in ["း", "ာ","ါ"]:
            if i == "ာ" and eng[-1] == "ay":
                eng[-1] = "aww"
            elif "(short)" in eng[-1]:
                eng[-1] = eng[-1][:-7]
            else:
                eng.append(eng[-1][-1])
        elif i == "်" or i == "္":
            if eng[-1] == "aww":
                eng[-1] = "aw"
            else:
                match eng[-2-dot]:
                    case "k" | "g":
                        if eng[-4] == "aww":
                            del eng[-3:]
                            eng[-1] = "auʔ"
                        elif eng[-4] == "oh":
                            del eng[-3:]
                            eng[-1] = "aiʔ"
                        else:
                            del eng[-3:]
                            eng[-1] = "ehʔ"
                    case "y":
                        del eng[-3:]
                        eng[-1] = "eh"
                    case "s":
                        del eng[-3:]
                        eng[-1] = "ihʔ"
                    case "ng":
                        if dot:
                            eng.pop()
                        if eng[-4] == "aww":
                            del eng[-3:]
                            eng[-1] = "aung"
                        elif eng[-4] == "oh":
                            del eng[-3:]
                            eng[-1] = "aing"
                        else:
                            del eng[-3:]
                            eng[-1] = "in"
                        if dot:
                            eng.append("(short)")
                    case "t" | "p" | "th" | "d" | "b":
                        if eng[-4] == "ee(short)":
                            del eng[-3:]
                            eng[-1] = "ayʔ"
                        elif eng[-4] == "uu(short)":
                            del eng[-3:]
                            eng[-1] = "oahʔ"
                        elif eng[-5] == "w":
                            del eng[-4:]
                            eng[-1] = "uuʔ"
                        else:
                            del eng[-3:]
                            eng[-1] = "eahʔ"
                    case "n" | "m":
                        if dot:
                            eng.pop()
                        if eng[-4] == "ee(short)":
                            del eng[-3:]
                            eng[-1] = "ein"
                        elif eng[-4] == "uu(short)":
                            del eng[-3:]
                            eng[-1] = "one"
                        elif eng[-5] == "w":
                            del eng[-4:]
                            eng[-1] = "un"
                        else:
                            del eng[-3:]
                            eng[-1] = "an"
                        if dot:
                            eng.append("(short)")
                    case "ny":
                        if eng[-5] == "sh":
                            del eng[-3:]
                            eng[-1] = "ay"
                        elif eng[-5] == "m":
                            del eng[-3:]
                            eng[-1] = "y"
                            eng.append("ee")
                        else:
                            word = ""
                            phrase = ""
                            sentence = ""
                            ee = 0
                            eh = 0

                            
                            word_start, word_stop = index-2, index+1
                            while True:
                                if string[word_start] in consonants or string[word_start] == "ဧ":
                                    break
                                word_start -= 1
                            if len(string) >= index+2:
                                if string[index+1] == "း":
                                    word_stop += 1
                            word = "(" + string[word_start:word_stop] + ")"
                            if debug:
                                print(word)
                            prediction = classify(word)
                            if debug:
                                print(prediction["class_name"])
                            if prediction["class_name"] == "ee":
                                ee += 1
                            elif prediction["class_name"] == "eh":
                                eh += 1

                            start, stop = index, index
                            brake = [" ", "။", "၊"]
                            while True:
                                if start == 0:
                                    break
                                if string[start] in brake:
                                    break
                                start -= 1
                            while True:
                                if stop == len(string)-1:
                                    break
                                if string[stop] in brake:
                                    break
                                stop += 1
                            phrase = string[start:stop+1]
                            phrase = phrase[:word_start-start] + "(" + phrase[word_start:word_stop] + ")" + phrase[word_stop-start:]
                            if debug:
                                print(phrase)
                            prediction = classify(phrase)
                            if debug:
                                print(prediction["class_name"])
                            if prediction["class_name"] == "ee":
                                ee += 1
                            elif prediction["class_name"] == "eh":
                                eh += 1

                            start, stop = index, index
                            brake = ["။", "၊"]
                            while True:
                                if start == 0:
                                    break
                                if string[start] in brake:
                                    break
                                start -= 1
                            while True:
                                if stop == len(string)-1:
                                    break
                                if string[stop] in brake:
                                    break
                                stop += 1
                            sentence = string[start:stop+1]
                            sentence = sentence[:word_start-start] + "(" + sentence[word_start:word_stop] + ")" + sentence[word_stop-start:]
                            if debug:
                                print(sentence)
                            prediction = classify(sentence)
                            if debug:
                                print(prediction["class_name"])
                            if prediction["class_name"] == "ee":
                                ee += 1
                            elif prediction["class_name"] == "eh":
                                eh += 1

                            result = ""
                            if eh > ee:
                                result = "eh"
                            else:
                                result = "ee"
                            del eng[-3:]
                            eng[-1] = result
                    case _:
                        con = eng[-2]
                        del eng[-3:]
                        eng[-1] = "a"+con
        elif i == "့":
            eng.append("(short)")
            dot = True
        elif i in punctuation:
            eng.append(punctuation[i])
        elif i in word_vowels:
            if eng != []:
                eng.append(" ")
            eng.append(word_vowels[i])
        elif i == 'ံ':
            if eng[-1] == "ee(short)":
                eng[-1] = "ain"
            elif eng[-1] == "uu(short)":
                eng[-1] = "one"
            elif eng[-2] == "w":
                del eng[-1:]
                eng[-1] = "un"
            else:
                eng[-1] = "an"
        elif i == "ဿ":
            if eng[-1] == "ee(short)":
                eng[-1] = "ayʔ"
            elif eng[-1] == "uu(short)":
                eng[-1] = "oahʔ"
            elif eng[-2] == "w":
                del eng[-2:]
                eng[-1] = "uuʔ"
            else:
                eng[-1] = "eahʔ"
            eng.append(" ")
            eng.append("th")
            eng.append("ah(short)")
        elif i in numbers:
            if not eng[-1].isdigit():
                eng.append(" ")
            eng.append(numbers[i])
        else:
            eng.append(" ")
            eng.append(i)
            dot = 0
        if debug:
            print(eng)
    return "".join(eng)
print(convertToEng("""
တိုးတိုးနဲ့ စိုးမိုးက နေ့တိုင်း ဘာတွေအတူတူလုပ်သလဲ။
""")) # insert text here


def convertToJap(string):
    consonants = {
        "က": ["カ", "キ", "ク", "ケ", "コ"],
        "ခ": ["ッカ", "ッキ", "ック", "ッケ", "ッコ"],
        "ဂ": ["ガ", "ギ", "グ", "ゲ", "ゴ"],
        "ဃ": ["ッガ", "ッギ", "ッグ", "ッゲ", "ッゴ"],
        "င": ["ンガ", "ンギ", "ング", "ンゲ", "ンゴ"],
        "စ": ["サ", "シ", "ス", "セ", "ソ"],
        "ဆ": ["ッサ", "ッシ", "ッス", "ッセ", "ッソ"],
        "ဇ": ["ザ", "ジ", "ズ", "ゼ", "ゾ"],
        "ဈ": ["ッザ", "ッジ", "ッズ", "ッゼ", "ッゾ"],
        "ည": ["ニャ", "ニィ", "ニュ", "ニェ", "ニョ"],
        "ဋ": ["タ", "チ", "ツ", "テ", "ト"],
        "ဌ": ["ッタ", "ッチ", "ッツ", "ッテ", "ット"],
        "ဍ": ["ダ", "ヂ", "ヅ", "デ", "ド"],
        "ဎ": ["ッダ", "ッヂ", "ッヅ", "ッデ", "ッド"],
        "ဏ": ["ナ", "ニ", "ヌ", "ネ", "ノ"],
        "တ": ["タ", "チ", "ツ", "テ", "ト"],
        "ထ": ["ッタ", "ッチ", "ッツ", "ッテ", "ット"],
        "ဒ": ["ダ", "ヂ", "ヅ", "デ", "ド"],
        "ဓ": ["ッダ", "ッヂ", "ッヅ", "ッデ", "ッド"],
        "န": ["ナ", "ニ", "ヌ", "ネ", "ノ"],
        "ပ": ["パ", "ピ", "プ", "ペ", "ポ"],
        "ဖ": ["ッパ", "ッピ", "ップ", "ッペ", "ッポ"],
        "ဗ": ["バ", "ビ", "ブ", "ベ", "ボ"],
        "ဘ": ["ッバ", "ッビ", "ッブ", "ッベ", "ッボ"],
        "မ": ["マ", "ミ", "ム", "メ", "モ"],
        "ယ": ["ヤ", "イ", "ユ", "イェ", "ヨ"],
        "ရ": ["ヤ", "イ", "ユ", "イェ", "ヨ"],
        "လ": ["ラ", "リ", "ル", "レ", "ロ"],
        "ဝ": ["ワ", "イ", "ウ", "イェ", "ヲ"],
        "သ": ["タ", "チ", "ツ", "テ", "ト"],
        "ဟ": ["ハ", "イ", "フ", "イェ", "ホ"],
        "ဠ": ["ラ", "リ", "ル", "レ", "ロ"],
        "အ": ["ア", "イ", "ウ", "エ", "オ"]
    }
    ya = ["ャ", "ィ", "ュ", "ェ", "ョ"]
    semi_consonants = {
        "ျ": "y",
        "ြ": "y",
        "ွ": "w",
        "ှ": "h"
    }
    # vowels = {
    #     'ီ': "ee",
    #     'ိ': "ee(short)",
    #     'ေ': "ay",
    #     'ဲ': "ehh",
    #     'ူ': "uu",
    #     'ု': "uu(short)",
    # }
    punctuation = {
        "။": "。",
        "၊": "、"
    }
    # word_vowels = {
    #     "ဣ": "ee(short)",
    #     "ဤ": "ee",
    #     "ဧ": "ay",
    #     "ဩ": "aww",
    #     "ဪ": "aw",
    #     "ဥ": "uu(short)",
    #     "ဦ": "uu"
    # }
    class Word:
        def __init__(self, consonant, vowel, semi_consonant):
            self.consonant = consonant
            self.vowel = vowel
            self.semi_consonant = semi_consonant
        def __str__(self):
            if self.semi_consonant != []:
                word = [consonants, self.consonant, self.vowel]
                for i in self.semi_consonant:
                    match i:
                        case "y":
                            word.insert(2, 1)
                            word.insert(3, ya)
                        case "w":
                            word[-1] = 2
                            word += [consonants, 33, self.vowel]
                        case "h":
                            word = [consonants, 31, 0] + word
                words = []
                for i in word:
                    if type(i) == list:
                        words.append(i)
                    else:
                        words[-1] = words[-1][i]
                return "".join(words)
                        
            else:
                return consonants[self.consonant][self.vowel]
    jap = []
    for i in string:
        if i in consonants:
            jap.append(Word(i, 0, []))
        elif i in semi_consonants:
            index = -1
            while type(jap[index]) != Word:
                index -= 1
            jap[index].semi_consonant.append(semi_consonants[i])
        elif i in punctuation:
            jap.append(punctuation[i])
    word = ""
    for i in jap:
        word += str(i)
    return word
# print(convertToJap("ပျ"))