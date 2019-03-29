"""
Increment a string integer without converting it to an int
"""

def increment_digit(digit):
    keys = {'9':'0', '0':'1', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9'}
    return keys[digit]

def increment_number(num):
    # case 1: the number is 1 digit
    # case 2: the number is 9
    # case 3: the number is more than one digit that does not end in a 9
    # case 4: the number is more than one digit, ends in a 9 and maybe has more 9s up the chain

assert increment_digit('1') is '2'
# assert increment('11') == '12' 
# assert increment('9') == '10'
# assert increment('119') == '120'
# assert increment('999') == '1000'