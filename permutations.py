from random import randint

"""
You have a list: [a,b,c,d]
find how many permutations of it there are.

Hints: the number of permutations is n factorial
since n = 4
we have 1*2*3*4 = 24

we should be returning a set of 
"""
myset = set()
print(type(myset))
mylist = 'abcd'

# perms = 0
# while(perms is not 24):
#     new_list = "0000"
#     for i in range(4):
#         target = mylist[i]
#         rand = randint(0,3)
#         print(rand)
#         new_list[rand] = target
#     if 0 not in new_list:
#         myset.add(new_list)
#     perms = len(myset)        
        


# def try_positions(l):
#     for i in enumerate(l):

#         print(i)
#         k = 

# # take the first one
# # swap with the one next to it
# # keep doing that until it gets to the end

# ['b', 'a', 'c', 'd']
# ['b', 'c', 'a', 'd']
# ['b', 'c', 'd', 'a']

# # take the one which is now at the beginning
# ['c', 'b', 'd', 'a']
# ['c', 'd', 'b', 'a']
# ['c', 'd', 'a', 'b']

# # do it again
# ['d', 'c', 'a', 'b']
# ['d', 'a', 'c', 'b']
# ['d', 'a', 'b', 'c']

# # you can do it for all 4
# ['c', 'd', 'a', 'b']
# ['c', 'a', 'd', 'b']
# ['c', 'a', 'b', 'd']

# # that gets us to 12 + original

# idkyet(mylist)