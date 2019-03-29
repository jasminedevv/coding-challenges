"""
Problem: you have an array of socks. You need to figure out how many pairs of each pattern you have.

socks = ['chickens', 'flowers', 'red', 'red', 'flowers', 'chickens', 'flowers', 'christmas', 'flowers']

"""

# solution 1: make a histogram of each occurence and then divide each number for all the keys
def histogram(arr):
    hist = dict()
    for item in arr:
        try:
            hist[item] += 1
        except KeyError:
            hist[item] = 1
    return hist
            
def get_pairs(socks):
    hist = histogram(socks)
    for sock_type in hist:
        if hist[sock_type] % 2 == 0:
            hist[sock_type] /= 2
        else:
            hist[sock_type] = (hist[sock_type] - 1) / 2
    return hist

socks = ['chickens', 'flowers', 'red', 'red', 'flowers', 'chickens', 'flowers', 'christmas', 'flowers']

pairs = get_pairs(socks)

assert pairs['flowers'] == 2
assert pairs['chickens'] == 1
assert pairs['red'] == 1
assert pairs['christmas'] == 0

print("Solution works!")