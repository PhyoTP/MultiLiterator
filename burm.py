consonants = {
    "က": "k",
    "ခ": "kh",
    "ဂ": "g",
    "ဃ": "gh",
    "င": "ng",
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
    'ူ': "oo",
    'ု': "oo(short)",
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
    "ဥ": "oo(short)",
    "ဦ": "oo"
}

def convertToEng(string):
    eng = []
    for i in string:
        if i in consonants:
            if eng != []:
                eng.append(" ")
            eng.append(consonants[i])
            eng.append("ah(short)")
        elif i in semi_consonants:
            if i == "ှ":
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
        elif i == "်":
            if eng[-1] == "aww":
                eng[-1] = "aw"
            else:
                match eng[-2]:
                    case "k":
                        if eng[-4] == "aww":
                            del eng[-3:]
                            eng[-1] = "au(strong)"
                        elif eng[-4] == "oh":
                            del eng[-3:]
                            eng[-1] = "ai(strong)"
                        else:
                            del eng[-3:]
                            eng[-1] = "eh(strong)"
                    case "y":
                        del eng[-3:]
                        eng[-1] = "eh"
                    case "s":
                        del eng[-3:]
                        eng[-1] = "ih(strong)"
                    case "ng":
                        if eng[-4] == "aww":
                            del eng[-3:]
                            eng[-1] = "au"
                        elif eng[-4] == "oh":
                            del eng[-3:]
                            eng[-1] = "ai"
                        else:
                            del eng[-3:]
                            eng[-1] = "ih"
                    case "t" | "p":
                        if eng[-4] == "ee(short)":
                            del eng[-3:]
                            eng[-1] = "ate(strong)"
                        elif eng[-4] == "oo(short)":
                            del eng[-3:]
                            eng[-1] = "oah(strong)"
                        elif eng[-5] == "w":
                            del eng[-4:]
                            eng[-1] = "ut(strong)"
                        else:
                            del eng[-3:]
                            eng[-1] = "at(strong)"
                        
        elif i == "့":
            eng.append("(short)")
        elif i in punctuation:
            eng.append(punctuation[i])
        elif i in word_vowels:
            if eng != []:
                eng.append(" ")
            eng.append(word_vowels[i])
        else:
            eng.append(i)
    # print(eng)
    return "".join(eng)
print(convertToEng(""))
# print(list("ဪ"))