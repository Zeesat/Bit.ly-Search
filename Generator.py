# import string
# from itertools import product

# def gen_all(max_lenght=6):
#     charset = string.ascii_uppercase + "0123456789"
#     for lenght in range (1, max_lenght + 1):
#         for p in product(charset, repeat=lenght):
#             yield ''.join(p)

# g = gen_all(6)

# for _ in range(20000):
#     print(next(g))

g = "ABC"
c = "DEF"
print(c + g)