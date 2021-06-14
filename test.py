text = str(input())
for i in text:
    if i in ["a","e","i","o","u"]:
        print("vowel")
    elif i in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        print("consonant")
    else:
        break