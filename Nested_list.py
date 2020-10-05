menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
#Just nesting the list
for nlists in menu:
    if "spam" not in nlists:
        print(nlists)
    else:
        no_of_counts=nlists.count("spam")
        for counts in range(no_of_counts):
            nlists.remove("spam")
        print(nlists)
        
