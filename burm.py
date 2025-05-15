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
                            eng[-1] = "aut"
                        elif eng[-4] == "oh":
                            del eng[-3:]
                            eng[-1] = "yt"
                        else:
                            del eng[-3:]
                            eng[-1] = "et"
                    case "y":
                        del eng[-3:]
                        eng[-1] = "eh"
                    case "s":
                        del eng[-3:]
                        eng[-1] = "it"
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
                            eng[-1] = "ait"
                        elif eng[-4] == "uu(short)":
                            del eng[-3:]
                            eng[-1] = "oat"
                        elif eng[-5] == "w":
                            del eng[-4:]
                            eng[-1] = "ut"
                        else:
                            del eng[-3:]
                            eng[-1] = "at"
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
                        if len(eng) >= 3:
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
                eng[-1] = "ait"
            elif eng[-1] == "uu(short)":
                eng[-1] = "oat"
            elif eng[-2] == "w":
                del eng[-2:]
                eng[-1] = "ut"
            else:
                eng[-1] = "at"
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
# print(convertToEng("အင်္ဂါ")) # insert text here


def convertToJap(string, debug=False):
    if debug:
        print(list(string))
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
        "ဝ": ["ワ", "ウィ", "ウ", "ウェ", "ヲ"],
        "သ": ["タ", "チ", "ツ", "テ", "ト"],
        "ဟ": ["ハ", "イ", "フ", "イェ", "ホ"],
        "ဠ": ["ラ", "リ", "ル", "レ", "ロ"],
        "အ": ["ア", "イ", "ウ", "エ", "オ"]
    }
    ya = ["ャ", "ィ", "ュ", "ェ", "ョ"]
    sha = ["シャ", "シ", "シュ", "シェ", "ショ"]
    semi_consonants = {
        "ျ": "y",
        "ြ": "y",
        "ွ": "w",
        "ှ": "h"
    }
    vowels = {
        'ီ': [1],
        'ိ': [1.5],
        'ေ': [3, 1],
        'ဲ': [3, 3],
        'ူ': [2],
        'ု': [2.5],
    }
    punctuation = {
        "။": "。",
        "၊": "、"
    }
    word_vowels = {
        "ဣ": [1.5],
        "ဤ": [1],
        "ဧ": [3, 1],
        "ဩ": [2, 4, "ー"],
        "ဪ": [2, 4],
        "ဥ": [2.5],
        "ဦ": [2]
    }
    class Word:
        def __init__(self, consonant, vowel, semi_consonant):
            self.consonant = consonant
            self.vowel = vowel
            self.semi_consonant = semi_consonant
        def __str__(self):
            word = []
            additional = ""
            count = 0
            dot = False
            for i in self.vowel:
                if type(i) == int:
                    if count > 0:
                        additional += consonants["အ"][i]
                elif type(i) == float:
                    if count > 0:
                        additional += consonants["အ"][int(i)] 
                    dot = True
                else:
                    additional += i
                    print(i)
                count += 1
            if dot:
                additional += "「短い」"
            if self.semi_consonant != []:
                for i in self.semi_consonant:
                    match i:
                        case "y":
                            if self.consonant == "က":
                                word.append("ち" + consonants["ယ"][int(self.vowel[0])] + additional)
                            elif self.consonant == "ခ":
                                word.append("ち" + ya[int(self.vowel[0])] + additional)
                            else:
                                word.append(consonants[self.consonant][1] + ya[int(self.vowel[0])] + additional)
                        case "w":
                            word.append(consonants[self.consonant][2] + consonants["အ"][int(self.vowel[0])] + additional)
                        case "h":
                            if self.consonant == "ယ" or self.consonant == "ရ":
                                word.append(sha[int(self.vowel[0])] + additional)
                            else:
                                word.append("匕" + consonants[self.consonant][int(self.vowel[0])] + additional)
            else:
                word.append(consonants[self.consonant][int(self.vowel[0])] + additional)
            return "".join(word)
    jap = []
    for index, i in enumerate(string):
        if i in consonants:
            jap.append(Word(i, [0.5], []))
        elif i in semi_consonants:
            jap[-1].semi_consonant.append(semi_consonants[i])
        elif i in punctuation:
            jap.append(punctuation[i])
        elif i in vowels:
            if i == 'ု' and jap[-1].vowel == [1.5]:
                jap[-1].vowel = [4]
            else:
                jap[-1].vowel = vowels[i]
        elif i in ["း", "ာ","ါ"]:
            if i == "ာ" and jap[-1].vowel == [3, 1]:
                jap[-1].vowel = [2, 4, "ー"]
            elif jap[-1].vowel[-1] % 1 != 0:
                jap[-1].vowel[-1] = int(jap[-1].vowel[-1])
            else:
                jap[-1].vowel.append("ー")
        elif i == "်" or i == "္":
            if jap[-1].vowel == [2, 4, "ー"]:
                del jap[-1].vowel[-1]
            else:
                con = jap[-1]
                del jap[-1]
                match consonants[con.consonant][0]:
                    case "カ" | "ガ":
                        if jap[-1].vowel == [2, 4 , "ー"]:
                            jap[-1].vowel = [0, 2, "ット"]
                        elif jap[-1].vowel == [4]:
                            jap[-1].vowel = [0, 1, "ット"]
                        else:
                            jap[-1].vowel = [3, "ット"]
                    case "ヤ":
                        jap[-1].vowel = [3]
                    case "サ":
                        jap[-1].vowel = [1, "ット"]
                    case "ンガ":
                        if jap[-1].vowel == [2, 4 , "ー"]:
                            jap[-1].vowel = [0, 2, "ン"]
                        elif jap[-1].vowel == [4]:
                            jap[-1].vowel = [0, 1, "ン"]
                        else:
                            jap[-1].vowel = [1, "ン"]
                    case "タ" | "パ" | "ダ" | "バ":
                        if jap[-1].vowel == [1.5]:
                            jap[-1].vowel = [3, 1, "ット"]
                        elif jap[-1].vowel == [2.5]:
                            jap[-1].vowel = [4, 2, "ット"]
                        elif "w" in jap[-1].semi_consonant:
                            jap[-1].semi_consonant.remove("w")
                            jap[-1].vowel = [2, "ット"]
                        else:
                            jap[-1].vowel = [0, "ット"]
                    case "ナ" | "マ":
                        if jap[-1].vowel == [1.5]:
                            jap[-1].vowel = [3, 1, "ン"]
                        elif jap[-1].vowel == [2.5]:
                            jap[-1].vowel = [4, 2, "ン"]
                        elif "w" in jap[-1].semi_consonant:
                            jap[-1].semi_consonant.remove("w")
                            jap[-1].vowel = [2, "ン"]
                        else:
                            jap[-1].vowel = [0, "ン"]
                    case "ニャ":
                        if (jap[-1].consonant == "ယ" or jap[-1].consonant == "ရ") and "h" in jap[-1].semi_consonant:
                            jap[-1].vowel = [3, 1]
                        elif jap[-1].consonant == "မ":
                            jap[-1].semi_consonant.append("y")
                            jap[-1].vowel = [1]
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
                            
                            if ee > eh:
                                jap[-1].vowel = [1]
                            else:
                                jap[-1].vowel = [3]
                    case _:
                        jap[-1].vowel = [0, consonants[con.consonant][4]]
        elif i == "့":
            jap[-1].vowel[-1] += 0.5
        elif i in word_vowels:
            jap.append(Word("", word_vowels[i], []))
        elif i == 'ံ':
            if jap[-1].vowel == [1.5]:
                jap[-1].vowel = [3, 1, "ン"]
            elif jap[-1].vowel == [2.5]:
                jap[-1].vowel = [4, 2, "ン"]
            elif "w" in jap[-1].semi_consonant:
                jap[-1].semi_consonant.remove("w")
                jap[-1].vowel = [2, "ン"]
            else:
                jap[-1].vowel = [0, "ン"]
        elif i == "ဿ":
            if jap[-1].vowel == [1.5]:
                jap[-1].vowel = [3, 1, "ッ"]
            elif jap[-1].vowel == [2.5]:
                jap[-1].vowel = [4, 2, "ッ"]
            elif "w" in jap[-1].semi_consonant:
                jap[-1].semi_consonant.remove("w")
                jap[-1].vowel = [2, "ッ"]
            else:
                jap[-1].vowel = [0, "ッ"]
            jap.append(Word("သ", [0.5], []))
        else:
            jap.append(i)
        if debug:
            print([[i, j.consonant, j.vowel, j.semi_consonant] for j in jap])
    word = ""
    for i in jap:
        word += str(i)
    return word
print(convertToJap("ဖြိုးသက်ပိုင်",debug=True))