"""
Given two arrays:
1. Contains words
2. Contains NAUGHTY words

Return array1 with the naughty words removed

My solution1:
array2 should be a set to make things faster

For each word in array1, check if it is in array2(now a set).
if so, replace it with [REDACTED]
"""

censor = censor_list

censored = {"heart", "meet", "discuss", "strategy"}

text = "It's true, he has a big heart. I'm going to meet him again tonight to discuss our strategy."

def censor_simple(text, banned):
    text = text.split()
    for index, word in enumerate(text):
        if word in banned:
            text[index] = "[REDACTED]"
    return " ".join(text)

def censor_list(text, banned):
    return [word for word in text if word in banned word = "[REDACTED]"]


print(censor(text, censored))