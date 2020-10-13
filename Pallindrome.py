def Is_pallendrome(str2):
    return str2[::-1] == str2
def is_sentence(sentence):
    str1=""
    for char in sentence:
        if char.isalnum():
            str1+=char
    return str1

sentence=(input("enter the Word.......").casefold())
str2=is_sentence(sentence)
if Is_pallendrome(str2):
    print("{} is pallendrome".format(sentence))
else:
    print("{} is not pallendrome".format(sentence))
